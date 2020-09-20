from flask import request, render_template, session
from app import app, db
from app.main.legit.scraper.get_ig_info import insta_scrape
from app.main.config.models import User, Insta_info
from datetime import datetime
@app.route('/homepage')
def homepage():
    user = User.query.filter_by(username=session["curr"]).first()
    current_user = session["curr"]
    return render_template('homepage.html', curr = current_user, users=user.accounts)

@app.route('/homepage/<username>/<platform>')
def render_user(username, platform):
    print(username, platform)
    user = User.query.filter_by(username=username).first()
    current_user = session["curr"]
    if platform.lower() == "instagram":
        now = datetime.utcnow()
        profile = Insta_info.query.filter_by(username=username).first()
        print(profile)
        
        print(profile)
        if profile is not None:
            print('already in db')
            diff = profile.searched_last - now
            print(diff)
            if diff.days > 0:
                pass
            else:
                print('ok no api req fone')
                return render_template('homepage.html', curr=current_user, 
                                                        followers=profile.followers,
                                                        posts = profile.posts,
                                                        engagement=profile.engagement,
                                                        pfp_url=profile.pfp_url,
                                                        username=username,
                                                        platform='instagram')
                                                
        followers, posts, engagement, pfp_url, zz = insta_scrape(username)
        insta_to_insert = Insta_info(followers=followers,
                                     posts=posts,
                                     engagement=engagement,
                                     pfp_url=pfp_url,
                                     username=username)
        db.session.add(insta_to_insert)
        db.session.commit()
        return render_template('homepage.html', curr=current_user, 
                                                        followers=followers,
                                                        posts = posts,
                                                        engagement=engagement,
                                                        pfp_url=pfp_url,
                                                        username=username,
                                                        platform='instagram')
                                                    
    return render_template('homepage.html', curr=current_user, platform=platform)
#pprint(insta_scrape('katyperry'))

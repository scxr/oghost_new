from flask import request, render_template, session
from app import app, db
from app.main.legit.scraper.get_ig_info import insta_scrape
from app.main.legit.scraper.get_tt_info import tt_scrape
from app.main.legit.scraper.get_sc_info import snap_scrape
from app.main.config.models import User, Insta_info, Tiktok_info, Snapchat_info
from datetime import datetime
from flask_jwt_extended import jwt_required
@app.route('/homepage')
@jwt_required
def homepage():
    user = User.query.filter_by(username=session["curr"]).first()
    current_user = session["curr"]
    return render_template('homepage.html', curr = current_user, users=user.accounts)

@app.route('/homepage/<username>/<platform>')
@jwt_required
def render_user(username, platform):
    print(username, platform)
    user = User.query.filter_by(username=session["curr"]).first()
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
                return render_template('homepage.html', users=user.accounts,
                                                        curr=current_user, 
                                                        followers=profile.followers,
                                                        posts = profile.posts,
                                                        pfp_url=profile.pfp_url,
                                                        username=username,
                                                        platform='instagram',
                                                        bio=profile.bio,
                                                        following=profile.following)
        #return followers, following, posts, bio, pfp_url, username 
        followers, following, posts, bio, pfp_url, username = insta_scrape(username)
        insta_to_insert = Insta_info(followers=followers,
                                     posts=posts,
                                     pfp_url=pfp_url,
                                     username=username,
                                     bio=bio,
                                     following=following)
        db.session.add(insta_to_insert)
        db.session.commit()
        return render_template('homepage.html', curr=current_user, 
                                                        followers=followers,
                                                        posts = posts,
                                                        pfp_url=pfp_url,
                                                        username=username,
                                                        platform='instagram',
                                                        users=user.accounts,
                                                        bio=bio)


    elif platform.lower() == "tiktok":
        now = datetime.utcnow()
        profile = Tiktok_info.query.filter_by(username=username).first()
        print(profile)

        if profile is not None:
            print('db')
            diff = profile.searched_last - now
            if diff.days > 0:
                pass
            else:
                print("ok ntek")

                return render_template('homepage.html', users=user.accounts,
                                            curr=current_user, 
                                            profile=profile,
                                            username=username,
                                            platform='tiktok')

        tt_info = tt_scrape(username)
        profile = Tiktok_info(**tt_info)

        db.session.add(profile)
        db.session.commit()
        db.session.refresh(profile)
        return render_template('homepage.html', curr=current_user,
                                            users=user.accounts,
                                            profile=profile,
                                            username=username,
                                            platform="tiktok")

    elif platform.lower() == "snapchat":
        now = datetime.utcnow()
        profile = Snapchat_info.query.filter_by(username=username).first()
        print(profile)

        if profile is not None:
            diff = profile.searched_last - now
            if diff.days > 0:
                pass
            else:
                return render_template('homepage.html', users=user.accounts,
                            curr=current_user, 
                            profile=profile,
                            username=username,
                            platform='snapchat') 

        sc_info = snap_scrape(username)
        print(sc_info)
        profile = Snapchat_info(username=username, exists=sc_info)

        db.session.add(profile)
        db.session.commit()
        db.session.refresh(profile)
        return render_template('homepage.html', curr=current_user,
                                    users=user.accounts,
                                    profile=profile,
                                    username=username,
                                    platform="snapchat")

                                                    
    return render_template('homepage.html', curr=current_user, platform=platform)
#pprint(insta_scrape('katyperry'))


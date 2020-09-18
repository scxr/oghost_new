from flask import current_app
from sqlalchemy import create_engine
conf = current_app.config
engine = create_engine(f"mysql://{conf["MYSQL_USERNAME"]}:{conf["MYSQL_PASSWORD"]}@localhost/{conf["MYSQL_DATABASE"]}")

"""
mydb = mysql.connector.connect(
    host=current_app
)
"""
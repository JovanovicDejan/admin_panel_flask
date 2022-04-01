from flask import Flask
app = Flask(__name__)

from db.DB import DB as db
from models.user import User


db.create_table("""CREATE TABLE IF NOT EXISTS user(
                user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(150) NOT NULL UNIQUE,
                password VARCHAR(300) NOT NULL
                )ENGINE=INNODB""")

db.insert_into_query("INSERT INTO user (username, password) VALUES (%s, %s)", ("johndoe", "1234"))
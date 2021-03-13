from werkzeug.security import generate_password_hash
from app.models import db, User

def seed_users():

    demo = User(first_name="Demo", last_name="User", email="demo@aa.io", hashed_password=generate_password_hash("123"), zip="12345")
    ned = User(first_name="Ned", last_name="Bedder", email="ned@aa.io", hashed_password=generate_password_hash("123"), zip="12345")

    users = [demo, ned]

    for user in users:
        db.session.add(user)

    db.session.commit()


def undo_users():
    db.session.execute('TRUNCATE users;')
    db.session.commit()

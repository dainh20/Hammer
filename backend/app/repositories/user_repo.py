from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, username, email, password_hash):
    user = User(username=username, email=email, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email):
    return db.query(User).filter(User.email == email).first()
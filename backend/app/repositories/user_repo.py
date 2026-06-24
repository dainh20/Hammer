from sqlalchemy.orm import Session

from app.models.user import User


def create_user(
    db: Session,
    username: str,
    name: str,
    email: str,
    password_hash: str,
    phone: str,
    address: str
):
    user = User(
        username=username,
        name=name,
        email=email,
        password_hash=password_hash,
        phone=phone,
        address=address
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def get_user_by_email(
    db: Session,
    email: str
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def get_user_by_id(
    db: Session,
    user_id: int
):
    return (
        db.query(User)
        .filter(User.user_id == user_id)
        .first()
    )
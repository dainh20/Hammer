from sqlalchemy.orm import Session

from app.repositories import user_repo

from app.repositories.wallet_repo import (
    create_wallet
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(
    db: Session,
    data
):
    # =====================================
    # CHECK EMAIL EXISTS
    # =====================================
    existing_user = (
        user_repo.get_user_by_email(
            db,
            data.email
        )
    )

    if existing_user:
        raise Exception(
            "Email already exists"
        )

    # =====================================
    # HASH PASSWORD
    # =====================================
    hashed_password = hash_password(
        data.password
    )

    try:
        # =====================================
        # CREATE USER
        # =====================================
        user = user_repo.create_user(
            db=db,
            username=data.username,
            name=data.name,
            email=data.email,
            password_hash=hashed_password,
            phone=data.phone,
            address=data.address
        )

        # =====================================
        # CREATE WALLET
        # =====================================
        create_wallet(
            db,
            user.user_id
        )

        return user

    except Exception:
        db.rollback()
        raise


def login_user(
    db: Session,
    email: str,
    password: str
):
    # =====================================
    # FIND USER
    # =====================================
    user = user_repo.get_user_by_email(
        db,
        email
    )

    if not user:
        raise Exception(
            "Invalid credentials"
        )

    # =====================================
    # VERIFY PASSWORD
    # =====================================
    valid_password = verify_password(
        password,
        user.password_hash
    )

    if not valid_password:
        raise Exception(
            "Invalid credentials"
        )

    return user


def login_and_create_token(
    db: Session,
    username: str,
    password: str
):
    # =====================================
    # LOGIN
    # =====================================
    user = login_user(
        db,
        username,
        password
    )

    # =====================================
    # CREATE JWT TOKEN
    # =====================================
    token = create_access_token({
        "sub": str(user.user_id)
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
from sqlalchemy.orm import Session

from app.models.wallet import Wallet


def create_wallet(
    db: Session,
    user_id: int
):
    wallet = Wallet(
        user_id=user_id,
        balance=0,
        locked_balance=0
    )

    db.add(wallet)

    db.commit()

    db.refresh(wallet)

    return wallet


def get_wallet_by_user_id(
    db: Session,
    user_id: int
):
    return (
        db.query(Wallet)
        .filter(Wallet.user_id == user_id)
        .first()
    )


def update_balance(
    db: Session,
    user_id: int,
    amount: int
):
    wallet = get_wallet_by_user_id(
        db,
        user_id
    )

    wallet.balance += amount

    db.commit()

    db.refresh(wallet)

    return wallet
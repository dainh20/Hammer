from sqlalchemy.orm import Session

from app.repositories import wallet_repo

from app.repositories.wallet_repo import (
    create_wallet
)


def deposit_money(
    db: Session,
    user_id: int,
    amount: int
):
    # =====================================
    # VALIDATE AMOUNT
    # =====================================
    if amount <= 0:
        raise Exception(
            "Invalid amount"
        )

    # =====================================
    # GET WALLET
    # =====================================
    wallet = wallet_repo.get_wallet_by_user_id(
        db,
        user_id
    )

    # =====================================
    # AUTO CREATE WALLET
    # =====================================
    if not wallet:
        wallet = create_wallet(
            db,
            user_id
        )

    # =====================================
    # UPDATE BALANCE
    # =====================================
    return wallet_repo.update_balance(
        db,
        user_id,
        amount
    )
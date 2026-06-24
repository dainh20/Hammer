from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.repositories import (
    auction_repo,
    bid_repo
)
from app.repositories.bid_repo import (
    get_highest_bid
)
from app.repositories.wallet_repo import (
    get_wallet_by_user_id
)


def place_bid(
    db: Session,
    auction_id: int,
    user_id: int,
    amount: int
):
    try:
        # =====================================
        # LOCK AUCTION ROW
        # =====================================
        auction = (
            auction_repo.get_auction_for_update(
                db,
                auction_id
            )
        )

        # =====================================
        # VALIDATE AUCTION EXISTS
        # =====================================
        if not auction:
            raise Exception(
                "Auction not found"
            )

        # =====================================
        # VALIDATE STATUS
        # =====================================
        if auction.status != "active":
            raise Exception(
                "Auction is not active"
            )

        # =====================================
        # VALIDATE TIME
        # =====================================
        now = datetime.now(timezone.utc)

        if now < auction.start_time:
            raise Exception(
                "Auction has not started"
            )

        if now > auction.end_time:
            raise Exception(
                "Auction has ended"
            )

        # =====================================
        # SELLER CANNOT BID
        # =====================================
        if auction.seller_id == user_id:
            raise Exception(
                "Seller cannot bid on own auction"
            )

        # =====================================
        # GET CURRENT PRICE
        # =====================================
        previous_highest_bid = get_highest_bid(
            db,
            auction_id
        )

        current_price = (
            auction.current_price
            or auction.starting_price
        )

        wallet = get_wallet_by_user_id(
            db,
            user_id
        )

        if not wallet:
            raise Exception(
                "Wallet not found"
            )

        available_balance = (
            wallet.balance
            - wallet.locked_balance
        )

        if available_balance < amount:
            raise Exception(
                "Insufficient balance"
            )



        # =====================================
        # VALIDATE BID AMOUNT
        # =====================================
        if amount <= current_price:
            raise Exception(
                "Bid amount must be higher than current price"
            )

        if previous_highest_bid:
        
            # SAME USER RE-BID
            if previous_highest_bid.user_id == user_id:
            
                difference = (
                    amount
                    - previous_highest_bid.bid_amount
                )

                wallet.locked_balance += difference

            else:
                # UNLOCK OLD BIDDER
                old_wallet = get_wallet_by_user_id(
                    db,
                    previous_highest_bid.user_id
                )

                old_wallet.locked_balance -= (
                    previous_highest_bid.bid_amount
                )

                # LOCK NEW BIDDER
                wallet.locked_balance += amount

        else:
            # FIRST BID
            wallet.locked_balance += amount


        wallet = get_wallet_by_user_id(
            db,
            user_id
        )

        if not wallet:
            raise Exception(
                "Wallet not found"
            )

        available_balance = (
            wallet.balance
            - wallet.locked_balance
        )

        if available_balance < amount:
            raise Exception(
                "Insufficient balance"
            )

        # =====================================
        # CREATE BID
        # =====================================

        bid = bid_repo.create_bid(
            db=db,
            auction_id=auction_id,
            user_id=user_id,
            bid_amount=amount
        )

        # =====================================
        # UPDATE CURRENT PRICE
        # =====================================
        auction.current_price = amount
        # =====================================
        # COMMIT TRANSACTION
        # =====================================
        db.commit()

        db.refresh(bid)

        return bid

    except Exception:
        db.rollback()
        raise
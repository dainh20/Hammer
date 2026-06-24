import time
import app.models
from app.core.database import SessionLocal

from app.repositories.auction_repo import (
    get_expired_auctions
)

from app.repositories.auction_winner_repo import (
    create_auction_winner
)

from app.repositories.bid_repo import (
    get_winning_bid,
    get_latest_loser_bids
)

from app.repositories.wallet_repo import (
    get_wallet_by_user_id
)


def process_expired_auctions():

    db = SessionLocal()

    try:

        auctions = get_expired_auctions(
            db
        )

        for auction in auctions:

            print(
                f"Processing auction {auction.auction_id}"
            )

            # =====================================
            # GET WINNING BID
            # =====================================
            winning_bid = get_winning_bid(
                db,
                auction.auction_id
            )

            # =====================================
            # NO BID
            # =====================================
            if not winning_bid:

                auction.status = "ended"

                db.commit()

                print(
                    f"Auction {auction.auction_id} ended without bids"
                )

                continue

            # =====================================
            # CREATE AUCTION WINNER
            # =====================================
            create_auction_winner(
                db=db,
                auction_id=auction.auction_id,
                winner_id=winning_bid.user_id,
                winning_bid_id=winning_bid.id,
                final_price=winning_bid.bid_amount
            )

            # =====================================
            # UNLOCK LOSERS
            # =====================================
            loser_bids = get_latest_loser_bids(
                db,
                auction.auction_id,
                winning_bid.user_id
            )

            for loser_bid in loser_bids:

                loser_wallet = get_wallet_by_user_id(
                    db,
                    loser_bid.user_id
                )

                if not loser_wallet:
                    continue

                loser_wallet.locked_balance -= (
                    loser_bid.bid_amount
                )

                # SAFETY CHECK
                if loser_wallet.locked_balance < 0:
                    loser_wallet.locked_balance = 0

            # =====================================
            # UPDATE AUCTION STATUS
            # =====================================
            auction.status = "ended"

            db.commit()

            print(
                f"Auction {auction.auction_id} ended successfully"
            )

    except Exception as e:

        db.rollback()

        print(
            f"Worker error: {e}"
        )

    finally:

        db.close()


if __name__ == "__main__":

    print(
        "Auction worker started..."
    )

    while True:

        process_expired_auctions()

        time.sleep(10)
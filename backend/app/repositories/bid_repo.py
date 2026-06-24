from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.bid import Bid


# =====================================
# CREATE BID
# =====================================
def create_bid(
    db: Session,
    auction_id: int,
    user_id: int,
    bid_amount: int
):
    bid = Bid(
        auction_id=auction_id,
        user_id=user_id,
        bid_amount=bid_amount
    )

    db.add(bid)

    db.flush()

    return bid


# =====================================
# GET BID BY ID
# =====================================
def get_bid_by_id(
    db: Session,
    bid_id: int
):
    return (
        db.query(Bid)
        .filter(Bid.id == bid_id)
        .first()
    )


# =====================================
# GET ALL BIDS OF AUCTION
# =====================================
def get_bids_by_auction(
    db: Session,
    auction_id: int
):
    return (
        db.query(Bid)
        .filter(Bid.auction_id == auction_id)
        .order_by(Bid.bid_amount.desc())
        .all()
    )


# =====================================
# GET HIGHEST BID
# =====================================
def get_highest_bid(
    db: Session,
    auction_id: int
):
    return (
        db.query(Bid)
        .filter(Bid.auction_id == auction_id)
        .order_by(Bid.bid_amount.desc())
        .first()
    )


# =====================================
# GET WINNING BID
# =====================================
def get_winning_bid(
    db: Session,
    auction_id: int
):
    return (
        db.query(Bid)
        .filter(Bid.auction_id == auction_id)
        .order_by(Bid.bid_amount.desc())
        .first()
    )


# =====================================
# GET LOSER BIDS
# =====================================
def get_loser_bids(
    db: Session,
    auction_id: int,
    winner_user_id: int
):
    return (
        db.query(Bid)
        .filter(
            Bid.auction_id == auction_id,
            Bid.user_id != winner_user_id
        )
        .all()
    )


# =====================================
# GET LATEST LOSER BIDS
# =====================================
def get_latest_loser_bids(
    db: Session,
    auction_id: int,
    winner_user_id: int
):
    subquery = (
        db.query(
            Bid.user_id,
            func.max(Bid.bid_amount).label("max_bid")
        )
        .filter(
            Bid.auction_id == auction_id,
            Bid.user_id != winner_user_id
        )
        .group_by(Bid.user_id)
        .subquery()
    )

    return (
        db.query(Bid)
        .join(
            subquery,
            (Bid.user_id == subquery.c.user_id)
            &
            (Bid.bid_amount == subquery.c.max_bid)
        )
        .all()
    )
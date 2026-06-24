from sqlalchemy.orm import Session
from app.models.auction import Auction
from datetime import datetime, timezone


def create_auction(
    db: Session,
    auction: Auction
):
    db.add(auction)

    db.commit()

    db.refresh(auction)

    return auction


def get_auction_by_id(
    db: Session,
    auction_id: int
):
    return (
        db.query(Auction)
        .filter(Auction.auction_id == auction_id)
        .first()
    )




def get_auction_for_update(
    db: Session,
    auction_id: int
):
    return (
        db.query(Auction)
        .filter(Auction.auction_id == auction_id)
        .with_for_update()
        .first()
    )



def get_expired_auctions(
    db: Session
):
    now = datetime.now(
        timezone.utc
    )

    return (
        db.query(Auction)
        .filter(
            Auction.status == "active",
            Auction.end_time <= now
        )
        .all()
    )


def get_active_auction_by_item(
    db: Session,
    item_id: int
):
    return (
        db.query(Auction)
        .filter(
            Auction.item_id == item_id,
            Auction.status == "active"
        )
        .first()
    )
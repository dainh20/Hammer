from sqlalchemy.orm import Session
from app.models.auction import Auction
from app.repositories import auction_repo
from app.repositories.auction_repo import (
    get_active_auction_by_item
)

def create_auction(
    db: Session,
    seller_id: int,
    data
):
    auction = Auction(
        item_id=data.item_id,
        seller_id=seller_id,
        starting_price=data.starting_price,
        reserve_price=data.reserve_price,
        current_price=data.starting_price,
        start_time=data.start_time,
        end_time=data.end_time,
        status="draft"
    )

    existing_active_auction = (
        get_active_auction_by_item(
            db,
            data.item_id
        )
    )
    
    if existing_active_auction:
        raise Exception(
            "Item already has an active auction"
        )

    return auction_repo.create_auction(
        db,
        auction
    )



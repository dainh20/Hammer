from sqlalchemy.orm import Session

from app.models.auction_winner import (
    AuctionWinner
)


def create_auction_winner(
    db: Session,
    auction_id: int,
    winner_id: int,
    winning_bid_id: int,
    final_price: int
):
    winner = AuctionWinner(
        auction_id=auction_id,
        winner_id=winner_id,
        winning_bid_id=winning_bid_id,
        final_price=final_price
    )

    db.add(winner)

    db.commit()

    db.refresh(winner)

    return winner
from sqlalchemy import (
    Column,
    BigInteger,
    TIMESTAMP
)

from sqlalchemy.sql import func

from app.core.database import Base


class AuctionWinner(Base):
    __tablename__ = "auction_winners"

    auction_id = Column(
        BigInteger,
        primary_key=True
    )

    winner_id = Column(
        BigInteger,
        nullable=False
    )

    winning_bid_id = Column(
        BigInteger,
        nullable=False
    )

    final_price = Column(
        BigInteger,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )
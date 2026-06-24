from sqlalchemy import (
    Column,
    BigInteger,
    ForeignKey,
    TIMESTAMP
)

from sqlalchemy.sql import func

from app.core.database import Base


class Bid(Base):
    __tablename__ = "bid"

    id = Column(
        BigInteger,
        primary_key=True
    )

    auction_id = Column(
        BigInteger,
        ForeignKey("auctions.auction_id"),
        nullable=False
    )

    user_id = Column(
        BigInteger,
        ForeignKey("users.user_id"),
        nullable=False
    )

    bid_amount = Column(
        BigInteger,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )
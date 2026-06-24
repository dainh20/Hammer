from sqlalchemy import (
    Column,
    BigInteger,
    String,
    ForeignKey,
    TIMESTAMP
)

from sqlalchemy.sql import func

from app.core.database import Base


class Auction(Base):
    __tablename__ = "auctions"

    auction_id = Column(
        BigInteger,
        primary_key=True
    )

    item_id = Column(
        BigInteger,
        ForeignKey("items.id")
    )

    seller_id = Column(
        BigInteger,
        ForeignKey("users.user_id")
    )

    starting_price = Column(
        BigInteger,
        nullable=False
    )

    reserve_price = Column(
        BigInteger
    )

    current_price = Column(
        BigInteger
    )

    start_time = Column(
        TIMESTAMP(timezone=True),
        nullable=False
    )

    end_time = Column(
        TIMESTAMP(timezone=True),
        nullable=False
    )

    status = Column(
        String(20),
        default="draft"
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )
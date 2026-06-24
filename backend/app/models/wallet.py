from sqlalchemy import (
    Column,
    BigInteger,
    ForeignKey,
    TIMESTAMP
)

from sqlalchemy.sql import func

from app.core.database import Base


class Wallet(Base):
    __tablename__ = "wallets"

    user_id = Column(
        BigInteger,
        ForeignKey("users.user_id"),
        primary_key=True
    )

    balance = Column(
        BigInteger,
        default=0
    )

    locked_balance = Column(
        BigInteger,
        default=0
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
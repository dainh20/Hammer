from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Text,
    Integer,
    ForeignKey,
    TIMESTAMP
)

from sqlalchemy.sql import func

from app.core.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(
        BigInteger,
        primary_key=True
    )

    seller_id = Column(
        BigInteger,
        ForeignKey("users.user_id"),
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    description = Column(
        Text
    )

    category_id = Column(
        BigInteger
    )

    condition = Column(
        Integer
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
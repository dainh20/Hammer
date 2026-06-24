from sqlalchemy.orm import Session

from app.models.item import Item


def create_item(
    db: Session,
    item: Item
):
    db.add(item)

    db.commit()

    db.refresh(item)

    return item


def get_item_by_id(
    db: Session,
    item_id: int
):
    return (
        db.query(Item)
        .filter(Item.id == item_id)
        .first()
    )
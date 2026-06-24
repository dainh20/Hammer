from sqlalchemy.orm import Session

from app.models.item import Item

from app.repositories import item_repo


def create_item(
    db: Session,
    seller_id: int,
    data
):
    item = Item(
        seller_id=seller_id,
        title=data.title,
        description=data.description,
        category_id=data.category_id,
        condition=data.condition
    )

    return item_repo.create_item(
        db,
        item
    )
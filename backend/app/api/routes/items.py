from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.api.deps import (
    get_db,
    get_current_user
)

from app.models.user import User

from app.schemas.item import (
    ItemCreate,
    ItemOut
)

from app.services.item_service import (
    create_item
)

router = APIRouter()


@router.post(
    "/",
    response_model=ItemOut
)
def create_new_item(
    data: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return create_item(
            db=db,
            seller_id=current_user.user_id,
            data=data
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
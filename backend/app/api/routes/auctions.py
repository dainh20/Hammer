from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.schemas.auction import (
    AuctionCreate,
    AuctionOut
)

from app.services.auction_service import (
    create_auction
)

from app.api.deps import (
    get_db,
    get_current_user
)

from app.models.user import User



router = APIRouter()


@router.post(
    "/",
    response_model=AuctionOut
)
def create_new_auction(
    data: AuctionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return create_auction(
            db=db,
            seller_id=current_user.user_id,
            data=data
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
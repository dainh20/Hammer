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

from app.schemas.bid import (
    BidCreate,
    BidOut
)

from app.services.bid_service import (
    place_bid
)

router = APIRouter()


@router.post(
    "/",
    response_model=BidOut
)
def create_bid(
    data: BidCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return place_bid(
            db=db,
            auction_id=data.auction_id,
            user_id=current_user.user_id,
            amount=data.bid_amount
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
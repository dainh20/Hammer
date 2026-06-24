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
from app.services.wallet_service import (
    deposit_money
)

router = APIRouter()


@router.post("/deposit")
def deposit(
    amount: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return deposit_money(
            db=db,
            user_id=current_user.user_id,
            amount=amount
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
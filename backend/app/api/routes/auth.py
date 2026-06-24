from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.api.deps import get_db

from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserOut
)

from app.services.auth_service import (
    register_user,
    login_user
)

from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserOut,
    Token
)

from app.services.auth_service import (
    register_user,
    login_and_create_token
)

router = APIRouter()


@router.post(
    "/register",
    response_model=UserOut
)
def register(
    data: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return register_user(
            db,
            data
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post(
    "/login",
    response_model=Token
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    try:
        return login_and_create_token(
            db,
            form_data.username,
            form_data.password
        )

    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
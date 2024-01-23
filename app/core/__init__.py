from typing_extensions import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session


from fastapi.param_functions import Depends

from .database import get_session
from .models import Base


# DatabaseSession = Annotated[AsyncSession, Depends(get_session)]
DatabaseSession = Annotated[Session, Depends(get_session)]

__all__ = (
    'Base',
    'DatabaseSession',
    'api_router',
)

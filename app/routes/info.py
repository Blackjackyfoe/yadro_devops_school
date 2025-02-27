from fastapi import APIRouter
from app.config import settings

router = APIRouter(prefix="/info")

@router.get("")
async def get_info():
    """
    Endpoint for retrieving basic app info.
    """

    version = settings.VERSION
    return {
        "version": version,
        "service": "currency",
        "author": "v.ivanychev"
    }
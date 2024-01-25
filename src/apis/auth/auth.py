from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
async def login(username: str, password: str):
    """
    Login to the system.
    Returns a token.
    """
    return {"token": "some_auth_token"}

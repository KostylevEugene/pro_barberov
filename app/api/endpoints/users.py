from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/check")
async def check():
    return {"msg": "Gello World"}

@router.post("/")
async def create_user():
    pass


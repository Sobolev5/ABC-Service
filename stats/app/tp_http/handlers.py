from fastapi import APIRouter
from fastapi import Depends
from fastapi import status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.tp_http import schema
from app.db.session import get_db
from app.src import views


router = APIRouter()


@router.get("/")
async def main():
    return {"stat server": 200}


@router.post("/health")
async def ping(schema: schema.HealthRQ) -> schema.DefaultRS:
    return {"message": "200 OK"}


@router.post("/user", response_model=schema.DefaultRS)
async def upsert_user(
        schema: schema.UserRQ, 
        db: AsyncSession = Depends(get_db)
    ) -> dict:

    user, error = await views.upsert_user(schema.dict(), db)
    if error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        )
    
    return {"message": f"User successfully upserted ID={user.id}"}
    




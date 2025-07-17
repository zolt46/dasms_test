from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import date

from models import Ammo
from database import get_db, Base, engine

app = FastAPI()

origins = ["*"]  # 실제 운영 시 도메인 제한 필요
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AmmoIn(BaseModel):
    type: str
    category: str
    quantity: int
    location: str
    condition: str
    supplied_at: date
    consumed_at: date | None = None
    supply_type: str
    reason: str
    notes: str

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/api/ammo", response_model=List[AmmoIn])
async def get_ammo(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Ammo))
    return result.scalars().all()

@app.post("/api/ammo")
async def add_ammo(item: AmmoIn, db: AsyncSession = Depends(get_db)):
    new_ammo = Ammo(**item.dict())
    db.add(new_ammo)
    await db.commit()
    return {"status": "ok"}

@app.post("/api/ammo/bulk")
async def bulk_add_ammo(items: List[AmmoIn], db: AsyncSession = Depends(get_db)):
    for item in items:
        db.add(Ammo(**item.dict()))
    await db.commit()
    return {"status": "bulk ok"}

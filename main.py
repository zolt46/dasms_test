from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import date

from .models import Ammo, Base
from .database import engine, SessionLocal
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]  # CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AmmoCreate(BaseModel):
    type: str
    category: str
    quantity: int
    location: str
    condition: str
    supplied_at: date | None = None
    consumed_at: date | None = None
    supply_type: str
    reason: str
    notes: str

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/api/ammo/bulk")
async def create_ammo_bulk(items: List[AmmoCreate], db: AsyncSession = Depends(get_db)):
    db.add_all([Ammo(**item.dict()) for item in items])
    await db.commit()
    return {"status": "ok"}

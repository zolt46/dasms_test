from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import async_session, engine, Base
from models import PersonFirearm, Ammo
from typing import List
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# 초기 테이블 생성
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# 의존성 주입
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

# Pydantic 모델
class PersonFirearmCreate(BaseModel):
    name: str
    rank: str
    service_number: str
    unit: str
    position: str
    firearm_type: str
    serial_number: str
    location: str
    status: str
    reason: str | None = None
    notes: str | None = None
    system_id: str
    system_pw: str
    access_level: str
    fingerprint: str

class AmmoCreate(BaseModel):
    type: str
    category: str
    quantity: int
    location: str
    condition: str
    supplied_at: datetime | None = None
    consumed_at: datetime | None = None
    supply_type: str
    reason: str | None = None
    notes: str | None = None

# API 라우터

@app.post("/api/firearm", status_code=201)
async def create_firearm(data: PersonFirearmCreate, session: AsyncSession = Depends(get_session)):
    new_entry = PersonFirearm(**data.dict())
    session.add(new_entry)
    await session.commit()
    return {"status": "created"}

@app.post("/api/ammo", status_code=201)
async def create_ammo(data: AmmoCreate, session: AsyncSession = Depends(get_session)):
    new_entry = Ammo(**data.dict())
    session.add(new_entry)
    await session.commit()
    return {"status": "created"}

@app.get("/api/ammo", response_model=List[AmmoCreate])
async def get_ammo(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Ammo))
    return result.scalars().all()

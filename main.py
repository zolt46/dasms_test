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

@app.get("/api/personnel")
async def get_personnel(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(PersonnelWeapon))
    people = result.scalars().all()
    return [
        {
            "name": p.name,
            "rank": p.rank,
            "serial_number": p.serial_number,
            "unit": p.unit,
            "position": p.position,
            "system_id": p.system_id,
            "system_password": p.system_password,
            "system_permission": p.system_permission
        }
        for p in people
    ]

@app.post("/api/personnel/bulk")
async def save_personnel(data: List[dict], session: AsyncSession = Depends(get_session)):
    for item in data:
        person = PersonnelWeapon(**item, weapon_type="K2", weapon_serial="TEMP", weapon_location="무기고A", weapon_condition="양호", fingerprint="placeholder")
        session.add(person)
    await session.commit()
    return {"status": "ok"}


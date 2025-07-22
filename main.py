# ✅ main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from pydantic import BaseModel

from database import get_async_session
from models import PersonnelWeapon, Ammo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Pydantic Schemas ===
class PersonnelInput(BaseModel):
    name: str
    rank: str
    serial_number: str
    unit: str
    position: str
    system_id: str
    system_password: str
    system_permission: str
    weapon_type: str = "기타"
    weapon_serial: str = "-"
    weapon_location: str = "기타"
    weapon_condition: str = "기타"
    weapon_reason: str | None = None
    weapon_note: str | None = None
    fingerprint: str = "default"

class AmmoInput(BaseModel):
    name: str
    category: str
    quantity: int
    location: str
    condition: str
    supply_type: str
    supplied_at: str | None = None
    consumed_at: str | None = None
    reason: str | None = None
    notes: str | None = None

# === API Routes ===

@app.get("/api/personnel", response_model=List[PersonnelInput])
async def get_personnel(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(PersonnelWeapon))
    return [row._mapping for row in result.fetchall()]

@app.post("/api/personnel/bulk")
async def save_personnel_bulk(data: List[PersonnelInput], session: AsyncSession = Depends(get_async_session)):
    for item in data:
        session.add(PersonnelWeapon(**item.dict()))
    await session.commit()
    return {"status": "ok"}

@app.get("/api/ammo", response_model=List[AmmoInput])
async def get_ammo(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Ammo))
    return [row._mapping for row in result.fetchall()]

@app.post("/api/ammo/bulk")
async def save_ammo_bulk(data: List[AmmoInput], session: AsyncSession = Depends(get_async_session)):
    for item in data:
        session.add(Ammo(**item.dict()))
    await session.commit()
    return {"status": "ok"}

@app.get("/api/firearm", response_model=List[PersonnelInput])
async def get_firearm(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(PersonnelWeapon))
    return [row._mapping for row in result.fetchall()]

@app.post("/api/firearm")
async def save_firearm(data: List[PersonnelInput], session: AsyncSession = Depends(get_async_session)):
    for item in data:
        session.add(PersonnelWeapon(**item.dict()))
    await session.commit()
    return {"status": "ok"}
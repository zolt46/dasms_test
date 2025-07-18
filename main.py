# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware
from database import get_async_session
from models import PersonnelWeapon
from sqlalchemy import select
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PersonnelInput(BaseModel):
    name: str
    rank: str
    serial_number: str
    unit: str
    position: str
    system_id: str
    system_password: str
    system_permission: str

@app.get("/api/person", response_model=List[PersonnelInput])
async def get_personnel(session: AsyncSession = Depends(get_async_session)):
    query = await session.execute(select(
        PersonnelWeapon.name,
        PersonnelWeapon.rank,
        PersonnelWeapon.serial_number,
        PersonnelWeapon.unit,
        PersonnelWeapon.position,
        PersonnelWeapon.system_id,
        PersonnelWeapon.system_password,
        PersonnelWeapon.system_permission
    ))
    rows = query.fetchall()
    return [dict(row._mapping) for row in rows]

@app.post("/api/person")
async def create_personnel(person: PersonnelInput, session: AsyncSession = Depends(get_async_session)):
    new_entry = PersonnelWeapon(
        name=person.name,
        rank=person.rank,
        serial_number=person.serial_number,
        unit=person.unit,
        position=person.position,
        system_id=person.system_id,
        system_password=person.system_password,
        system_permission=person.system_permission,
        # 나머지는 기본값 (빈 문자열) 처리
        weapon_type='기타',
        weapon_serial='-',
        weapon_location='기타',
        weapon_condition='기타',
        weapon_reason=None,
        weapon_note=None,
        fingerprint='default_fingerprint'  # 추후 별도로 업데이트 가능
    )
    session.add(new_entry)
    await session.commit()
    return {"status": "success"}
# models.py
from sqlalchemy import Column, Integer, String, Text, CheckConstraint, TIMESTAMP
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

class PersonnelWeapon(Base):
    __tablename__ = "personnel_weapon"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rank = Column(String, nullable=False)
    serial_number = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    position = Column(String, nullable=False)
    weapon_type = Column(String, nullable=False)
    weapon_serial = Column(String, nullable=False)
    weapon_location = Column(String, nullable=False)
    weapon_condition = Column(String, nullable=False)
    weapon_reason = Column(Text, nullable=True)
    weapon_note = Column(Text, nullable=True)
    system_id = Column(String, nullable=False)
    system_password = Column(String, nullable=False)
    system_permission = Column(String, nullable=False)
    fingerprint = Column(String, nullable=False)

class Ammo(Base):
    __tablename__ = "ammo"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    supply_type = Column(String, nullable=False)
    supplied_at = Column(TIMESTAMP, nullable=True)
    consumed_at = Column(TIMESTAMP, nullable=True)
    reason = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)

class AmmoCreate(BaseModel):
    name: str
    category: str
    quantity: int
    location: str
    condition: str
    supply_type: str
    supplied_at: Optional[str] = None
    consumed_at: Optional[str] = None
    reason: Optional[str] = None
    notes: Optional[str] = None

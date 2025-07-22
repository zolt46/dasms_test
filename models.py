# ✅ models.py
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PersonnelWeapon(Base):
    __tablename__ = "personnel_weapon"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    rank = Column(Text, nullable=False)
    serial_number = Column(Text, nullable=False)
    unit = Column(Text, nullable=False)
    position = Column(Text, nullable=False)
    weapon_type = Column(Text, nullable=False)
    weapon_serial = Column(Text, nullable=False)
    weapon_location = Column(Text, nullable=False)
    weapon_condition = Column(Text, nullable=False)
    weapon_reason = Column(Text, nullable=True)
    weapon_note = Column(Text, nullable=True)
    system_id = Column(Text, nullable=False)
    system_password = Column(Text, nullable=False)
    system_permission = Column(Text, nullable=False)
    fingerprint = Column(Text, nullable=False)

class Ammo(Base):
    __tablename__ = "ammo"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    category = Column(Text, nullable=False)
    quantity = Column(Integer, nullable=False)
    location = Column(Text, nullable=False)
    condition = Column(Text, nullable=False)
    supply_type = Column(Text, nullable=False)
    supplied_at = Column(Text, nullable=True)
    consumed_at = Column(Text, nullable=True)
    reason = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)

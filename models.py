from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base

class PersonFirearm(Base):
    __tablename__ = 'person_firearm'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    rank = Column(String, nullable=False)
    service_number = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    position = Column(String, nullable=False)
    firearm_type = Column(String, nullable=False)
    serial_number = Column(String, nullable=False)
    location = Column(String, nullable=False)
    status = Column(String, nullable=False)
    reason = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    system_id = Column(String, nullable=False)
    system_pw = Column(String, nullable=False)
    access_level = Column(String, nullable=False)
    fingerprint = Column(String, nullable=False)

class Ammo(Base):
    __tablename__ = 'ammo'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    supplied_at = Column(DateTime, nullable=True)
    consumed_at = Column(DateTime, nullable=True)
    supply_type = Column(String, nullable=False)
    reason = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)

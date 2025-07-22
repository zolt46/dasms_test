from sqlalchemy import Column, Integer, String, Text, CheckConstraint, TIMESTAMP
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

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

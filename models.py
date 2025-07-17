from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Ammo(Base):
    __tablename__ = "ammo"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    location = Column(String)
    condition = Column(String)
    supplied_at = Column(Date, nullable=True)
    consumed_at = Column(Date, nullable=True)
    supply_type = Column(String)
    reason = Column(String)
    notes = Column(String)

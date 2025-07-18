from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PersonnelWeapon(Base):
    __tablename__ = "personnel_weapon"  # 이미 존재하는 테이블명
    __table_args__ = {'extend_existing': True}  # 중요: 기존 테이블에 연결

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

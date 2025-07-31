from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from database import Base


class Employee(Base):
    """
    用户表
    """

    __tablename__ = 'employee'

    id = Column('id',Integer, primary_key=True, autoincrement=True, comment='主键')
    create_time = Column('created_at', DateTime, nullable=True, default='', comment='创建时间')
    personID = Column('personID',String(100), nullable=True, default='', comment='人员标识码')
    name = Column('personNAME', String(100), nullable=True, default='', comment='姓名')
    status = Column('personSTATUS', String(1), nullable=True, default='N', comment='人员状态')
    ou = Column('personOU', String(64), nullable=True, default='', comment='所属组织')
    
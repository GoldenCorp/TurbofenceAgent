from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Literal, Optional
class EmployeeModel(BaseModel):
    """
    员工表对应pydantic模型
    """
    
    id: Optional[int] = Field(default=None, description='主键')
    create_time: Optional[datetime] = Field(default=None, description='创建时间')
    personID: Optional[str] = Field(default=None, description='人员标识码')
    name: Optional[str] = Field(default=None, description='姓名')
    status: Optional[str] = Field(default=None, description='人员状态')
    ou: Optional[str] = Field(default=None, description='所属组织')
    class Config:
        orm_mode = True
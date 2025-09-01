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
        from_attributes = True
        
    
class enen(BaseModel):
    """
    员工请求参数对应pydantic模型
    """
    name: Optional[str] = Field(default=None, description='enen的姓名')
    class Config:
        from_attributes = True

class EmployeeQueryInputModel(BaseModel):
    """
    员工请求参数对应pydantic模型
    """
    name: Optional[str] = Field(default=None, description='员工的姓名')
    class Config:
        from_attributes = True
        
class ChuchaiInputModel(BaseModel):
    """
    员工请求参数对应pydantic模型
    """
    name: Optional[str] = Field(default='李仕佳', description='出差员工的姓名')
    dest: Optional[str] = Field(default='天津', description='出差的目的地城市')
    days: Optional[int] = Field(default=11, description='出差的天数')
    reason: Optional[str] = Field(default='出差啊', description='出差的目的原因')
    class Config:
        from_attributes = True
        
class BaojiaInputModel(BaseModel):
    """
    周界安防报价的请求参数对应pydantic模型
    """
    totalCamera: Optional[int] = Field(default=0, description='摄像头个数')
    totalCameraPole: Optional[int] = Field(default=0, description='摄像杆数')
    totalFCLength: Optional[float] = Field(default=0.0, description='总光缆长度')
    totalLength: Optional[float] = Field(default=0.0, description='电源线总长度')
    class Config:
        from_attributes = True
        
class BaojiaStrnputModel(BaseModel):
    """
    周界安防报价的请求参数对应pydantic模型
    """
    totalCamera: Optional[str] = Field(default=0, description='摄像头个数')
    totalCameraPole: Optional[str] = Field(default=0, description='摄像杆数')
    totalLength: Optional[str] = Field(default=0.0, description='电源线总长度')
    class Config:
        from_attributes = True
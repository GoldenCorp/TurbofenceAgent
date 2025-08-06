from fastapi import APIRouter, Depends, File, Form, Query, Request, UploadFile
from fastapi.exceptions import HTTPException
from vos import (
    EmployeeModel,
    EmployeeQueryInputModel
)

from dos import (
    Employee
)
from database import db
# from http_exception import HTTPException
userRouter = APIRouter(prefix='/user')

@userRouter.post("/employee", response_model=EmployeeModel, operation_id="user2", summary="这个工具可以检查这个用户是否是我组织内合法用户")
def user(user: EmployeeQueryInputModel):
    theUser = db.query(Employee).filter(Employee.name == user.name).first()
    if theUser is None:
        raise HTTPException(status_code=404, detail="用户不存在")

    return theUser
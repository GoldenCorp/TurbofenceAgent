from fastapi import APIRouter, Depends, File, Form, Query, Request, UploadFile
from vos import (
    EmployeeModel,
)

from dos import (
    Employee
)
from database import db
# from http_exception import HTTPException
userRouter = APIRouter(prefix='/user')

@userRouter.get("/employee", response_model=EmployeeModel, operation_id="user", summary="这个工具可以检查这个用户是否是我组织内合法用户")
def user(userName: str):
    theUser = db.query(Employee).filter(Employee.name == userName).first()
    if theUser is None:
        print("用户不存在")

    return theUser

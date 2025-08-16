from fastapi import APIRouter, Depends, File, Form, Query, Request, UploadFile
from vos import (
    ChuchaiInputModel
)
import httpx
from fastapi.security import HTTPBearer

# Scheme for the Authorization header
token_auth_scheme = HTTPBearer()
# from http_exception import HTTPException
oaRouter = APIRouter(prefix='/oa')

@oaRouter.post("/chuchai", operation_id="chuchai", summary="这个工具可以根据参数发起oa出差流程")
# def chuchai():
def chuchai(chuchaiParam:ChuchaiInputModel,token=Depends(token_auth_scheme)):
    # with httpx.Client() as client:
    #     response = client.get("https://www.baidu.com")
    #     return response.text
    
    data = {
        "app_id": "688def4a8ec4c27266c1c038",
        "entry_id": "688def56379921af1bfa3d1b",
        "data": {
            "_widget_1754132314714": {
            "data": chuchaiParam.name,
            # "data": '李仕佳',
            "visible": True
            },
            "_widget_1754132314715": {
            "data": chuchaiParam.dest,
            # "data": '天津',
            "visible": True
            },
            "_widget_1754132314716": {
            "data": chuchaiParam.days,
            # "data": '11',
            "visible": True
            },
            "_widget_1754132314717": {
            "data": chuchaiParam.reason,
            # "data": '李仕佳',
            "visible": True
            }
        },
        "data_creator": "R-72frEzKd",
        "is_start_workflow": True
    }
    headers = {
        "Authorization": "Bearer Lc2zHmdtk2rglJeNXYDLlhBzlwPtVvO7"

    }
    r = httpx.post("https://api.jiandaoyun.com/api/v5/app/entry/data/create", json=data, headers=headers)
    return r.json()


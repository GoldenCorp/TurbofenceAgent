from fastapi import APIRouter, Depends, File, Form, Query, Request, UploadFile

import httpx
# from http_exception import HTTPException
oaRouter = APIRouter(prefix='/oa')

@oaRouter.get("/chuchai", operation_id="chuchai", summary="这个工具可以根据参数发起oa出差流程")
def chuchai():
    with httpx.Client() as client:
        response = client.get("https://www.baidu.com")
        return response.text


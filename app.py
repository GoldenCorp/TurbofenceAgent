from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from userRouter import userRouter
from oaRouter import oaRouter
app = FastAPI(
    title='giit',
    description='接口文档',
    version='0.0.1'
)

app.include_router(router=userRouter, tags='用户')
app.include_router(router=oaRouter, tags='oa')
mcp = FastApiMCP(app, name="giit", description="测试")
mcp.mount()

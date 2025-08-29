from fastapi import FastAPI,Depends
from fastapi_mcp import FastApiMCP, AuthConfig
from userRouter import userRouter
from oaRouter import oaRouter
from baojiaRouter import baojiaRouter
from starlette.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.security import HTTPBearer
# Scheme for the Authorization header
token_auth_scheme = HTTPBearer()
app = FastAPI(
    title='giit',
    description='接口文档',
    version='0.0.1',
    docs_url=None
)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Custom Swagger UI",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css"
    )

app.include_router(router=userRouter, tags=['用户'])
app.include_router(router=oaRouter, tags=['oa'])
app.include_router(router=baojiaRouter, tags=['报价'])
mcp = FastApiMCP(app, name="giit", description="测试",
    auth_config=AuthConfig(
        dependencies=[Depends(token_auth_scheme)],
    )
)
mcp.mount()

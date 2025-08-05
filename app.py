from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from userRouter import userRouter
from oaRouter import oaRouter
from starlette.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
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
mcp = FastApiMCP(app, name="giit", description="测试")
mcp.mount()

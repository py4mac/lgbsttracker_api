from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import uvicorn
from lgbsttracker_api.api.api_v1.api import api_router

app = FastAPI(
    title="Working Time",
    openapi_url="/api/v1/openapi.json",
    redoc_url="/api/v1/doc",
    docs_url=None)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Working Time",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    # Bug: https://github.com/Redocly/redoc/issues/926
    openapi_schema["servers"] = [{"url": "http://127.0.0.1:8000"}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
app.include_router(api_router, prefix='/api/v1')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
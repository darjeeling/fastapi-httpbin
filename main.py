from fastapi import FastAPI, Request
from typing import Any

app = FastAPI(
    title="FastAPI httpbin",
    description="A simple httpbin-like HTTP testing service",
    version="0.1.0",
)


@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "FastAPI httpbin - A simple HTTP testing service",
        "endpoints": {
            "GET /get": "Returns GET request data",
            "POST /post": "Returns POST request data",
            "GET /headers": "Returns request headers",
            "GET /ip": "Returns client IP address",
            "GET /user-agent": "Returns User-Agent header",
        },
    }


@app.get("/get")
async def get_request(request: Request):
    """Returns GET request data"""
    return {
        "args": dict(request.query_params),
        "headers": dict(request.headers),
        "origin": request.client.host if request.client else None,
        "url": str(request.url),
    }


@app.post("/post")
async def post_request(request: Request):
    """Returns POST request data"""
    try:
        json_data = await request.json()
    except Exception:
        json_data = None

    form_data = {}
    try:
        form = await request.form()
        form_data = dict(form)
    except Exception:
        pass

    return {
        "args": dict(request.query_params),
        "data": await request.body() if not json_data else None,
        "form": form_data if form_data else None,
        "json": json_data,
        "headers": dict(request.headers),
        "origin": request.client.host if request.client else None,
        "url": str(request.url),
    }


@app.get("/headers")
async def get_headers(request: Request):
    """Returns request headers"""
    return {"headers": dict(request.headers)}


@app.get("/ip")
async def get_ip(request: Request):
    """Returns client IP address"""
    return {"origin": request.client.host if request.client else None}


@app.get("/user-agent")
async def get_user_agent(request: Request):
    """Returns User-Agent header"""
    return {"user-agent": request.headers.get("user-agent", "")}

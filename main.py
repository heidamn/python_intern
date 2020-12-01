from fastapi import FastAPI
from app import is_alive_host
app = FastAPI()


@app.get("/healthz")
async def get_is_alive_host(hostname):
    return {"status": "up" if is_alive_host else "down"}
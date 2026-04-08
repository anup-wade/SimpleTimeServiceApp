from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

@app.get("/")
async def get_time(request: Request):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.client.host
    }

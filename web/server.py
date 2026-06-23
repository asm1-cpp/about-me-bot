import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="web/templates")

log_queues = {
    "DEBUG": asyncio.Queue(),
    "INFO": asyncio.Queue(),
    "ERROR": asyncio.Queue()
}

async def log_generator(level_filter: str):
    queue = log_queues[level_filter]
    while True:
        message = await queue.get()
        yield f"data: {message}\n\n"

@app.get("/", response_class=HTMLResponse)
async def get_index_page(request: Request):
    return templates.TemplateResponse(request, "INDEX.html")

@app.get("/stream/debug")
async def stream_debug():
    return StreamingResponse(log_generator("DEBUG"), media_type="text/event-stream")

@app.get("/stream/info")
async def stream_info():
    return StreamingResponse(log_generator("INFO"), media_type="text/event-stream")

@app.get("/stream/error")
async def stream_error():
    return StreamingResponse(log_generator("ERROR"), media_type="text/event-stream")

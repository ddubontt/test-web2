from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/api")
def api_status():
    return {"estado": "Zero Config Web activado", "magia": True}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8085)

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from whereistheaccent.api.api import router as api_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="web/static"), name="static")

templates = Jinja2Templates(directory="web/templates")


@app.get("/", response_class=HTMLResponse)
def hello_world(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.include_router(api_router, prefix="/v1")

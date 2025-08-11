from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/multi_block")
def multi_block(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
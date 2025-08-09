from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/include")
def include_example(request: Request):
    return templates.TemplateResponse("include_example.html", {"request": request})
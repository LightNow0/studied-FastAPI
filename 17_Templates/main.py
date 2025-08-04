from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="template")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "username": "John"})

## username을 요청에서 받기
# HTTP 요청에서 username을 받아 템플릿에 전달하는 예제
# 1. 경로 매개변수 사용예제
@app.get("/user/{username}")
def get_user(request: Request, username: str):
    return templates.TemplateResponse("index.html", {"request": request, "username": username})

# 2. 쿼리 매개변수 사용예제
@app.get("/user")
def get_users(request: Request, username: str = "Kim"):
    return templates.TemplateResponse("index.html", {"request": request, "username": username})
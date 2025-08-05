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

# FastAPI와 Jinja2의 기본 문법
@app.get("/safe")
def read_root_safe(request: Request):
    my_variabl_with_html = "<h1>Hello, FastAPI!</h1>"
    return templates.TemplateResponse("index_with_safe.html", {"request": request, "my_variabl_with_html": my_variabl_with_html})


# 조건문
@app.get("/greet")
def greeting(request: Request, time_of_day: str):
    return templates.TemplateResponse("index.html", {"request": request, "time_of_day": time_of_day})

# 반복문
@app.get("/items")
def read_items(request: Request):
    my_items = ["apple", "banana", "cherry"]
    return templates.TemplateResponse("index.html", {"request": request, "items": my_items})

## 리스트를 직접 요청을 받아 출력 -> 데이터는 ,기준으로 내부에서 리스트로 만듭니다.
@app.get("/dynamic_items/")
def dynamic_items(request: Request, item_list: str = ""):
    items = item_list.split(",")
    return templates.TemplateResponse("index.html", {"request": request, "items": items})

## macro
@app.get("/macro")
def read_macro(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "John"})


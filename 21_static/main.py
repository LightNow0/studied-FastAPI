from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


# 정적 파일을 위한 설정
app.mount("/static", StaticFiles(directory='static'), name="static")

templates = Jinja2Templates(directory="templates")

# 메인페이지 라우트ㅡ
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
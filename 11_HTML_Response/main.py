from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# HTMLResponse를 response_class로 사용하여 경로 연산을 정의합니다.
# 이 경로 연산은 HTML형식의 응답을 반환합니다.
@app.get("/html", response_class=HTMLResponse)
def read_html():
    # HTML 형식의 문자열을 반환합니다.
    # FastAPI는 이를 HTMLResponse 객체로 반환하여 응답합니다.
    return "<h1>This is HTML</h1>"
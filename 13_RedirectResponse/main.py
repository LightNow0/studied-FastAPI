from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse

app = FastAPI()

# RedirectResponse를 사용하여 경로 연산을 정의합니다.
#  클라이언트를 '/text'경로로 리디렉션합니다.
@app.get("/redirect")
def read_redirect():
    return RedirectResponse(url="text")


# '/text' 경로는 RedirectResponse를 반환하는 간단한 연산입니다.
@app.get("/text", response_class=PlainTextResponse)
def read_text():
    return "This is PlainTextResponse"


# curl -X GET "http://127.0.0.1:8000/text" -L
# -L -> 리디렉션을 따르도록 지시하는 옵션입니다.
# /redirect로 요청이 들어오면 '/text'로 리디렉션합니다.
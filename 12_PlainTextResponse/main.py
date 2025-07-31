from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

# PlainTextResponse를 response_class로 사용하여 경로를 연산을 정의합니다.
# 이 경로 연산은 텍스트 형식의 응답을 반환합니다.
@app.get("/text", response_class=PlainTextResponse)
def read_text():
    # 단순 텍스트 문자열을 반환합니다.
    # FastAPI는 이를 PlainTextResponse객체로 반환하여 응답합니다.
    return "This is Plain Text"




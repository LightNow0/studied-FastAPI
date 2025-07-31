from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# JSONResponse를 response_class로 사용하여 경로 연산을 정의합니다.
# 이 경로 연산은 JSON 형식의 응답을 반환합니다.
@app.get("/json", response_class=JSONResponse)
def read_json():
    # 딕셔너리를 반환합니다. FastAPI는 이름 JSONResponse 객체로 반환하여 응답합니다.
    return {"msg": "This is JSON"}
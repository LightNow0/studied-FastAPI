# fastapi -> import
from fastapi import FastAPI, Query
from typing import List, Dict

# fastapi 인스턴스생성
app = FastAPI()


# HTTP GET 요청을 "/"경로로 받을 준비
@app.get("/")
# 해당 요청을 처리할 함수 정의
def read_root():
    return {"message": "Hello, World!"}     # JSON 형태의 응답을 반환


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# @app.get("/items/")
# def read_items(skip = 0, limit = 10):
#     return {"skip": skip, "limit": limit}


@app.get("/items/")
def read_items(q: list[int] = Query([])):       # 빈 리스트를 기본값으로 설정
    return {"q":q}

@app.post("/create-item/")
def create_item(item: Dict[str, int]):
    return item

# @app.get("/getdata/")
# def read_items(data: str = "funcoding"):     # data의 기본값은 funcoding:
#     return {"data": data}
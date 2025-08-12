from fastapi import FastAPI

app = FastAPI()

# "/items/" 경로에 대한 GET 요청을 처리하는 함수입니다.
# 'skip'과 'limit'이라는 2개의 쿼리 매개변수를 받습니다.
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    # 함수가 호출될 때 FastAPI는 'skip'과 'limit' 매개변수에 대한 값을
    # 요청 URL에서 추출하여 전달합니다.
    return {"skip": skip, "limit": limit}

@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}
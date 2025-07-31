from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic model을 정의합니다
# 이 모델은 응답 데이터의 구조를 나타냅니다.
class Item(BaseModel):
    name: str
    price: float

# FastAPI 경로 연산을 정의합니다
# 이 연산은 GET요청을 처리하고 response_model을 Item으로 지정하여 반환할 데이터의 구조를 정의합니다.
@app.get("/item/", response_model=Item)
def get_item():
    # 데이터베이스나 다른 데이ㅓ터 소스에서 아이템을 가져와 반환합니다.
    # 여기서는 예시를 위해 고정된 값을 반환합니다.
    return {"name": "milk", "price": 3.5}
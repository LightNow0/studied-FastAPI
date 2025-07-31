from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic 모델을 정의합니다.
# 해당 모델은 응답 데이터의 각 항목의 구조를 나타냅니다.
class Item(BaseModel):
    name: str

# 경로연산을 정의합니다.
# response_model은 List[Item]으로 지정되어있습니다
# 이는 반환되는 응답이 Item 인스턴스들의 리트임을 명시합니다.
@app.get("/items/", response_model=List[Item])
async def get_item():
    # 데이터베이스나 다른 데이터 소스에서 아이템 리스트를 가져와 반환합니다.
    # 여기서는 예시를 위해 고정된 리스트를 반환합니다.
    return [{"name": "Item 1"}, {"name": "Item 2"}]
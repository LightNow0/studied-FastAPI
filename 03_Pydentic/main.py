from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
    # name은 최소 2자 최대 50자를 가져야하며 필수 필드입니다.
    name: str = Field(..., title="Item Name", min_length=2, max_length=50)
    # description은 선택 필드이며 최대 300자까지 가능합니다.
    description: str = Field(None, description="The description of the item", max_length=300)
    # price는 0보다 커야하며 필수 필드입니다
    price: float = Field(..., gt=0, description="The price must be greater then zero")
    # tag필드는 선택적이며 기본값으로 빈 리스트를 갖습니다. JSON에서는 item-tags로 나타납니다
    tag: List[str] = Field(default=[], alias="item-tags")

@app.post("/items/")
async def create_item(item: Item):
    # 아이템 생성을 위한 엔드포인트로 모델 인스턴스의 딕셔너리 표현을 반환합니다.
    return {"item": item.dict()}
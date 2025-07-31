from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 각각의 동물을 나타내는 Pydantic 모델을 정의합니다.
class Cat(BaseModel):
    name: str

class Dog(BaseModel):
    name: str


# 경로연산을 정의합니다. 여기서 response_model은 Union{Cat, Dog}로 지정되어 있습니다.
# 이는 반환되는 응답이 Cat 혹은 Dog 모델중 하나의 형태를 띠게 됩니다.
@app.get("/animal/", response_model=Union[Cat, Dog])
async def get_animal(animal: str):
    # 쿼리 매개변수로 "animal"을 받아서 그에 맞는 동물 데이터를 반환합니다.
    if animal == "cat":
        return Cat(name="Whiskers")
    else:
        return Dog(name="Fido")
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union, TypeVar, Generic

app = FastAPI()

class Item(BaseModel):
    name: str
    tags: List[str]
    variant: Union[int, str]

@app.post("/items/")
def create_item(item: Item):
    return {"item": item.dict()}

## 제네릭 타입
# 제네릭 타입은 일종의 '타입 템플릿'이며 여러 다른 타입에 대한 동일한 로직을 적용할 수 있습니다.

# FastAPI와 Pydantic에서 제네릭 타입을 ,사용하려면 typing 모듈의 Generic class를 이용합니다.

# TypeVar: TypeVar는 타입 변수를 생성하며 제네릭 클래스나 함수가 사용할 수 있는 타입 매개변수를 정의합니다.
#           정적타입 검사 도구가 타입 정보를 이해하고 검사할 수 있게 만드는 역할을 합니다.
# Generic[T]: T를 타입 매개변수로 가지는 제네릭 클래스를 정의할 때 사용합니다. 이 구문에서 왼쪽과 오른쪽 위치에 따라 T의 역할은 서로 다릅니다.

# 왼쪽의 [T]:  타입 변수의 이름으로 코드 내에서 타입 힌트로 사용됩니다.
# 예) Generic[T], List[T] -> 실제 코드에서 제네릭 타입으로 사용될 때 참조하는 이름입니다.

# 오른쪽의 [T]: 이것은 TypeVar 함수에 전달되는 문자열 리터럴로 TypeVar 객체를 생성할 때 내부적으로 사용되는 식별자입니다.




# TypeVar와 GenericType의 예시 코드

# 타입 변수  T를 선언합니다. 이것은 커스텀 제네릭 타입을 만들기 위한 첫 단계입니다.
# 여기서 'T'는 임의의 타입을 나타내는 타입 변수입니다.
T = TypeVar('T')

# Generic[T]를 상속받는 클래스를 정의함으로써 GenericItem은 어떤 타입 T도 받을 수 있는 제네릭  클래스가 됩니다.
# 이 클래스는 이름과 내용의 필드를 가지며 content의 타입은 동적으로 결정됩니다.
class GenericItem(BaseModel, Generic[T]):
    name: str   # 아이템의 이름 필드이며 문자열 타입입니다.
    content: T  # 아이템의 내용 피드이며 T 타입입니다.


# Pydentic에서의 GenericType의 예시 코드

app = FastAPI()

# T는 제네릭 타입에서 사용될 타입변수입니다.
T = TypeVar('T')

# GenericItem 클래스는 제네릭 타입 T를 사용하는 모델입니다.
# 이 모델은 다양한 타입의 content 필드를 가질 수 있습니다.
class GenericItem(BaseModel, Generic[T]):
    name: str
    content: T
    
# 이 엔드포인트는 정수 타입의 content를 가진 GenericItem 객체를 생성합니다
@app.post("/generic_items/")
def create_item(item: GenericItem[int]):
    return {"item": item.dict()}
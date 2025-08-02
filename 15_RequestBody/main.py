## 사용자가 특정 항목의 ID로 정보를 요청하는 GET 요청을 하는 경우 항목의 ID는 쿼리 매개변수나 URL경로의 일부로 전송되는 코드

from fastapi import FastAPI, Query, Body

app = FastAPI()

@app.get("/items/")
def read_item(item_id: int = Query(...)):
    # item_id는 Query 매개변수를 통해 전달됩니다.
    return {"item_id": item_id}


# POST메소드로 '/items/'경로에 데이터를 전송하는 경로 연산을 정의합니다.
@app.post("/items/")
def create_items(item: dict = Body(...)):   # 필드가 필수가 아닌경우 ...이 아닌 None으로 값을 설정을 해줘야합니다.
    # 클라이언트가 전송하는 JSON 바디 데이터를 'item'이라는 변수로 받습니다.
    # 'dict' 타입은 JSON바디가 Python 딕셔너리로 파싱될 것임을 나타냅니다.
    # Body(...)는 이 필드가 클라이언트로부터 필수로 제공되어야 함을 나타냅니다.
    return {"item": item}


# 요청바디의 다양한 옵션
# Body()함수를 사용하여 요청바디를 정의할 때 추가적인 옵션을 제공하여 API의 요구사항을 더욱 세밀하게 조정할 수 있습니다.
# 이 옵션들로 개발자는 클라이언트로부터 받은 데이터를 더욱 정밀하게 제어하고 API문서화를 통해 사용자에게 유용항 정보를 제공할 수 있습니다.

@app.post("/advanced_items/")
def create_advanced_item(
    item: dict = Body(
        default=None,   # 필수가 아닌 필드 기본값 설정
        example={"key": "value"},   # 문서에 표시될 예시 값
        media_type="application/json",  # 미디어 타입 명시
        alias="item_alias",     # 별칭 설정(실제 사용자x)
        title="Sample Item",    # 문서 제목
        description="This is a sample item",    # 상세 설명
        deprecated=False,       # 사용중단 여부
    )
):
    
    return {"item": item}
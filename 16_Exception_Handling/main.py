from fastapi import FastAPI, HTTPException

app = FastAPI()


# # '/items/' 경로에 대한 GET 요청을 처리하는 경로 연산을 정의합니다.
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     # 예외가 발생할 가능성이 있는 코드를 try 블록안에 작성합니다.
#     try:
#         # item_id가 음수인 경우 ValueError를 발생합니다.
#         if  item_id < 0:
#             raise ValueError("음수는 허용되지 않습니다.")
    
#     except ValueError as e:
#         # 발생한 ValueError를 HTTPException으로 변환하여 처리합니다.
#         # 클라이언트에게 상태코드 400과 에러메시지를 반환합니다
#         raise HTTPException(status_code=400, detail=str(e))


# HTTPException 클래스
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id == 42:
        raise HTTPException (status_code=404, detail="Item Not Found")
    return {"item_id": item_id}

# HTTP Headers

## WWW-Authenticate Header
raise HTTPException(
    status_code=401,
    detail="Not authenticated",
    headers={"WWW-Authenticate": "Bearer"}
)
# 클라이언트에게 어떤 인증 방식을 사용해야하는지 알려줍니다. 주로 401Unauthorized 응답과 함께 사용됩니다.

## Retry_After Header
raise HTTPException(
    status_code=429,
    detail="Too  many Requests",
    headers={"Retry-After": "120"}
)
# 클라이언트가 서비스에 대한 요청을 너무 많이 보냈을 때 일정 시간 후에 다시 시도하라는 지시를 전달합니다.

## X-Rate-Limit Header
raise HTTPException(
    status_code=429,
    detail="Rate limit exceeded",
    headers={"X-Retry-Limit": 100}
)
# 사용자가 한정된 시간 내에 요청할 수 있는 최대 횟수를 알려줍니다.

## X-Error Header
raise HTTPException(
    status_code=500,
    detail="Internal Server Error",
    headers={"X-Error": "Database connection failed"}
)
# 내부 서버 에러 발생시 에러의 세부 사항을 클라이언트에게 전달합니다.

## Cache-Control Header
raise HTTPException(
    status_code=200,
    detail="Response Information",
    headers={"Cache-Control": "no-cache"}
)
# 클라이언트에게 해당 응답을 ,캐시하지 말라는 지시를 합니다. 데이터가 실시간으로 갱신되어야 할 때 유용합니다.

## Location Header
raise HTTPException(
    status_code=201,
    detail="New item created",
    headers={"Location": "/items/5"}
)
# 새로 생성된 리소스의 URI를 클라이언트에게 제공합니다. 주로 201 Created 응답에서 사용됩니다.

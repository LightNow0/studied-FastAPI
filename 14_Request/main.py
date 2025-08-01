from fastapi import FastAPI, Query

app = FastAPI()


## Query Parameter

#'/users/' 경로에 대한 GET 요청을 처리하는 경로 연산을 정의합니다.
#이 경로 연산은 쿼리 매개변수 'q'를 받아들입니다.
# @app.get("/users/")
# def read_users(q: str = Query(None, max_length=50)):
#     return {"q": q}

# ----------------------------------------------------------------------------------------------------------------------------------------------

## alias

# '/items/' 경로 연산을 정의합니다.
# 'internal_query' 매개변수는 외부에서는 'search'라는 이름의 쿼리 매개변수로 접근합니다.
@app.get("/items/")
def read_items(internal_query: str = Query(None, alias="search")):
    # 클라이언트는 'search'라는 이름으로 쿼리매개변수를 전송합니다.
    # FastAPI 애플리케이션은 이를 'internal_query'라는 내부 변수로 처리합니다.
    return {"query_handled": internal_query}



# ----------------------------------------------------------------------------------------------------------------------------------------------

## deprecated

@app.get("/users/")
def read_users(q: str = Query(None, deprecated=True)):
    return {"q": q}


# ----------------------------------------------------------------------------------------------------------------------------------------------


## description

# '/info/'경로 연산을 정의합니다.
# '/info/' 매개변수에 대한 설명을 Query의 description 옵션을 통해 추가합니다.
@app.get("/info/")
def read_info(info: str = Query(None, description="정보를 입력해주세요")):
    # 클라이언트는 'info'라는 이름으로 쿼리 매개변수를 전송할 수 있고 이 매개변수에 대한 설명은 Swagger UI에서 확인할 수 있습니다.
    return{"info": info}
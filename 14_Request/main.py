from fastapi import FastAPI, Query

app = FastAPI()


## Query Parameter

#'/users/' 경로에 대한 GET 요청을 처리하는 경로 연산을 정의합니다.
#이 경로 연산은 쿼리 매개변수 'q'를 받아들입니다.
@app.get("/users/")
def read_users(q: str = Query(None, max_length=50)):
    return {"q": q}


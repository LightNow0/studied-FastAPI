from fastapi import FastAPI, APIRouter
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

# TrustedHostMiddleware 미들웨어를 추가합니다.
# 이 미들웨어는 들어오는 모든 요청의 호스트가 allowed_hosts에 지정된 호스트중 하나인지
# 검사합니다.
# 만약 요청이 허용되지 않은 호스트에서 온 것이라면 400 Bad Request 응답을 반환합니다. 
# 이는 서비스가 지정된 호스트(도메인)에서만 접근 가능하도록 보안을 강화하는데 도움을 줍니다.
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["example.com", "localhost", "127.0.0.1"]
)

router = APIRouter()

# APIRouter를 사용한 라우트
@router.get("/items/")
def read_items_from_router():
    return {"message": "You are accessing the API from an allowed host via router."}

# 메인 애플리케이션에 APIRouter를 포함합니다.
app.include_router(router, prefix="/api/v1")

# 일반 애플리케이션 라우트
@app.get("/hello/")
def read_hello():
    return {"message": "Hello, World!"}
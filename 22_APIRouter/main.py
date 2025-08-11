from fastapi import FastAPI, APIRouter

app = FastAPI()

# APIRouter 객체생성
router = APIRouter()

# router에 라우트 추가
@router.get("/items/")
def read_items():
    return {"Hello": "World"}

# FastAPI 애플리케이션에 router 포함
app.include_router(router)
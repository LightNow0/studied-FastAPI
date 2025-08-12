from fastapi import FastAPI, Depends, APIRouter, HTTPException

app = FastAPI()

def common_dependency():
    return "This is a common dependency."

# 상위 라우터
parent_router = APIRouter(
    prefix="/parent",
    tags=["parent"],
    dependencies=[Depends(common_dependency)]
)

@parent_router.get("/item/")
def read_parent_item():
    return {"message": "This is an item from the parent router."}

# 하위 라우터
child_router = APIRouter()

@child_router.get("/item")
def read_child_item(common: str = Depends(common_dependency)):
    return {
        "message": "This is an item from the mchild router",
        "common": common
        }

# 하위 라우터를 상위 라우터에 추가 (상속)
parent_router.include_router(
    child_router,
    prefix="/child",
    )

# 상위 라우터를 애플리케이션에 추가
app.include_router(parent_router)
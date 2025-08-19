from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

# 데이터를 스트리밍하는 제너레이터 함수
def data_generator():
    for i in range(100):
        yield f"data chunk {i}\n"

# FastAPI 경로 연산에 StreamingResponse 반환
@app.get("/stream")
def stream_data():
    generator = data_generator()    # 데이터 생성을 위한 제너레이터 함수 호출
    return StreamingResponse(generator, media_type="text/plain")


"""
data_generator() 함수는 100개의 데이터 청크를 순차적으로 생성하고 각 청크는 yield를 통해 반환됩니다.
stream_data() 함수에서 이 제너레이터를 StreamingResponse의 인자로 전달하며 반환될 데이터의 타입이
일반 텍스트이므로 media_type="text/plain"으로 지정합니다.

"""
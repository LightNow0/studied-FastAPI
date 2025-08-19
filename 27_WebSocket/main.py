from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # 클라이언트 연결 수락
    try:
        while True:
            # 클라이언트에서 메시지 받기
            data = await websocket.receive_text()
            # 받은 메시지를 다시 클라이언트로 전송
            await websocket.send_text(f"Returned Message: {data} From Server")
    except WebSocketDisconnect:
        print("WebSocket disconnected")
        # 명시적으로 웹소켓 연결 종료
        await websocket.close(code=1000)

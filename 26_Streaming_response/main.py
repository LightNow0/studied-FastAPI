from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import csv
import io

app = FastAPI()

def csv_streamer():
    data = [["name", "age"], ["alice", 32], ["bob, 29"]]
    output = io.StringIO()
    writer = csv.writer(output)
    for row in data:
        writer.writerow(row)
        yield output.getvalue() # 여기서 StreamingResponse 를 사용하면 중간 결과를  응답해줄 수 있습니다.
        output.flush()
        output.truncate(0)
        output.seek(0)

@app.get("/csv")
def get_csv():
    return StreamingResponse(
        csv_streamer(),
        headers={"Content-Type": "text/csv"},
    )

"""
csv_streamer() 함수는 CSV 데이터를 yield로 하나씩 전송합니다
StreamingResponse를 사용하여 이 데이터가 조각으로 나위어 클라이언트에게 전달됩니다.

csv_streamer() 함수는 CSV 데이터를 생성하고 이를 스트리밍하는 방식으로 구현된 제너레이터 함수입니다.
이 함수는 io.StringIO 객체를 사용하여 메모리상에 CSV 형식의 데이터를 쓰고 각 행이 작성될 때마다
현재까지의 내용을 yield를 통해 반환합니다.
이를 통해 데이터는 연속적인 스트림으로 소비자에게 전달될 수 있으며 전체 데이터세트가 한번에 메모리에 로드될
필요가 없기 때문에 메모리 사용을 최적화할 수 있습니다.

yield문은 함수의 실행을 일시 중지하고 함수가 생성한 값을 호출자에게 전달합니다. 함수가 다시 호출되면 실행은 yield문
다음부터 계속됩니다.
이러한 방식은 데이터를 청크 단위로 나누어 전송하는 데 유용합니다.

csv_streamer() 함ㅅ수내에서 csv.writer는 StringIO 스트림에 CSV 형식의 행을 작성합니다.
각 행을 작성한 후, output.getvalue()를 통해 StringIO 버퍼의 내용을 가져와서 yield합니다.
이후 output.flush()를 호출하여 스트림을 비우고 output.truncate(0)으로 버퍼의 내용을 지우며
output.seek(0)으로 스트림의 위치를 처음 으로 되돌립니다.
이러한 과정을 반복하면서 데이터는 행 단위로  클라이언트에게 전송됩니다.

StreamingResponse 객체는 csv_streamer() 함수엣서 생성된 스트림을 응답으로 ㅡ저느달합니다.
headers={"Content-Type": "text/csv}를 설정함으로써 응답의 MIME 타입이 CSV임을 명시합니다.
이 헤더는 웹 브라우저나 다른 클라이언트가 응답을 받을때 데이터가 CSV 형식임을 인식하고 적절하게 처리할 수 있도록 도와줍니다.

@app.get("/csv") 데코레이터는 /csv 경로로 들어오는 HTTP GET 요청을 get_csv() 함수로 라우팅합니다.
해당 함수는 StreaminResponse를 반환함으로써 요청을 받는 즉시 클라이언트에게 데이터 스트리밍을 시작합니다.
이는 대용량 데이터를 처리할 때 특히 유용하며 클라이언트는 파일 전체를 다운로드하지 않고도 스트림의 일부를
실시간으로 받아볼 수 있습니다.
"""
from modules.Notification import Notification
from datetime import time

from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 홈 페이지
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 약 정보 조회 API
@app.get("/medicine/{medicine_id}")
def read_medicine(medicine_id: int, q: str = None):
    return {"medicine_id": medicine_id, "q": q}

# 예시
notification_data = {
    "medicine_id": 1,
    "notification_type": "복용 알림",
    "notification_time": time(hour=9, minute=0),  # 시간을 time 객체로 생성
    "is_taken": False
}
notification = Notification(**notification_data)

# 알림 전송 API
@app.post("/notification/")
async def send_notification(notif: notification_data):

    # 알림 전송 로직 구현
    return {"result": "success"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)






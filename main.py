from fastapi import FastAPI

app = FastAPI()

# 홈 페이지
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 약 정보 조회 API
@app.get("/medicine/{medicine_id}")
def read_medicine(medicine_id: int, q: str = None):
    return {"medicine_id": medicine_id, "q": q}

# 알림 전송 API
@app.post("/notification/")
async def send_notification(notif: Notification):
    # 알림 전송 로직 구현
    return {"result": "success"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)






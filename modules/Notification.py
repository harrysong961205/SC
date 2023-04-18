from pydantic import BaseModel
from datetime import time

class Notification(BaseModel):
    medicine_id: int
    notification_type: str
    notification_time: time
    is_taken: bool
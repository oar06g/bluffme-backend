from fastapi import APIRouter

class BluffMe:
  def __init__(self):
    self.router = APIRouter()

    @self.router.get("/create-room")
    def create():
      return {"Hello": "World"}
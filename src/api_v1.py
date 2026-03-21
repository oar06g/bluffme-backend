from fastapi import APIRouter

class BluffMe:
  def __init__(self):
    self.router = APIRouter()

    @self.router.get("/")
    def read_root():
      return {"Hello": "World"}
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str
    name: str

@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"You wrote: '{item.name}'"}
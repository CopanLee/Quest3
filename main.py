from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet(name: Union[str, None] = None):
    if name:
        return {"message": f"Hello, {name}!"}
    return {"message": "Hello, World!"}
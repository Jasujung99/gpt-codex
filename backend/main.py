from fastapi import FastAPI
import uvicorn

from backend import users
from backend import projects

app = FastAPI()

app.include_router(users.router)
app.include_router(projects.router)

@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

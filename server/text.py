from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Ai Chat Server is running!"}
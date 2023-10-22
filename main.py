from fastapi import FastAPI, Response
import uvicorn

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)

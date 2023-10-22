from fastapi import FastAPI, Response
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Awesome cloud developer dff9 says hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

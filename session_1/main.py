import fastapi

app = fastapi.FastAPI()


@app.get("/")
async def say_hello():
    return "Hello, world!"

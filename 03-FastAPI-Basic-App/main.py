from fastapi import FastAPI

app = FastAPI(title="Basic FastAPI App")


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}


@app.get("/greet/{name}")
def greet_name(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/greet")
def greet_query(name: str = "World"):
    return {"message": f"Hello, {name}!"}

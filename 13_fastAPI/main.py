from fastapi import FastAPI

app = FastAPI()
app.counter = 0


@app.get("/")
def root():
    return {"message": "Hello World World World!"}


@app.get("/hello/{name}")
def hello_name(name: str):
    return f'Hello {name.capitalize()}'


@app.get("/counter")
def count():
    app.counter += 1
    return {"counter": app.counter}


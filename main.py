from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello_check():
    return {
        "msg":"Hello world check"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app"
    )
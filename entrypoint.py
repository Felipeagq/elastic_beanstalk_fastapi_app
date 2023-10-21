from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello_check():
    return {
        "msg":"Hello world check"
    }


@app.get("/otra")
def otra():
    return {
        "msg":"otra ruta"
    }


@app.get("/alternativa")
def otra():
    return {
        "msg":"ruta alternativa"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app"
    )
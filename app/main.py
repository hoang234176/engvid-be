from fastapi import FastAPI
import uvicorn

app = FastAPI()

PORT = 8000  # Default port

@app.get("/")
def read_root():
    res = {
        "status": "success",
        "message": f"Backend is running in port:{PORT}",
        "data": {
            "port": PORT,
        }
    }
    return res  

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
from fastapi import FastAPI
import uvicorn
from routers import thread



app = FastAPI()


app.include_router(thread.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8123, log_level="debug")
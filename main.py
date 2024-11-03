from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/beep")
async def beep():
    return {"message": "BEEEEEP!!"}

# Handler for AWS Lambda
handler = Mangum(app)

# Add this section for local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
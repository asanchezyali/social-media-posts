# api_server.py
import asyncio
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Latency Demo API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Fast endpoint with consistent response time"""
    return {"message": "Latency demonstration API"}

@app.get("/fast")
async def fast_endpoint():
    """Endpoint with fast response (10-30ms)"""
    await asyncio.sleep(random.uniform(0.01, 0.03))
    return {"response_type": "fast"}

@app.get("/medium")
async def medium_endpoint():
    """Endpoint with medium response time (50-150ms)"""
    await asyncio.sleep(random.uniform(0.05, 0.15))
    return {"response_type": "medium"}

@app.get("/slow")
async def slow_endpoint():
    """Endpoint with slow response time (200-500ms)"""
    await asyncio.sleep(random.uniform(0.2, 0.5))
    return {"response_type": "slow"}

@app.get("/variable")
async def variable_endpoint():
    """
    Endpoint with variable response time:
    - 80% of requests: fast (10-50ms)
    - 15% of requests: medium (100-300ms)
    - 5% of requests: very slow (500-1500ms)
    """
    random_value = random.random()
    
    if random_value < 0.8:
        await asyncio.sleep(random.uniform(0.01, 0.05))
        category = "fast (80%)"
    elif random_value < 0.95:
        await asyncio.sleep(random.uniform(0.1, 0.3))
        category = "medium (15%)"
    else:
        await asyncio.sleep(random.uniform(0.5, 1.5))
        category = "very slow (5%)"
    
    return {"response_type": "variable", "category": category}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server:app", host="0.0.0.0", port=8000, reload=True)
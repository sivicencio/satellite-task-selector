from fastapi import FastAPI
from .routers import tasks

metadata = {
    "title": "Satellite task selector API",
    "description": "An API for handling satellite tasks"
}

tags_metadata = [
    {
        "name": "tasks",
        "description": "Operations regarding satellite tasks, including their state"
    }
]

app = FastAPI(
    **metadata,
    openapi_tags=tags_metadata
)

app.include_router(tasks.router, prefix='/tasks')

@app.get("/")
async def root():
    return {"title": "Satellite task selector API"}

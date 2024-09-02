from fastapi import FastAPI
from .database import engine, Base
from .routers import books
from fastapi.middleware.cors import CORSMiddleware

# Initialize the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, can be adjusted for production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

@app.get('/')
def show():
    return "hello"

app.include_router(books.router)

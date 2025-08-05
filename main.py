from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import upload, simplify, ask

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # <-- frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(simplify.router, prefix="/simplify")
app.include_router(ask.router)

@app.get("/")
def root():
    return {"message": "LexiSimplify Backend is running"}
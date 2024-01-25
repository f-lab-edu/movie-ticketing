from fastapi import FastAPI
from src.apis.auth.auth import router as auth_router
from src.apis.movies.movies import router as movies_router
from src.apis.reservations.reservations import router as reservations_router
from src.apis.payments.payments import router as payments_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(movies_router)
app.include_router(reservations_router)
app.include_router(payments_router)


@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

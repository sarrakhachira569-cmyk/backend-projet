from fastapi import FastAPI
from user.user_controller import router as user_router
from client.client_controller import router as client_router
from catégorie.catégorie_controller import router as catégorie_router

app = FastAPI()

app.include_router(user_router)
app.include_router(client_router)
app.include_router(catégorie_router)

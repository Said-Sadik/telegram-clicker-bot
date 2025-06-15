from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Простейшее хранилище
users = {}

@app.get("/balance/{user_id}")
def get_balance(user_id: str):
    return {"clicks": users.get(user_id, 0)}

@app.post("/click/{user_id}")
def click(user_id: str):
    users[user_id] = users.get(user_id, 0) + 1
    return {"clicks": users[user_id]}

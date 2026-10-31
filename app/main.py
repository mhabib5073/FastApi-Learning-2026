from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    age: int
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {
        "message": "user created",
        "data" : user
    }
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User, notify: bool = False):
    if 0<= user_id < len(users):
        users[user_id] = user
        return {
            "message": "User updated",
            "notify" : notify,
            "data": user
        }
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
    


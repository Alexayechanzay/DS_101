from fastapi import FastAPI
from pydantic import BaseModel # for validation

app = FastAPI()

#static routes
@app.get("/") #creating route
def index(): #http://127.0.0.1:8000/
    return {"message":"Hello World from FastAPI"}

#to run> uvicorn main:app --reload
@app.get("/about") 
def about_page():#http://127.0.0.1:8000/about
    return {"message":"This is about page"}

@app.get("/contact") 
def contact_page():#http://127.0.0.1:8000/contact
    return {"message":"This is a contact page"}

#dynamic routes
@app.get("/users/{user_id}") 
def user_page(user_id: int):
    return {"message":"Get user by id", "user_id":user_id}

@app.get("/search") 
def search_data(name: str): #http://127.0.0.1:8000/search?name=Computer
    return {"search":name}

class User(BaseModel): #inhert BaseModel
    name: str
    email: str
    age: int

class UserResponse(BaseModel):
    name: str
    age: int

#browser can only work with get method
@app.post("/users") #request sent to create data
def create_user(user: User): #use API testing platform (e.g,postman)
    return {"message":"Added User","user":user}

@app.post("/users",response_model=UserResponse)
def create_user(user: User):
    return user
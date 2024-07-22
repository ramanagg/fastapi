
from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional


app=FastAPI(title="CrudApp",
    description="Basic crud in FastAPI",
    summary="This is basic crud opeartions with minimal data",
    version="1.0",
        license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)

class userClass(BaseModel):
    id:int
    name:str
    

class updateUserClass(BaseModel):
    id:Optional[int]=None
    name:Optional[str]=None

users={
    1:{
        'id':1,
        'name':'Raman'
    },
    2:{
        'id':2,
        'name' : "Praman"
    }
}
    


@app.get('/')

def index():
    return {'id':1,'name':'raman'} 

@app.get('/get-user/{id}')
def get_user(id:int = Path(description="Id of user",gt=0)):
    try:
        return users[id]
    except:
        return {'success':'false','message':'Record not found'}
    
@app.get('/search-user')
def search_user(name:str):
        for user in users:
            if users[user]["name"] == name:
                return users[user]
        return {'success':'false','message':'Record not found'}

@app.post('/create-user')
def create_user(user: userClass):
    return user

@app.put('/update-user/{id}')
def update_user(id:int,user: updateUserClass):
    if id not in users:
        return "Data not exist"
    users[id]=user
    return users[id]

@app.delete('/delete-user/{id}')
def delete_user(id:int):
    if id not in users:
        return {"message":"Data not exist"}
    del users[id]
    return {"message":"Data deleted successfully"}



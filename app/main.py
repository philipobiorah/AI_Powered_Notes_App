from fastapi import  FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message":"Welcome to AI Note App"}


@app.post("/createnote")
def createnote(payload: dict = Body(...)):
    print(payload)
    return {"new_note":f"title {payload['title']} content{payload['content']}"}
    

#Fetch all notes
@app.get("/notes")
def getNotes():
    return {"Fetch all notes successful"}


#Perform sentiment analyis
@app.get("/notes/{id}/analyze")
def check_sentiment():
    return {"Sentiment Analysis result": "sentiment"}



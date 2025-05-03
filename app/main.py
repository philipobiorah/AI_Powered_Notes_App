from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message":"Welcome to AI Note App"}


@app.post("/createnote")
def createnote():
    return {"message": "Note created successfully"}

#Fetch all notes
@app.get("/notes")
def getNotes():
    return {"Fetch all notes successful"}


#Perform sentiment analyis
@app.get("/notes/{id}/analyze")
def check_sentiment():
    return {"Sentiment Analysis result": "sentiment"}



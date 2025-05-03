from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message":"Welcome to AI Note App"}


@app.post("/createnote")
def createnote():
    return {"message": "Note created successfully"}

@app.get("/notes")
#Fetch all notes
def getNotes():
    return {"Fetch all notes successful"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def view():
    return {"message" : "Welcome To FastAPI"}

@app.get("/about")
def about():
    return {"about" : "This is About Page"}
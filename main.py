from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management system api"}
@app.get('/about')
def about():
    return {"message": "This is a Patient Management System API built with FastAPI."}

@app.get("/view")
def view_patients():
    data = load_data()
    return data
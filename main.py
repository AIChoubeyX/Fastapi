from fastapi import FastAPI , Path , HTTPException , Query
import json

app = FastAPI()
# function to load data from JSON file
def load_data():
    with open('patients.json' , 'r') as f:
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

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve" , example="P001")):
    # Load data from JSON file
    data = load_data()
    # Find patient by ID
    if patient_id in data :
        return data[patient_id]
    raise HTTPException(status_code=404 , detail="Patient not found")


@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description ='Sort on the basis of height, weight or bmi') , order: str =  Query('asc', description='Sort order: asc for ascending, desc for descending')):
    valid_fields = ['height' , 'weight' , 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400 , detail=f"Invalid sort_by field. Must be one of {valid_fields}")
    if order not in ['asc' , 'desc']:
        raise HTTPException(status_code=400 , detail="Invalid order. Must be 'asc' or 'desc'")
    data = load_data()

    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values() , key=lambda x: x[sort_by] , reverse=sort_order)
    return sorted_data




# querry paramters are optional key value pairs sent in the url after ? symbol use to pass additional information to the server
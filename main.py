from fastapi import FastAPI , Path , HTTPException , Query
from pydantic import BaseModel, Field, computed_field
from fastapi.responses import JSONResponse
from typing import List , Optional, Annotated, Literal
import json




app = FastAPI()

class Patient (BaseModel):
    id :Annotated[str , Field(..., description="Unique identifier for the patient" , json_schema_extra={'example': 'P001'})] 
    name : Annotated[str , Field(..., description="Full name of the patient" , json_schema_extra={'example': 'John Doe'})]
    city : Annotated[str , Field(..., description="City where the patient resides" , json_schema_extra={'example': 'New York'})]
    age : Annotated[int , Field(...,gt=0,lt=100, description="Age of the patient" , json_schema_extra={'example': 30})]
    gender : Annotated[Literal['male', 'female', 'others']  , Field(..., description="Gender of the patient" , json_schema_extra={'example': 'Male'})]
    height : Annotated[float , Field(...,gt=0, description="Height of the patient in centimeters" , json_schema_extra={'example': 175.5})]
    weight : Annotated[float , Field(...,gt=0, description="Weight of the patient in kilograms" , json_schema_extra={'example': 70.2})]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / ((self.height / 100) ** 2), 2)
        return bmi
    

    @computed_field 
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"



# function to load data from JSON file
def load_data():
    with open('patients.json' , 'r') as f:
        data = json.load(f)
    return data
# function to save data to JSON file
def save_data(data):
    with open('patients.json' , 'w') as f:
        json.dump(data , f)

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
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve" , examples=["P001"])):
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




# query parameters are optional key value pairs sent in the url after ? symbol use to pass additional information to the server


@app.post('/create')
def create_patient(patient: Patient):
    # Load existing data
    data = load_data()
    # Check if patient ID already exists
    if patient.id in data:
        raise HTTPException(status_code=400 , detail="Patient with this ID already exists")
    # new patient data addition
    data[patient.id] = patient.model_dump(exclude=['id'])
    # Save updated data back to JSON file
    save_data(data)
    return JSONResponse(status_code=201 , content={"message": "Patient created successfully"}) 
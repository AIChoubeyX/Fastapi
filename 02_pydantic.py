from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Data inserted successfully")
patient_info = {"name": "John Doe", "age": 30}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
from pydantic import BaseModel , EmailStr , AnyUrl
from typing import List , Dict , Optional

class Patient(BaseModel):
    name: str
    email : EmailStr
    # EmailStr is used to validate email format...it is a built-in type in pydantic
    age: int
    linkedin_profile : Optional[AnyUrl] = None
    weight : float
    married : bool = False
    allergies : Optional[List[str]] = None
    contact_details : Optional[Dict[str, str]] = None
    # optional is used to define fields that can be omitted
    # false is used to define default values for fields
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.linkedin_profile)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)


    print("Data inserted successfully")
patient_info = {"name": "John Doe", "email": "john.doe@example.com", "age": 30 , "weight": 70.5 , "linkedin_profile": "https://www.linkedin.com/in/johndoe", "married": False, "allergies": ["pollen", "nuts"], "contact_details": {"phone": "123-456-7890", "email": "john.doe@example.com"}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
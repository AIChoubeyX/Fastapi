from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name : str
    email : EmailStr
    age : int
    weight : float
    height : float
    married : bool 
    allergies : List[str]
    contact_details : Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / ((self.height / 100) ** 2), 2)
        return bmi
    
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("BMI:", patient.bmi)
    print("Data inserted successfully")

patient_info = {"name": "John Doe", "email": "john.doe@example.com", "age": 55 , "weight": 70.5 , "height": 175.0,"married": False, "allergies": ["pollen", "nuts"], "contact_details": {"phone": "123-456-7890", "email": "john.doe@example.com"}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)


# computed fields are read-only fields that are derived from other fields in the model.# They are defined using the @computed_field decorator and are typically implemented as properties.
# In this example, the bmi field is computed based on the weight and height fields.
# The bmi property calculates the Body Mass Index using the formula: weight (kg) / (height (m))^2.
# The computed bmi field is then accessed in the insert_patient_data function to display the BMI value along with other patient details.
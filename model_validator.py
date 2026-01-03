from pydantic import BaseModel , EmailStr , AnyUrl, Field, field_validator, model_validator
from typing import List , Dict , Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=1 , max_length=100, title="Full Name of the Patient" , description="The patient's full name must be between 1 and 100 characters long.")]
    # Annotated is used to add validation constraints to fields
    email : EmailStr
    # EmailStr is used to validate email format...it is a built-in type in pydantic
    age: int
    linkedin_profile : Optional[AnyUrl] = None
    weight : float = Field(..., gt=0 , description="Weight in kilograms")
    # Field is used to add extra validation and metadata to fields
    married : bool = False
    allergies : Optional[List[str]] = None
    contact_details : Optional[Dict[str, str]] = None
    # optional is used to define fields that can be omitted
    # false is used to define default values for fields
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients over 60 must have an emergency contact in contact_details")
        return model
    
    
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
patient_info = {"name": "John Doe", "email": "john.doe@example.com", "age": 55 , "weight": 70.5 , "linkedin_profile": "https://www.linkedin.com/in/johndoe", "married": False, "allergies": ["pollen", "nuts"], "contact_details": {"phone": "123-456-7890", "email": "john.doe@example.com"}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

# This will raise a validation error because the patient is over 60 and does not have an emergency contact in contact_details.
# model validator is used to perform validation that depends on multiple fields or the entire model.
# In this example, we check if the patient's age is over 60 and ensure that an emergency contact is provided in the contact_details dictionary.
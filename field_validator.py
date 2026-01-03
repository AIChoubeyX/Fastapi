from pydantic import BaseModel , EmailStr , AnyUrl, Field, field_validator
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
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['example.com', 'hdf.com', 'gmail.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of the following: {', '.join(valid_domains)}")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    
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
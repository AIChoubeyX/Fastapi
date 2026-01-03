from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address : Address
    
address_dict = {"city": "New York", "state": "NY", "pin": "10001"}    

address1 = Address(**address_dict)

patient_dict = {"name": "Alice Smith", "gender": "Female", "age": 28, "address": address_dict}

Patient1 = Patient(**patient_dict)
print(Patient1)
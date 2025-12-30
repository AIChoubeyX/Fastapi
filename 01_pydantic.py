def insert_patient_data(name:str,age:int):

    if type(name) == str and type(age) == int:
        print("name")
        print("age")
        print("Data inserted successfully")
    else:
        TypeError("Invalid data types for name or age")

insert_patient_data("John Doe",30)       



# main problem is if we not classify the data types then while inserting wrong data types may be inserted leading to issues later on
# to overcome this we can use pydantic models to define the data types and structure of the data we want to insert
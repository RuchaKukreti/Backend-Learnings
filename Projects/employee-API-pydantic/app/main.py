#db
employees =[(1, "John","Software Engineer",50000,"Project A"),
            (2, "Jane", "Data Analyst", 60000, "Project B"),
            (3, "Alice", "Project Manager", 70000, "Project C"),
            (4, "Bob", "UX Designer", 55000, "Project D"),
            (5, "Charlie", "DevOps Engineer", 65000, "Project E")]

#DTOs/ Models

from pydantic import BaseModel
from pydantic import Field

class employeeCreateRequest(BaseModel):
      employee_id : int
      employee_name : str
      employee_designation : str
      salary : int
      project : str
          

class employeeReadRequest(BaseModel):
      employee_id : int

class employeeUpdateRequest(BaseModel):
      employee_id : int =Field(default=None, ge=2, le=50)
      employee_name : str =Field(default=None, min_length=2, max_length=50)
      employee_designation : str =Field(default=None)
      salary : int =Field(default=None)
      project : str =Field(default=None)

class employeeDeleteRequest(BaseModel):
      employee_id : int

#APIs

from fastapi import FastAPI
app=FastAPI()

@app.get("/employees/{id}")
def get_employee(id: int):
    for employee in employees:
        if employee[0] == id:
            return employee
    return {"message" :"Employee not found"}

@app.post("/employees")
def create_employee(employeeCreateRequest : employeeCreateRequest):
    new_employee = {
        "employee_id": employeeCreateRequest.employee_id,
        "employee_name": employeeCreateRequest.employee_name,
        "employee_designation": employeeCreateRequest.employee_designation,
        "salary": employeeCreateRequest.salary,
        "project": employeeCreateRequest.project,
    }
    employees.append(new_employee)
    return new_employee
    
@app.delete("/employees")
def delete_employee(employeeDeleteRequest : employeeDeleteRequest):
    for employee in employees:
        if employee[0] == employeeDeleteRequest.employee_id:
            employees.remove(employee)
            return {"message": "Employee deleted successfully"}
    return {"message": "Employee not found"}

@app.put("/employees")
def update_employee(employeeUpdateRequest : employeeUpdateRequest):
    for employee in employees:
        if employee[0] == employeeUpdateRequest.employee_id:
            updated_employee = (
                employeeUpdateRequest.employee_id,
                employeeUpdateRequest.employee_name,
                employeeUpdateRequest.employee_designation,
                employeeUpdateRequest.salary,
                employeeUpdateRequest.project,
            )
            employees[employees.index(employee)] = updated_employee
            return updated_employee
    return {"message": "Employee not found"}

@app.patch("/employees")
def patch_employee(employeeUpdateRequest : employeeUpdateRequest):
    for employee in employees:
        if employee[0] == employeeUpdateRequest.employee_id:
            updated_employee = (
                employeeUpdateRequest.employee_id,
                employeeUpdateRequest.employee_name if employeeUpdateRequest.employee_name is not None else employee[1],
                employeeUpdateRequest.employee_designation if employeeUpdateRequest.employee_designation is not None else employee[2],
                employeeUpdateRequest.salary if employeeUpdateRequest.salary is not None else employee[3],
                employeeUpdateRequest.project if employeeUpdateRequest.project is not None else employee[4],
            )
            employees[employees.index(employee)] = updated_employee
            return updated_employee
    return {"message": "Employee not found"}
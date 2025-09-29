# employee_crud

## Features
- Create a new employee with **auto-generated ID**.
- Upload a profile photo (max 5 MB).
- List all employees.
- Update employee details.
- Soft-delete employee records (is_deleted = True).
- Versioned API (`/api/v1/`).

- API Endpoints

Base URL: /api/v1/

1. List all Employees

Method: GET
URL: /api/v1/employees/

2. Create Employee

Method: POST
URL: /api/v1/employees/

Body (form-data):

employee_name: Naveen
email: naveen@gmail.com
photo: (image file, max 5 MB)

3. Retrieve Employee

Method: GET
URL: /api/v1/employees/<uuid>/

Description: Retrieve details of a single employee by ID.


4. Update Employee

Method: PUT
URL: /api/v1/employees/<uuid>/

Body (form-data or JSON):

employee_name: Naveen P Anil
email: naveen@gmail.com
photo: (image file, max 5 MB)


5. Delete Employee (Soft Delete)

Method: DELETE

URL: /api/v1/employees/<uuid>/

Description: Marks is_deleted = True for the employee.

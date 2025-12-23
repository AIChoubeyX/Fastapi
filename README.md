# Patient Management System API

A FastAPI-based REST API for managing patient health data including BMI calculations and health verdicts.

## Overview

This application provides a simple yet effective API for viewing and managing patient information. It includes data for 55+ patients with their health metrics and corresponding health verdicts (Normal, Overweight, Obese, Underweight).

## Features

- **Patient Data Management**: Store and retrieve patient information
- **Health Metrics**: Track height, weight, and BMI
- **RESTful API**: Clean and intuitive endpoints
- **JSON Data Storage**: Simple file-based data management with `patients.json`

## Project Structure

```
Fastapi/
├── main.py              # FastAPI application entry point
├── patients.json        # Patient data storage (55+ records)
├── README.md           # This file
└── myenv/              # Python virtual environment
```

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn (ASGI server)

## Installation

### 1. Create Virtual Environment

```bash
python -m venv myenv
```

### 2. Activate Virtual Environment

**On Windows:**
```bash
myenv\Scripts\activate
```

**On macOS/Linux:**
```bash
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn
```

## Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, interactive API documentation is available at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### 1. **GET `/`**
Returns a welcome message and API description.

**Response:**
```json
{
  "message": "Patient Management system api"
}
```

### 2. **GET `/about`**
Returns information about the API.

**Response:**
```json
{
  "message": "This is a Patient Management System API built with FastAPI."
}
```

### 3. **GET `/view`**
Returns all patient records from the database.

**Response:**
```json
{
  "P001": {
    "name": "Ananya Sharma",
    "city": "Guwahati",
    "age": 28,
    "gender": "female",
    "height": 1.65,
    "weight": 90.0,
    "bmi": 33.06,
    "verdict": "Obese"
  },
  ...
}
```

## Patient Data Format

Each patient record contains:

| Field | Type | Description |
|-------|------|-------------|
| name | string | Patient's full name |
| city | string | Patient's city of residence |
| age | integer | Patient's age in years |
| gender | string | Patient's gender (male/female) |
| height | float | Patient's height in meters |
| weight | float | Patient's weight in kilograms |
| bmi | float | Body Mass Index (calculated) |
| verdict | string | Health status (Normal, Overweight, Obese, Underweight) |

## Health Verdict Categories

- **Underweight**: BMI < 18.5
- **Normal**: BMI 18.5 - 24.9
- **Overweight**: BMI 25.0 - 29.9
- **Obese**: BMI ≥ 30.0

## Example Usage

### Using cURL

```bash
# Get welcome message
curl http://localhost:8000/

# Get API information
curl http://localhost:8000/about

# Get all patients
curl http://localhost:8000/view
```

### Using Python

```python
import requests

# Get all patients
response = requests.get("http://localhost:8000/view")
patients = response.json()
print(patients)
```

## Database

Patient data is stored in `patients.json` as a JSON file with 55+ patient records. This is a simple file-based storage solution suitable for development and testing.

## Future Enhancements

- Add database integration (SQLite, PostgreSQL, etc.)
- Implement CRUD operations (Create, Read, Update, Delete)
- Add authentication and authorization
- Add filtering and search capabilities
- Implement pagination for large datasets
- Add data validation
- Add patient history tracking

## Troubleshooting

### Port Already in Use

If port 8000 is already in use, specify a different port:

```bash
uvicorn main:app --reload --port 8001
```

### Module Not Found

Ensure your virtual environment is activated and FastAPI/Uvicorn are installed:

```bash
pip install --upgrade fastapi uvicorn
```

### patients.json Not Found

Ensure `patients.json` is in the same directory as `main.py`.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please check:
- FastAPI Documentation: https://fastapi.tiangolo.com/
- Uvicorn Documentation: https://www.uvicorn.org/

---

**Version:** 1.0.0  
**Last Updated:** December 2025

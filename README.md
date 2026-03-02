# Student REST API (Flask)

## Description
This project implements RESTful APIs for managing student data using Flask. 
The data is stored in an in-memory array.

## Features
- Create student
- Read all students
- Read single student
- Update student
- Delete student

## Endpoints

GET /students
POST /students
GET /students/<id>
PUT /students/<id>
DELETE /students/<id>

## Sample JSON (POST)
{
    "id": 1,
    "name": "Manjeet",
    "age": 21,
    "course": "B.Tech"
}

## Run Locally
pip install -r requirements.txt
python app.py

## Deployment (Render)
1. Push code to GitHub
2. Go to https://render.com
3. Create Web Service
4. Connect GitHub repo
5. Set:
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
6. Deploy

## Testing
Use Postman to test all endpoints.

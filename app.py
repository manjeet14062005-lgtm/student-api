from flask import Flask, request, jsonify
import os

app = Flask(__name__)

students = []

# Home route (optional)
@app.route('/')
def home():
    return "Student API is running"

# GET all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# GET single student
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student['id'] == id:
            return jsonify(student)
    return jsonify({"message": "Not found"}), 404

# POST (create student)
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    student = {
        "id": data['id'],
        "name": data['name'],
        "age": data['age'],
        "course": data['course']
    }
    students.append(student)
    return jsonify({"message": "Added", "student": student}), 201

# PUT (update student)
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    for student in students:
        if student['id'] == id:
            student['name'] = data.get('name', student['name'])
            student['age'] = data.get('age', student['age'])
            student['course'] = data.get('course', student['course'])
            return jsonify({"message": "Updated", "student": student})
    return jsonify({"message": "Not found"}), 404

# DELETE student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    for student in students:
        if student['id'] == id:
            students.remove(student)
            return jsonify({"message": "Deleted"})
    return jsonify({"message": "Not found"}), 404

# Run app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
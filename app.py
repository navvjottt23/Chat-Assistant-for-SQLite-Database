from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to execute SQL queries
def execute_query(query, params=()):
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

# Route to handle chat queries
@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get('query')
    
    if "show me all employees in the" in user_query.lower():
        department = user_query.lower().split("department")[0].split("in the")[1].strip()
        result = execute_query("SELECT Name FROM Employees WHERE Department = ?", (department,))
        if result:
            return jsonify({"response": [row[0] for row in result]})
        else:
            return jsonify({"response": "No employees found in this department."})
    
    elif "who is the manager of the" in user_query.lower():
        department = user_query.lower().split("department")[0].split("of the")[1].strip()
        result = execute_query("SELECT Manager FROM Departments WHERE Name = ?", (department,))
        if result:
            return jsonify({"response": result[0][0]})
        else:
            return jsonify({"response": "Department not found."})
    
    elif "list all employees hired after" in user_query.lower():
        date = user_query.lower().split("after")[1].strip()
        result = execute_query("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
        if result:
            return jsonify({"response": [row[0] for row in result]})
        else:
            return jsonify({"response": "No employees hired after this date."})
    
    elif "what is the total salary expense for the" in user_query.lower():
        department = user_query.lower().split("department")[0].split("for the")[1].strip()
        result = execute_query("SELECT SUM(Salary) FROM Employees WHERE Department = ?", (department,))
        if result:
            return jsonify({"response": result[0][0]})
        else:
            return jsonify({"response": "Department not found."})
    
    else:
        return jsonify({"response": "Sorry, I don't understand that query."})

# Home route
@app.route('/')
def home():
    return "Welcome to the SQLite Chat Assistant!"

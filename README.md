# Chat-Assistant-for-SQLite-Database
This is a Python-based chat assistant that interacts with an SQLite database to answer user queries. The assistant supports natural language queries and converts them into SQL queries to fetch data from the database. It is built using Flask for the backend and a simple HTML frontend for user interaction.
# Features
1. Natural Language Queries: Users can ask questions in plain English.

2. SQLite Database: Stores employee and department data.

3. Flask Backend: Handles query processing and database interactions.

4. HTML Frontend: Provides a user-friendly chat interface.

5. Deployment on Railway: Hosted on Railway for public access

# Steps to Run the Project Locally
Prerequisites
Python 3.7 or higher

pip (Python package manager)

## Step 1: Clone the Repository
Clone the project repository to your local machine:

bash
Copy
git clone https://github.com/navvjottt23/Chat-Assistant-for-SQLite-Database
cd sqlite-chat-assistant

## Step 2: Set Up the Database
Navigate to the project directory.

Run the following Python script to create and populate the SQLite database:

bash
Copy
python setup_database.py
This will create a company.db file with the required tables and sample data.

## Step 3: Install Dependencies
Install the required Python packages:

bash
Copy
pip install -r requirements.txt

## Step 4: Run the Application
Start the Flask server:

bash
Copy
python app.py
Open your browser and navigate to:

Copy
http://127.0.0.1:5000

## Step 5: Interact with the Chatbot
Enter your query in the input box and click "Send".

The chatbot will process your query and display the response in the chat window.

# Project Structure

sqlite-chat-assistant/
├── app.py                # Flask backend
├── setup_database.py     # Script to create and populate the database
├── company.db            # SQLite database file
├── templates/            # HTML templates
│   └── index.html        # Chatbot frontend
├── static/               # Static files (CSS, JS, images)
│   └── styles.css        # Optional: CSS file for styling
├── requirements.txt      # Python dependencies
├── Procfile              # For Railway deployment
└── README.md             # Project documentation

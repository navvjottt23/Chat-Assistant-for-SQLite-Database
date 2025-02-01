## Chat-Assistant-for-SQLite-Database
This is a Python-based chat assistant that interacts with an SQLite database to answer user queries. The assistant supports natural language queries and converts them into SQL queries to fetch data from the database. It is built using Flask for the backend and a simple HTML frontend for user interaction.
## Features
Natural Language Queries: Users can ask questions in plain English.

SQLite Database: Stores employee and department data.

Flask Backend: Handles query processing and database interactions.

HTML Frontend: Provides a user-friendly chat interface.

Deployment on Railway: Hosted on Railway for public access

## How It Works
User Input:

The user types a query in the chat interface (e.g., "Show me all employees in the Sales department").

Query Parsing:

The Flask backend uses simple string matching and regular expressions to parse the query and extract relevant parameters (e.g., department name, date).

SQL Query Execution:

The backend constructs an SQL query based on the parsed input and fetches data from the SQLite database (company.db).

Response Generation:

The backend formats the fetched data into a user-friendly response and sends it back to the frontend.

Frontend Display:

The HTML frontend displays the user's query and the chatbot's response in a chat-like interface.

## Supported Queries
The chat assistant supports the following types of queries:

Show me all employees in the [department] department.

Example: "Show me all employees in the Sales department."

Who is the manager of the [department] department?

Example: "Who is the manager of the Engineering department?"

List all employees hired after [date].

Example: "List all employees hired after 2021-01-01."

What is the total salary expense for the [department] department?

Example: "What is the total salary expense for the Marketing department?"


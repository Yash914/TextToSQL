Hybrid Schema-Aware Text-to-SQL System
Project Overview

This project implements a Hybrid Text-to-SQL system that converts natural language queries into SQL statements.

The system combines machine learning techniques with rule-based SQL generation.
Rule-based logic is used for deterministic database operations, while the ML component is used to interpret natural language queries for data retrieval.

The generated SQL queries are executed using a SQLite database backend.

System Architecture
User Input
   │
   ▼
Intent Detection
   │
   ├── CRUD Operation → Rule-Based SQL Builder
   │
   └── SELECT Query → ML Text-to-SQL Model
   │
   ▼
SQLite Query Execution
   │
   ▼
Result Output
Key Features

Natural language to SQL conversion

Hybrid architecture (ML + rule-based)

Dynamic table creation

Insert, update, and delete operations

Intelligent SELECT query interpretation

SQLite database integration

Modular and extendable code structure

Technologies Used

Python

SQLite

PyTorch (optional ML component)

Project Structure
TextToSQL/
│
├── main.py
├── schema_manager.py
├── intent_classifier.py
├── database.db
├── requirements.txt
├── README.md
└── .gitignore
How to Run
1. Clone the Repository
git clone https://github.com/yourusername/TextToSQL.git
cd TextToSQL
2. Run the Program
python main.py
Example Commands
Create Table
create table student with roll_no int, name text, cgpa real
Insert Data
insert student roll_no 1 name yash cgpa 9.2
Show Data
show student
Update Data
update student set cgpa 9.8 where roll_no 1
Delete Data
delete from student where roll_no 2
Academic Relevance

This project demonstrates concepts related to:

Natural Language Processing

Text-to-SQL generation

Hybrid AI system design

Schema-aware query generation

Database management systems

Backend system architecture

Future Improvements

Transformer-based Text-to-SQL model

Schema-aware neural encoding

Execution-based accuracy evaluation

Web interface using Flask or React

Multi-database support

Hybrid Schema-Aware Text-to-SQL System
Project Overview

This project implements a Hybrid Text-to-SQL system that converts natural language queries into SQL statements.

The system combines machine learning techniques with rule-based SQL generation.
Rule-based logic is used for deterministic operations like table creation and data manipulation, while the ML component is used to interpret natural language queries for data retrieval.

The system executes generated queries on a SQLite database.

System Architecture

User Input
↓
Intent Detection
↓
If CRUD operation → Rule-based SQL generator
If SELECT query → ML-based Text-to-SQL module
↓
SQL Execution using SQLite
↓
Query Result

Key Features

Natural language to SQL conversion

Hybrid architecture (ML + rule-based)

Supports basic database operations

Dynamic table creation

Insert, update and delete support

SQLite database integration

Modular and easy-to-extend code structure

Technologies Used

Python

SQLite

PyTorch (for ML model – optional)

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
Clone the repository
git clone https://github.com/yourusername/TextToSQL.git
cd TextToSQL
Run the program
python main.py
Example Commands

Create table

create table student with roll_no int, name text, cgpa real

Insert data

insert student roll_no 1 name yash cgpa 9.2

Show data

show student

Update data

update student set cgpa 9.8 where roll_no 1

Delete data

delete from student where roll_no 2
Learning Outcomes

This project helped in understanding:

Natural Language Processing basics

Text-to-SQL systems

Hybrid AI system design

Database query execution

Backend system architecture

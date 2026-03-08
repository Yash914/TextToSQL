
# Hybrid Schema-Aware Text-to-SQL System

## Overview
The **Hybrid Schema-Aware Text-to-SQL System** converts natural language queries into executable SQL statements. 
The system combines **machine learning techniques** with **rule-based SQL generation** to provide both flexibility and reliability.

Rule-based logic is used for deterministic database operations such as creating tables or inserting data, while the ML component interprets natural language queries for data retrieval. The generated SQL queries are executed using a **SQLite database backend**.

---

## System Architecture

User Input  
→ Intent Detection  
→ CRUD Operations → Rule-Based SQL Generator  
→ SELECT Queries → ML Text-to-SQL Module  
→ SQLite Query Execution  
→ Result Output

---

## Key Features

- Natural language to SQL query conversion
- Hybrid architecture (Machine Learning + Rule-based system)
- Support for CRUD operations (Create, Read, Update, Delete)
- Schema-aware query processing
- SQLite database integration
- Modular and extensible project structure

---

## Technologies Used

- **Python**
- **SQLite**
- **PyTorch** (optional ML component)

---

## Project Structure

```
TextToSQL/
│
├── main.py                 # Main application entry point
├── schema_manager.py       # Handles database schema creation and management
├── intent_classifier.py    # Determines query intent (CRUD or SELECT)
├── database.db             # SQLite database file
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignored files
```

---

## Installation and Setup

### 1. Clone the Repository

```
git clone https://github.com/yourusername/TextToSQL.git
cd TextToSQL
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the Application

```
python main.py
```

---

## Example Commands

### Create Table
```
create table student with roll_no int, name text, cgpa real
```

### Insert Data
```
insert student roll_no 1 name yash cgpa 9.2
```

### Retrieve Data
```
show student
```

### Update Data
```
update student set cgpa 9.8 where roll_no 1
```

### Delete Data
```
delete from student where roll_no 2
```

---

## Academic Significance

This project demonstrates key concepts from:

- Natural Language Processing (NLP)
- Text-to-SQL generation
- Hybrid AI system design
- Database Management Systems
- Backend system architecture

---

## Future Improvements

- Transformer-based Text-to-SQL model
- Improved schema-aware neural encoding
- Web interface using Flask or React
- Support for multiple database systems
- Query optimization techniques

---

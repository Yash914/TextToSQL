# 🚀 Hybrid Schema-Aware Text-to-SQL System

## 📌 Project Overview

This project implements a **Hybrid Text-to-SQL System** that converts
natural language queries into executable SQL statements.

The system intelligently combines:

-   🧠 Machine Learning (for intelligent SELECT query generation)
-   🛠 Rule-Based SQL Construction (for deterministic CRUD operations)
-   🗄 SQLite backend for real SQL execution

This hybrid architecture ensures both **stability** and
**intelligence**.

------------------------------------------------------------------------

## 🏗 System Architecture

User Input\
↓\
Intent Detection\
↓\
If CRUD → Rule-Based SQL Builder\
If SELECT → ML Text-to-SQL Model\
↓\
SQLite Execution Engine\
↓\
Result Output

------------------------------------------------------------------------

## ✨ Key Features

-   Dynamic table creation
-   Schema-aware insert operations
-   Update and delete support
-   Intelligent SELECT query handling
-   SQLite database integration
-   Hybrid ML + Rule-based architecture
-   Persistent database storage
-   Modular clean code structure

------------------------------------------------------------------------

## 🧠 What Makes It Hybrid?

### 🔹 Machine Learning Handles:

-   Complex SELECT queries
-   WHERE conditions
-   JOIN operations
-   Aggregations (AVG, COUNT, MAX)
-   Natural language interpretation

### 🔹 Rule-Based Engine Handles:

-   CREATE TABLE
-   INSERT
-   UPDATE
-   DELETE

This ensures stability for deterministic operations while allowing ML to
handle semantic reasoning.

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python 3.10+
-   SQLite
-   PyTorch (for ML component -- optional/extendable)

------------------------------------------------------------------------

## 📂 Project Structure

TextToSQL/ │ ├── main.py\
├── schema_manager.py\
├── intent_classifier.py\
├── database.db\
├── requirements.txt\
├── README.md\
└── .gitignore

------------------------------------------------------------------------

## ▶️ How To Run

### 1️⃣ Clone Repository

git clone https://github.com/yourusername/TextToSQL.git\
cd TextToSQL

### 2️⃣ Run Application

python main.py

------------------------------------------------------------------------

## 🧪 Example Commands

### Create Table

create table student with roll_no int, name text, cgpa real

### Insert Data

insert student roll_no 1 name yash cgpa 9.2

### Show Data

show student

### Update Data

update student set cgpa 9.8 where roll_no 1

### Delete Data

delete from student where roll_no 2

------------------------------------------------------------------------

## 🎓 Academic Significance

This project demonstrates:

-   Natural Language Processing (NLP)
-   Text-to-SQL generation
-   Hybrid AI system design
-   Schema-aware reasoning
-   Database management systems
-   Modular backend architecture

------------------------------------------------------------------------

## 📊 Future Enhancements

-   Transformer-based Text-to-SQL model
-   Schema-aware neural encoding
-   Execution-based accuracy evaluation
-   Web-based UI (Flask/React)
-   Multi-database support
-   Authentication system

------------------------------------------------------------------------

## 👨‍💻 Author

Yash Madane\
Computer Engineering Student

------------------------------------------------------------------------

## 📜 License

This project is created for academic and learning purposes.

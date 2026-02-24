import sqlite3

class SchemaManager:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.schemas = {}  # {table: {column: type}}

    # ================= CREATE TABLE =================
    def create_table(self, table_name, columns):
        column_defs = []
        parsed_columns = {}

        for col in columns:
            parts = col.strip().split()

            if len(parts) == 2:
                col_name = parts[0]
                col_type = parts[1].upper()
            else:
                col_name = parts[0]
                col_type = "TEXT"

            if col_type in ["INT", "INTEGER"]:
                col_type = "INTEGER"
            elif col_type in ["REAL", "FLOAT", "DOUBLE"]:
                col_type = "REAL"
            else:
                col_type = "TEXT"

            column_defs.append(f"{col_name} {col_type}")
            parsed_columns[col_name] = col_type

        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_defs)})"

        self.cursor.execute(query)
        self.connection.commit()

        self.schemas[table_name] = parsed_columns
        return query

    # ================= INSERT =================
    def insert(self, table_name, values_dict):
        if table_name not in self.schemas:
            return "Table does not exist."

        schema = self.schemas[table_name]
        columns = []
        values = []

        for col, val in values_dict.items():
            if col in schema:
                columns.append(col)

                if schema[col] == "INTEGER":
                    values.append(str(int(val)))
                elif schema[col] == "REAL":
                    values.append(str(float(val)))
                else:
                    values.append(f"'{val}'")

        if not columns:
            return "No valid columns found."

        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)})"

        self.cursor.execute(query)
        self.connection.commit()

        return query

    # ================= SELECT =================
    def select_all(self, table_name):
        if table_name not in self.schemas:
            return "Table does not exist."

        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # ================= UPDATE =================
    def update(self, table_name, set_col, set_val, where_col, where_val):
        if table_name not in self.schemas:
            return "Table does not exist."

        query = f"UPDATE {table_name} SET {set_col} = '{set_val}' WHERE {where_col} = '{where_val}'"

        self.cursor.execute(query)
        self.connection.commit()
        return query

    # ================= DELETE =================
    def delete(self, table_name, where_col, where_val):
        if table_name not in self.schemas:
            return "Table does not exist."

        query = f"DELETE FROM {table_name} WHERE {where_col} = '{where_val}'"

        self.cursor.execute(query)
        self.connection.commit()
        return query
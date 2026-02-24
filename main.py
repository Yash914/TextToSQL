import re
from schema_manager import SchemaManager
from intent_classifier import detect_intent

schema_manager = SchemaManager()

print("Dynamic Schema-Aware SQL System Ready!")
print("Type 'exit' to quit.\n")

while True:
    question = input("Enter your question: ")

    if question.lower() == "exit":
        break

    intent = detect_intent(question)

    # ================= CREATE =================
    if intent == "CREATE":
        match = re.match(r"create table (\w+) with (.+)", question.lower())
        if match:
            table_name = match.group(1)
            columns_raw = match.group(2)
            columns = [col.strip() for col in columns_raw.split(",")]

            query = schema_manager.create_table(table_name, columns)
            print("Generated SQL:", query)
        else:
            print("Invalid CREATE syntax.")

    # ================= INSERT =================
    elif intent == "INSERT":
        words = question.lower().split()
        table_name = words[1]

        if table_name not in schema_manager.schemas:
            print("Table does not exist.")
            continue

        schema = schema_manager.schemas[table_name]
        values = {}

        for i in range(len(words) - 1):
            if words[i] in schema:
                values[words[i]] = words[i + 1]

        query = schema_manager.insert(table_name, values)
        print("Generated SQL:", query)

    # ================= SELECT =================
    elif intent == "SELECT":
        words = question.lower().split()
        table_name = words[-1]

        result = schema_manager.select_all(table_name)
        print("Result:", result)

    # ================= UPDATE =================
    elif intent == "UPDATE":
        match = re.match(
            r"update (\w+) set (\w+) (\w+) where (\w+) (\w+)",
            question.lower()
        )
        if match:
            table, set_col, set_val, where_col, where_val = match.groups()
            query = schema_manager.update(table, set_col, set_val, where_col, where_val)
            print("Generated SQL:", query)
        else:
            print("Invalid UPDATE syntax.")

    # ================= DELETE =================
    elif intent == "DELETE":
        match = re.match(
            r"delete from (\w+) where (\w+) (\w+)",
            question.lower()
        )
        if match:
            table, where_col, where_val = match.groups()
            query = schema_manager.delete(table, where_col, where_val)
            print("Generated SQL:", query)
        else:
            print("Invalid DELETE syntax.")

    else:
        print("Unknown command.")

    print()
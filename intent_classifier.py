def detect_intent(question):
    q = question.lower()

    if q.startswith("create table"):
        return "CREATE"
    elif q.startswith("insert"):
        return "INSERT"
    elif q.startswith("update"):
        return "UPDATE"
    elif q.startswith("delete"):
        return "DELETE"
    else:
        return "SELECT"
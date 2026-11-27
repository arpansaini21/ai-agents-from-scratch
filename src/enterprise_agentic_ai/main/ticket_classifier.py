def classify_ticket(description: str) -> str:
    if not isinstance(description, str):
        raise TypeError("Description must be a string")

    if not description.strip():
        raise ValueError("Description cannot be empty")

    description = description.lower()

    rules = {
        "login": "Identity Team",
        "payment": "Payments Team",
        "network": "Infrastructure Team",
        "database": "Database Team",
    }

    for keyword, team in rules.items():
        if keyword in description:
            return team

    return "General Support"

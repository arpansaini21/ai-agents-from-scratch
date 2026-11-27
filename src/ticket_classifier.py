class ClassifyTicket:

    def __init__(self, description):
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        elif not description.strip():
            raise ValueError("Description cannot be empty")
        self.description = description.lower()

    rules = {
        "login": "Identity Team",
        "payment": "Payments Team",
        "network": "Infrastructure Team",
        "database": "Database Team",
    }

    def assign_team(self):
        for keyword, team in self.rules.items():
            if keyword in self.description:
                return team
        return "General Support"

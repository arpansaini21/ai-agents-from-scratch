class ClassifyTicket:

    def __init__(self, description):
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        elif not description.strip():
            raise ValueError("Description cannot be empty")
        self.description = description.lower()

    rules = {
        "login": "Identity Team",
        "security": "Security Team",
        "payment": "Payments Team",
        "network": "Infrastructure Team",
        "database": "Database Team",
        "email": "Messaging Team",
    }

    def assign_team(self):
        assign_team = list()
        for keyword, team in self.rules.items():
            if keyword in self.description:
                assign_team.append(team)

        if len(assign_team) == 1:
            return assign_team[0]
        elif len(assign_team) > 1:
            return "Define and document a routing priority"
        else:
            return "General Support"

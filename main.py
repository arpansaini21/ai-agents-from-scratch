from src.ticket_classifier import ClassifyTicket

def main():
    tickets = [
        "Customer cannot login",
        "Payment transaction failed",
        "Network connection unavailable",
        "Database connection timeout",
        "Unable to update profile",
    ]

    for ticket in tickets:
        team = ClassifyTicket(ticket)
        print(f"{ticket} -> {team.assign_team()}")


if __name__ == "__main__":
    main()

from src.ticket_classifier import ClassifyTicket

def main():
    tickets = [
        "Customer cannot login",
        "Security alert triggered",
        "Payment transaction failed",
        "Network connection unavailable",
        "Database connection timeout",
        "Email delivery failed",
        "Customer cannot LOGIN",
        "Customer cannot login after a database failure.",
        "Unable to update profile",
        "",
        "   ",
        None,
    ]

    for ticket in tickets:
        try:
            classifier = ClassifyTicket(ticket)
        except (TypeError, ValueError) as error:
            print(f"{ticket!r} -> {type(error).__name__}: {error}")
            continue

        print(f"{ticket!r} -> {classifier.assign_team()}")


if __name__ == "__main__":
    main()

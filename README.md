# AI Agents from Scratch

This repository explores how to build AI agents with Python, LangChain, and LangGraph through hands-on examples. The first example uses a rule-based support ticket classifier as a baseline for ticket routing.

## Rule-Based Ticket Routing

The classifier accepts a support ticket description and returns the name of the team responsible for handling it.

1. Normalize the description to lowercase for case-insensitive matching.
2. Check the description for predefined keywords in the order shown below.
3. Return the team associated with the first matching keyword. If no keyword matches, route the ticket to General Support.

| Keyword | Assigned team |
| --- | --- |
| `login` | Identity Team |
| `payment` | Payments Team |
| `network` | Infrastructure Team |
| `database` | Database Team |

## Run the Example

From the repository root, run the following command with Python 3.12 or later. The example requires no third-party packages.

```bash
python3 main.py
```

The script prints each sample ticket description alongside its assigned team.

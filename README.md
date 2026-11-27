# AI Agents from Scratch

This repository explores how to build AI agents with Python, LangChain, and LangGraph through hands-on examples. The first example uses a rule-based support ticket classifier as a baseline for ticket routing.

## Rule-Based Ticket Routing

The classifier accepts a support ticket description and returns the name of the team responsible for handling it.

1. Normalize the description to lowercase for case-insensitive matching.
2. Check the description for predefined keywords in the order shown below.
3. Return the team associated with the first matching keyword. If no keyword matches, route the ticket to General Support.

| Keyword      | Assigned team       |
| ------------ | ------------------- |
| `login`    | Identity Team       |
| `payment`  | Payments Team       |
| `network`  | Infrastructure Team |
| `database` | Database Team       |

## Limitation of Rule based engine and Agentic Future Solution

Consider this ticket description:

> Customer cannot login after a database failure.

The classifier assigns the ticket to the Identity Team because it checks `login` before `database`. The database failure may be the root cause, while the login issue may be a symptom.

| Limitation                            | Future solution                                            |
| ------------------------------------- | ---------------------------------------------------------- |
| Fixed keyword matching                | Semantic classification using large language models (LLMs) |
| Multiple matching teams               | Multi-label classification                                 |
| No root cause analysis                | Incident investigation agent                               |
| No access to historical incident data | Retrieval-augmented generation (RAG)                       |
| No confidence score                   | Calibrated classification and evaluation                   |
| Risk of incorrect assignment          | Human-in-the-loop approval                                 |
| No monitoring                         | Observability and tracing                                  |



## Interview Question 1



You are designing an AI ticket classification system that receives one million support tickets every day. Would you send every ticket to an LLM?



Consider the following dimensions before answering:

- Infrastructure and inference cost.
- Latency and throughput.
- Classification accuracy.
- Deterministic versus probabilistic routing.
- Failure handling and fallback mechanisms.
- Security and sensitive customer information.



At one million tickets per day, the average throughput is approximately 11.6 tickets per second, but peak throughput could be considerably higher.

A strong Staff Engineer should evaluate whether a hybrid architecture using deterministic rules, lightweight ML models, and LLMs for complex cases would deliver better results than an LLM-only solution.

Write your proposed architecture in five to ten sentences. I will evaluate your reasoning as an interviewer.

# Compliance Risk Checker for Emails: 
A langchain based project to flag the risk if any risk is detected in the email body being sent from the organization.
It is helpful in detecting risks/violations of any legal, business or internal guidelines.

## Project and env setup:

1. Clone the repo:
```git
git clone https://github.com/het-zignuts/Compliance-Risk-Checker-for-Emails.git 
```

2. Create python env:
```bash
python -m venv .venv
```

3. Activate the env:
```bash
source .venv/bin/activate
```

2. Inside the repo, install deps:
```bash
pip install requirements.txt
```

3. Run the CLI app:
```bash
python main.py
```

## Project Overview

An AI-powered Corporate Email Compliance Assistant that analyzes outgoing emails in real time to detect legal, business, or internal risks such as confidential info, pricing, NDAs, or inappropriate language. It provides actionable suggestions and allows saving structured risk reports for compliance tracking. Built with LangChain, ChatGroq, and Pydantic.

## Workflow
- User inputs the email body.
- LangChain pipeline processes it: prompt → ChatGroq LLM → Pydantic parser.
- Detected risks are printed with reason, severity, and suggested alternatives.
- Optionally, users can save analysis reports.
- Supports iterative evaluation for multiple emails in a session.


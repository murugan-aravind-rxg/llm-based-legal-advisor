# Start with imports 
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display
import concurrent.futures

load_dotenv(override=True)
open_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")


# Summarizes legal documents using AI
def llm_summarizer(document: str) -> str:
    response = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1").chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a corporate lawyer. Summarize the key points of legal documents clearly."},
            {"role": "user", "content": f"Summarize this document:\n\n{document}"}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content
	
	
# Identifies and analyzes legal risks in documents
def llm_evaluate_risks(document: str) -> str:
    response = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1").chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a corporate lawyer. Identify and explain legal risks in the following document."},
            {"role": "user", "content": f"Analyze the legal risks:\n\n{document}"}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content
	

# Classifies and tags legal clauses by category
def llm_tag_clauses(document: str) -> str:
    response = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1").chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a legal clause classifier. Tag each clause with relevant legal and compliance categories."},
            {"role": "user", "content": f"Classify and tag clauses in this document:\n\n{document}"}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content
	

# Organizes and formats multiple AI responses into a structured report
def aggregator(responses: list[str]) -> str:
    sections = {
        "summary": "[Section 1: Summary]",
        "risk": "[Section 2: Risk Analysis]",
        "clauses": "[Section 3: Clause Classification & Compliance Tags]"
    }

    ordered = {
        "summary": None,
        "risk": None,
        "clauses": None
    }

    for r in responses:
        content = r.lower()
        if any(keyword in content for keyword in ["summary", "[summary]"]):
            ordered["summary"] = r
        elif any(keyword in content for keyword in ["risk", "liability"]):
            ordered["risk"] = r
        else:
            ordered["clauses"] = r

    report_sections = [
        f"{sections[key]}\n{value.strip()}"
        for key, value in ordered.items() if value
    ]

    return "\n\n".join(report_sections)
	
	
# Orchestrates parallel execution of all legal analysis agents
def coordinator(document: str) -> str:
    """Dispatch document to agents and aggregate results"""
    agents = [llm_summarizer, llm_evaluate_risks, llm_tag_clauses]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(agent, document) for agent in agents]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]
    return aggregator(results)


def main():
    dummy_document = """
    This agreement is made between ABC Corp and XYZ Ltd. ...
    """
    final_report = coordinator(dummy_document)
    print(final_report)

if __name__ == "__main__":
    main()

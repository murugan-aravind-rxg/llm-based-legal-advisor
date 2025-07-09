# LLM Legal Advisor V1

A parallelized, AI-powered legal document analyzer that leverages large language models (LLMs) to provide instant, structured legal insights. This tool summarizes legal documents, identifies risks, and classifies clauses—all in one go.

## Features

- **Parallel Analysis:** Summarizes, evaluates risks, and tags legal clauses concurrently for fast results.
- **Natural Language Processing:** Uses state-of-the-art LLMs for clear, concise, and accurate legal analysis.
- **Customizable:** Easily adapt the input document or extend the analysis agents.

## Requirements

- Python 3.8+
- API keys for LLM providers (e.g., OpenAI, Groq)
- Internet connection

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/murugan-aravind-rxg/llm-legal-advisor.git
   cd llm-legal-advisor
   ```

2. **Install dependencies:**
   ```bash
   pip install openai python-dotenv ipython
   ```

3. **Set up API keys:**
   - Create a `.env` file in the project directory with the following content:
     ```
     OPENAI_API_KEY=your_openai_key_here
     GROQ_API_KEY=your_groq_key_here
     ```

## Usage

1. **Run the script:**
   ```bash
   python llm_legal_advisorV1.py
   ```

2. **What happens:**
   - The script analyzes a sample legal document (you can edit the `dummy_document` variable).
   - It prints a structured report with:
     - Section 1: Summary
     - Section 2: Risk Analysis
     - Section 3: Clause Classification & Compliance Tags

3. **Customizing:**
   - Replace the contents of `dummy_document` in the script with your own legal text to analyze other documents.

## How It Works

- The script defines three agent functions:
  - `llm_summarizer`: Summarizes the document.
  - `llm_evaluate_risks`: Identifies and explains legal risks.
  - `llm_tag_clauses`: Tags and classifies legal clauses.
- The `coordinator` function runs these agents in parallel and aggregates their results into a structured report.

## Example Output

Data source:
    https://www.sec.gov/edgar/search/#
    Bing search
    Yahoo finance news

Assessment report on company: Zebra Technologies (Zebra)

01_CollectCompanySecReports.ipynb 
- Collect 10K (2022) , 10Q (2023), 8K (2023).  So far this manual process, download PDF files.

02_EmbeddingFAISS.ipynb 
- Embed all SEC data into FAISS vector store.
- Save index files locally:
    faiss_index_8-K, faiss_index_10-K, faiss_index_10_Q

03_ToolsAgentIR.ipynb
- Read FAISS index files (SEC data) 
- Create and prepare tools: FAISS retriver (SEC specific tool), Bing search, Yahoo finance. 
- Create  agent ("zero-shot-react-description") using these tools. 
- Agent batch process prepared questions, answering questions in the list one by one:
    List of Questions:
    data = [
        {
            "category": "Financial Profile:",
            "inquiries": [
                "What is the trend in revenue growth over the past few years?",
                "How are the company's gross, operating, and net profit margins trending?",
                "What is the company's operating cash flow and free cash flow?",
                "What is the company's debt structure? (Long-term, short-term, interest rates)",
                "What are the major risks disclosed by the company?",
                "Who are the company's competitors, how does the company perform compared to its competitors in the industry?",
                "How does the company allocate profits to dividends or share buybacks?",
            ],
        },
        {
            "category": "Operational Performance:",
            "inquiries": [
                "Are there any noticeable fluctuations in sales figures?",
                "Have there been any significant changes in expenses or cost of goods sold?",
                "What is the cash conversion cycle evolving?",
                "How does the debt level compare to equity and assets?",
                "Are there any pending litigations, investigations, or regulatory issues disclosed?",
                "What investments is the company making in its business?",
            ],
        },
        {
            "category": "Market Position and Risk Factors:",
            "inquiries": [
                "Which metrics or KPIs are highlighted by the company as key measures of success?",
                "What are the major risks disclosed by the company?",
                "Are there any market trends or industry-specific challenges affecting the company?",
                "How might these impact the company's future operations and financial health?",
            ],
        },
    ]
- Save questions and answers in JSON file: qna_zbra_003.json


04_RiskAssessmentOnFindings.ipynb
- Read qna_zbra_003.json
- Use openai.ChatCompletion with following prompt to generate assessment report:
    company_name = 'Zebra Technologies (Zebra)'
    prompt_text = f"""
    Please generate an assessment report on {company_name} based on the following questions and answers in JSON:
    {data}
    and the assessment report should contain the following sections:
    1. Executive Summary
    2. Overview of Key Findings
    3. Summary of Risks Identified
    4. Overall ratings on the risk level you would give, between 0 and 9 (0 - no risk, 9 - highest risk)
    """
- Create the final report in .docx format: ./reports/qna_zbra_003_assessment.docx
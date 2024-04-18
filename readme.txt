Project1: 
Involves two main tasks:
1. **Speech Transcription and Summary**:
   - Transcribe a voice recording (BillGates_2010.wav) into text using code in a Jupyter Notebook.
   - Provide the transcribed text and a summary of the call.
2. **Custom Form Recognizer Model**:
   - Build and train a custom classifier using Document Intelligence (formerly Form Recognizer) from Azure AI services.
   - Data source: 5 arXiv papers.
   - Extract information including the name of the paper, author list, abstract, and number of pages.
   - Optionally, classify content pages versus reference pages.
For each task, includes:
- Code in Jupyter Notebook.
- Final results.
- Project files, code to call the model with sample data.


Project2:
Involves several tasks:
1. **Summarization of Large Document**: Utilize Arxiv papers in the fields of mathematics, artificial intelligence, 
    and physics as the data source. Gather five papers from each field and summarize their content.   
2. **Embedding**:
   a. Classify text: embedding can be use for slightly different purposes rather than semantic retrieval
   b. Utilize BBC news as the data source for this task.
3. **Build Question and Answer**: Create a system capable of generating questions and answers based on given text.


Project3:
Involves several tasks:
1. **Langchain Text Splitter / LLM Chain**: Develop a system for splitting text, possibly utilizing a Large Language Model (LLM) Chain approach.
2. **Langchain QnA**: Create a Question and Answer system using Arxiv papers as the data source.
3. **Langchain Agent and Tools**:
   a. Integrate Bing Search functionality into the system.
   b. Develop a tool capable of answering questions based on the data from a CSV file (e.g., the titanic.CSV file), 
   such as queries regarding the number of passengers with more than 2 siblings.
4. **Prompt Flow**:
   a. Implement a flow for utilizing Bing Search to ask questions.


Project4:
**Company Profile Risk Assessment**
Objective:
Research and assess the risk associated with a company profile using the following tools:
a. Web search
b. SEC reports (online)
Requirements:
1. **Sources**: Gather information from various sources including web search and SEC reports.
2. **Thought Process**: Document the methodology and thinking process behind the assessment.   
Deliverables:
Prepare an assessment report in Word format detailing the findings, sources used, and the reasoning behind the assessment.


Project5:
**AI-Assisted Ski Trip planning**
Business Objective
Current Process
Traditional Ski Trip Planning:
Researching ski resorts online or through travel agencies.
Manually comparing prices, amenities, and reviews.
Booking accommodations, transportation, lift tickets, and other activities separately.
Managing the itinerary and logistics individually.

Issues
Time consuming and human do make mistake. For example, due the complexities of managing the itinerary and logistics, a friend booked a flight which was one week off targeted dates!

Scope for this project : AI-Assisted Centralized Itinerary Management
Managing the itinerary and logistics in ski trip planning involves organizing various components:
Transportation, accommodations, 
lift tickets, activities, and schedules. 

AI can significantly aid in this area by centralizing itinerary management:
Consolidation of Information: AI can compile and manage various bookings and reservations into a single, easily accessible itinerary, reducing the hassle of juggling multiple confirmations and schedules.
Automated Updates: It can send timely reminders, updates, and suggestions for better planning and organization.

Document Comparison: Compare 2 documents and high light difference
**Ski trip requirements vs AI generated day to day Ski plan, comparison / evaluation**


Project6:
End to end deployment: PromptFlow

Demo: 
1. Ski trip planning generation
2. Ski trip requirements vs AI generated day to day Ski plan, comparison / evaluation

1. Web app deloyment environment: Azure App Service is seleted for this Demo
Web hosting can any of serviec which support this project implementation, such as, Streamlit could be another choice ...
2. Web App UI: Flask is selected for simplicity.
# Deploy a Python (Flask) web app to Azure App Service - Sample Application
This is the sample Flask application for the Azure Quickstart [Deploy a Python (Django or Flask) web app to Azure App Service]
(https://docs.microsoft.com/en-us/azure/app-service/quickstart-python). 
For instructions on how to create the Azure resources and deploy the application to Azure, refer to the Quickstart article.
1) this web app will work with the two deployed Prompt Flows described in the next section.
2) the web app use a simple form switch (Plan/Doc compare) to direct user to work with either 'Generate Ski trip plan',
   or 'Compare Ski tirp requiement vs generated detailed day to day ski plan'.
3) the back end deployed Flows will handle the user question/prompt accordingly
3. Prompt Flow is used for deployments of Generating Ski trip plan and comparison of ski trip requirments vs generated ski day to day plan
Use Azure Prompt Flow to deploy two flows:
1) Generating Ski trip plan
    - FAISS index file: faiss_index_travel
    - index file is uploaded in GitHub as pulic access file so that Prompt Flow's FAISS tool can access
2) comparison of ski trip requirments vs generated ski day to day plan
    - FAISS index file: faiss_index_doc_compare
    - index file is uploaded in GitHub as pulic access file so that Prompt Flow's FAISS tool can access
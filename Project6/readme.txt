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




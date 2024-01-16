Week #3 Assignments
===================

Assignment #1:
3.1_LangchainTextSplitter.ipynb - split pdf files and embedding to vector store - Azure AI Search

Assignment #2:
3.2_LangchainQnA.ipynb - QnA based on the vector store which supports vector search. 

Assignment #3:
3.3_LangchainAgentAndTools.ipynb - Created a Bing search using Langchain API.  Build an agent to work wiht local .csv file and answer questions based on .csv file

Assignment #4:
3.4_Promptflow.ipynb - Flow script
3.4.1_PromptflowDeploymentTest.ipynb - test deployment
    
Two flows are created:
    1) Use Langchain API to access Bing Search - the Bing Search resource is created in Azure Bing resource. this is done in Python
    2) Use Serp API to access Bing Search - creat a Serp connection, select bing.

Steps:
1. In VS Code, use script to create Flow, run batch test, visoulization, localhost ... can also use Pormpt flow extension (UI) to change / validate / add connection/ build local app
2. Once flow is tested locally, then we can use Azure web application, ML studio, to upload the flow
3. Once the flow is uploaded, we can do additional test and make sure the flow is working on cloud side. Note, the runtime needs to be created.
4. Deploy the flow and test on cloud side. Collect endpoint and key info.
5. On client side, creat a simple python app which uses the flow deployment endpoint and apik key to send https request to the flow, then check the response.
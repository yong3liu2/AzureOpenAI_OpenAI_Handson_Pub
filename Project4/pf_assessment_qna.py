from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need

# In Python tool you can do things like calling external services or
# pre/post processing of data, pretty much anything you want




import os
import openai
from dotenv import load_dotenv
# Set up Azure OpenAI
load_dotenv()

openai.api_type = "azure"

AZURE_OPENAI_API_VERSION = os.getenv("AAG_AZURE_OPENAI_API_VERSION")
openai.api_version = AZURE_OPENAI_API_VERSION

AZURE_OPENAI_API_KEY = os.getenv("AAG_AZURE_OPENAI_API_KEY").strip()
assert AZURE_OPENAI_API_KEY, "ERROR: Azure OpenAI Key is missing"
openai.api_key = AZURE_OPENAI_API_KEY

AZURE_OPENAI_ENDPOINT = os.getenv("AAG_AZURE_OPENAI_ENDPOINT", "").strip()
assert AZURE_OPENAI_ENDPOINT, "ERROR: Azure OpenAI Endpoint is missing"
openai.api_base = AZURE_OPENAI_ENDPOINT

# Deployment for Chat
# DEPLOYMENT_NAME_CHAT = os.getenv('DEPLOYMENT_NAME_CHAT')
DEPLOYMENT_NAME_CHAT = os.getenv('AAG_DEPLOYMENT_NAME_CHAT_16K')

# Deployment for embedding
DEPLOYMENT_NAME_EMBEDDING = os.getenv("AAG_DEPLOYMENT_NAME_EMBEDDING")
model: str = DEPLOYMENT_NAME_EMBEDDING

# Azure AI Search (Cognitive vector store)
vector_store_address: str = os.getenv("AAG_AZURE_SEARCH_SERVICE_ENDPOINT")
vector_store_password: str = os.getenv("AAG_AZURE_SEARCH_ADMIN_KEY")
# index_name: str = "langchain-vector-arxiv-physics"

# Deployment for embedding
BING_SUBSCRIPTION_KEY = os.getenv("BING_SUBSCRIPTION_KEY")

# %% [markdown]
# ## Langchain Set up

# %%
from langchain.chat_models import AzureChatOpenAI
# Azure OpenAI model
llm = AzureChatOpenAI(
    azure_deployment="gpt-35-turbo-16k",
    temperature=0,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    openai_api_type="azure",
    api_key=AZURE_OPENAI_API_KEY,
)

# %% [markdown]
# ## Prepare Tools for Agent

# %% [markdown]
# ### Tool: Bing Search

# %%
from langchain.utilities import BingSearchAPIWrapper
import os

os.environ["BING_SUBSCRIPTION_KEY"] = BING_SUBSCRIPTION_KEY
os.environ["BING_SEARCH_URL"] = "https://api.bing.microsoft.com/v7.0/search"

azure_bing_search = BingSearchAPIWrapper()

# Unit test
# azure_bing_search.run("When Sam Altman got fired?")

# %%
from langchain.agents import initialize_agent, AgentType
from langchain.agents import Tool

# Here is the tool define
azure_bing_search_01 = Tool(
    name="bing search for all",
    func=azure_bing_search.run, 
    description="search for any information that is available"
)

azure_bing_search_02 = Tool(
    name="bing search on current events",
    func=azure_bing_search.run,
    description="useful for when you need to answer questions about current events"
)


# %% [markdown]
# ### Tool: Faiss db retriever

# %%
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Get Azure OpenAI embedding
embeddings: OpenAIEmbeddings = OpenAIEmbeddings(
    deployment=model,
    model=model,
    chunk_size=1,
    openai_api_base=AZURE_OPENAI_ENDPOINT,
    openai_api_type="azure",
    api_key=AZURE_OPENAI_API_KEY,
)

import os

# Get the directory of the current script using __file__
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Now you can reference files relative to the script's directory
relative_file_path_8K = os.path.join(current_script_directory, "faiss_index_8-K")
faiss_db_8K = FAISS.load_local(relative_file_path_8K, embeddings)

relative_file_path_10Q = os.path.join(current_script_directory, "faiss_index_10-Q")
faiss_db = FAISS.load_local(relative_file_path_10Q, embeddings)

relative_file_path_10K = os.path.join(current_script_directory, "faiss_index_10-K")
faiss_db_10K = FAISS.load_local(relative_file_path_10K, embeddings)


# # Load local FAISS db which we created in earlier using embedding
# faiss_db_8K = FAISS.load_local("faiss_index_8-K", embeddings)
# # Set up the retriever we want to use, and then turn it into a retriever tool
# # faiss_retriever_8K = faiss_db_8K.as_retriever()

# # Load local FAISS db which we created in earlier using embedding
# faiss_db_10Q = FAISS.load_local("faiss_index_10-Q", embeddings)
# # Set up the retriever we want to use, and then turn it into a retriever tool
# # faiss_retriever_10Q = faiss_db_10Q.as_retriever()

# # Load local FAISS db which we created in earlier using embedding
# faiss_db_10K = FAISS.load_local("faiss_index_10-K", embeddings)
# # Set up the retriever we want to use, and then turn it into a retriever tool
# # faiss_retriever_10K = faiss_db_10K.as_retriever()

# %%
# Merge all FAISS db: 10Q, 10K, 8K
faiss_db.merge_from(faiss_db_10K)
faiss_db.merge_from(faiss_db_8K)

# Set up the retriever we want to use, and then turn it into a retriever tool
faiss_retriever = faiss_db.as_retriever()

# %%
from langchain.agents.agent_toolkits import create_retriever_tool

# Tool define
faiss_retriever_all = create_retriever_tool(
    faiss_retriever,
    "SEC data search",
    "This tool is help looking for information about a company using its all U.S. Securities and Exchange Commission (SEC) filing reports, like 10-K, 10-Q, 8-K ...",
)

# %% [markdown]
# ### Tools - it seems that the same tool with different descriptions leads different results.

# %%
# Tools

tools_04 = [
    faiss_retriever_all,
    azure_bing_search_01
]

# %% [markdown]
# ## Q&A: Risk Assessment

# %% [markdown]
# ## Agent equipped with tools to answer all the questions

# %% [markdown]
# #### List of questions

# %%
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

# %%
agent004 = initialize_agent(
    tools_04,
    llm,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True,
)

# %%
# agent004.run("Who are the Zebra's competitors, how does the company perform compared to its competitors in the industry?")

# %% [markdown]
# #### QnA for PF

# %%
# Define an empty list to store the output
# user_input = "Who are the Zebra's competitors, how does the company perform compared to its competitors in the industry?"

# Prompt to make sure the question refers to the right company
def build_question_prompt(company_name, question):
    prompt_text = f"Please answer the following question. Note that inside the question, 'the company' refers to {company_name}. Here is the question: {question}. \
        NOTE: if you can find the answer, please provide the source."
    return prompt_text


# Choose an agent who can perform the best for a job given
def agent_in_action(agent_on_job, question_prompt):
    result = agent_on_job.run(question_prompt)
    return result

# QnA
company_name = 'Zebra Technologies'
agent_on_duty = agent004
# question_prompt = build_question_prompt(company_name, user_input)
# print(f"=> {question_prompt}")
# answer = agent_in_action(agent_on_duty, question_prompt)
# print(f"Answer: {answer}")

# main()
@tool
def assessment_qna(input: str) -> str:
    # QnA
    question_prompt = build_question_prompt(company_name, input)
    print(f"=> {question_prompt}")
    answer = agent_in_action(agent_on_duty, question_prompt)
    print(f"Answer: {answer}")
    # return input

    return answer
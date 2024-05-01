=========================================================================================================
Revolutionizing Compliance: OpenAI RAG Solution for Ontario Building Code - Exploring Part 7 Section 7.4
=========================================================================================================


[Data source]
- https://www.ontario.ca/page/ontarios-building-code
- OBC PDF file - Ontario Building Code - Exploring Part 7 Section 7.4

[Architecture]
- RAG

Components:
- LLM: OpenAI (models: Embedding, ChatCompletion)
- LangChain framework, rag-chain with/out source, Tools, Agents (openai-tools-agent, react-agent) 
- Vector store: FAISS
- Web: Streamlit?
- BigQuery: cache DB. Collect Q&A pairs, good or bad. Good ones will be used for repeating queries; bad ones will be used for feedback and review by human.

[Implementation]
Embedding:
01_OBC_Embedding_FAISS.ipynb
- LangChain PDF loader loads "Ontario Building Code - Exploring Part 7 Section 7.4" PDF file. Chunk: natural page for now.
- Embedding chunks into FAISS vector store.
- Save index files locally: faiss_index_obc.

Q&A: information retrieveal (IR) with different technics 

RAG chain with/out reference source page(s):
02_OBC_QnA_chain_w_source.ipynb
- Load FAISS vector store index: faiss_index_obc
- Create a retriever for faiss_index_obc
- Create rag chain with/out reference source 
- Use "rag chain with/out reference source" to query and answering


Tools and Agents:
03_OBC_QnA_tool_agent.ipynb
OpenAI tool agent:
- Create a retriever for faiss_index_obc: faiss_retriever_obc
- Create tools based on faiss_retriever_obc: faiss_retriever_obc_tool
- Create "openai_tools_agent" agent using the tools. 
- Create "openai_tools_agent" agent executer
- Use "OpenAI tools agent executer" query and answering

ReAct agent:
- Create a retriever for faiss_index_obc: faiss_retriever_obc
- Create tools based on faiss_retriever_obc: faiss_retriever_obc_tool
- Create "react_agent" agent using the tools. 
- Create "react_agent" agent executer
- Use "ReAct agent executer" query and answering


[Questions]

plumbing question 1
///////////////////
question 1：
The size of horizontal sanitary drainage pipe required for a plumbing system with one 4-piece washroom, and how much of the slope shall be selected。
solution：
step 1:
Determine each Fixture’s Hydraulic Load (unit is “Fixture Units” (FUs)), based on table 7.4.9.3:
•	flush tank Toilet: A standard toilet has 4 fixture units.
•	Lavatory: A typical bathroom sink has 1.5 fixture units.
•	Bathtub: A standard bathtub has 1.5 fixture units.
•	Shower: A shower head has 1.5 fixture units.
step 2:
Calculate Total Fixture Units:
total FU=4+1.5+1.5+1.5=8.5 FU
step 3:
Select Pipe Size , based on table 7.4.10.8:
8.5FU, can use 3” horizontal sanitary drainage pipe with the slope of 1 in 50.

******************************************************************

question 2：
The size of horizontal sanitary drainage pipe required for a plumbing system with four 4-piece washrooms, and how much of the slope shall be selected。
solution：
step 1:
Determine each Fixture’s Hydraulic Load (unit is “Fixture Units” (FUs)), based on table 7.4.9.3:
•	flush tank Toilet: A standard toilet has 4 fixture units.
•	Lavatory: A typical bathroom sink has 1.5 fixture units.
•	Bathtub: A standard bathtub has 1.5 fixture units.
•	Shower: A shower head has 1.5 fixture units.
step 2:
Calculate Total Fixture Units:
total FU for one 4-piece washroom = 4+1.5+1.5+1.5=8.5 FU
total FU for four 4-piece washrooms =4* 8.5=34 FU
step 3:
Select Pipe Size , based on table 7.4.10.8:
34 FU, can use 3” horizontal sanitary drainage pipe with the slope of 1 in 25, or use 4” horizontal sanitary drainage pipe with the slope of 1 in 100.


plumbing question 2- cleanouts
//////////////////////////////
question 1:
how big interval shall between two cleanouts on a 4” horizontal sanitary drainage pipe?
section 7.4.7.2 Size and Spacing of Cleanouts (1) (b)
answer: 15m

****************************************************************
question 2:
how big interval shall between two cleanouts on a 6” horizontal sanitary drainage pipe?
section 7.4.7.2 Size and Spacing of Cleanouts (1) (c)
answer: 30m

**************************************************************
question 3:
how many cleanouts shall be placed on a 6” horizontal sanitary drainage pipe with two 90-degree direction changes?
section 7.4.7.1 （5）Cleanouts for Drainage Systems. & section 7.4.7.2 Size and Spacing of Cleanouts (1) (c)
answer: every 30m and at each 90-degree direction change.


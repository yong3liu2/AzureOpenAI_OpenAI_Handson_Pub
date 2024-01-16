# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need

import os
from dotenv import load_dotenv
# Set up Azure OpenAI
load_dotenv()

# Bing subscription key
BING_SUBSCRIPTION_KEY = os.getenv("BING_SUBSCRIPTION_KEY")

os.environ["BING_SUBSCRIPTION_KEY"] = BING_SUBSCRIPTION_KEY
os.environ["BING_SEARCH_URL"] = "https://api.bing.microsoft.com/v7.0/search"

from langchain.utilities import BingSearchAPIWrapper
search = BingSearchAPIWrapper()

def bing_search(user_input):
    # # search.run("python")
    # search.run("When Sam Altman got fired?")
    return search.run(user_input)

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str) -> str:
    search_result = bing_search(input1)
    # return 'hello ' + input1 + search_result
    return 'Bing search result: ' + search_result


import os

# -------------------
import urllib.request
import json
import os
import ssl


AAG_PROMPT_FLOW_ENDPOINT_BING_SEARCH = (
    "https://yongpromptflow-bingsearch.eastus.inference.ml.azure.com/score"
)
# Replace this with the primary/secondary key or AMLToken for the endpoint
AAG_PROMPT_FLOW_ENDPOINT_BING_SEARCH_KEY = "lfZfe1etNqXJLVVy7uDdCj66CLYIo..."


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if (
        allowed
        and not os.environ.get("PYTHONHTTPSVERIFY", "")
        and getattr(ssl, "_create_unverified_context", None)
    ):
        ssl._create_default_https_context = ssl._create_unverified_context


allowSelfSignedHttps(
    True
)  # this line is needed if you use self-signed certificate in your scoring service.


def bing_search_endpoint(user_question):
    # Request data goes here
    # The example below assumes JSON formatting which may be updated
    # depending on the format your endpoint expects.
    # More information can be found here:
    # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
    data = {"question": user_question}
    # data = {"questiont":"Sam Altman join Microsoft and return back to OpenAI as of 11/22/2023?"}
    # data = {"question":"Who is China's president as of 11/22/2023?"}

    body = str.encode(json.dumps(data))

    url = AAG_PROMPT_FLOW_ENDPOINT_BING_SEARCH
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = AAG_PROMPT_FLOW_ENDPOINT_BING_SEARCH_KEY
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {
        "Content-Type": "application/json",
        "Authorization": ("Bearer " + api_key),
        "azureml-model-deployment": "pf-bingsearch-deployment",
    }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        # print(result)
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", "ignore"))


# result = bing_search_endpoint("Who is China's president as of 11/22/2023?")



def ski_travel_plan(user_question):
    # Request data goes here
    # The example below assumes JSON formatting which may be updated
    # depending on the format your endpoint expects.
    # More information can be found here:
    # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
    data = {"question": user_question}
    body = str.encode(json.dumps(data))

    url = 'https://azureml-travel-plan.eastus.inference.ml.azure.com/score'
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = 'Ez9d4lboTPkqQM14DNDJnvVs7rviP...'
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'azureml-travel-plan-1' }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))


def ski_travel_doc_compare(user_question):
    # Request data goes here
    # The example below assumes JSON formatting which may be updated
    # depending on the format your endpoint expects.
    # More information can be found here:
    # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
    data = {"question": user_question}
    body = str.encode(json.dumps(data))

    url = 'https://azureml-doc.eastus.inference.ml.azure.com/score'
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = 'mfcCNHvRmGsbVw8VLBxyH2deJ3poD...'
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'azureml-doc-1' }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)


from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    # user_input = request.form['user_input']
    # print(user_input)
    # # Retrieve the switch value from the form
    # selected_switch = request.form['switch']
    # print("selected_switch", selected_switch)

    user_input = request.form.get('user_input')
    selected_switch = request.form.get('switch')

    print(f"Received User Input: {user_input}")
    print(f"Received Switch Value: {selected_switch}")

    if(selected_switch == 'Plan'):
        # Ski trip planning
        byte_string = ski_travel_plan(user_input)
    else:
        # Ski trip doc comparison
        byte_string = ski_travel_doc_compare(user_input)

    # Decode the byte string to a regular string
    regular_string = byte_string.decode('utf-8')

    # Extract JSON data from the regular string
    bot_response_json = json.loads(regular_string)

    print(bot_response_json)

    return bot_response_json


if __name__ == '__main__':
    app.run(debug=True)

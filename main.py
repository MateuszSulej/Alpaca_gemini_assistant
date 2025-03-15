
from response_from_gemini import *
from call_function_from_string import *

alpaca = alpaca_demo

while True:
    prompt = input("Enter your prompt:")
    if prompt == "exit":
        break
    response = response_from_gemini(get_data_from_file("alpaca_demo.py") + prompt + "Analyze the user's input and determine the appropriate function from the provided set to accomplish their request. Output only the function name and its arguments in the format: function_name,argument1, argument2, .... No additional text or syntax.")
    print(response)
    call_function_from_string(alpaca_demo, response)






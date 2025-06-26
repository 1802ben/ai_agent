import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from system_prompt import system_prompt
from available_functions import available_functions
from call_function import call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )

    verbose = False
    if len(sys.argv) <2:
        print("No input")
        sys.exit(1)
    if len(sys.argv) > 2:
        if sys.argv[2] == "--verbose":
            verbose = True

    prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    for i in range(20):
        response = client.models.generate_content(
            model = "gemini-2.0-flash-001",
            contents = messages,
            config=config,
        )
        
        for candidate in response.candidates:
            messages.append(candidate.content)

        if response.function_calls:
            for function_call_part in response.function_calls:
                
                function_call_result = call_function(function_call_part)
                messages.append(function_call_result)

                if function_call_result.parts[0].function_response.response is None:
                    raise Exception("An Error occured")
                elif verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
        else:
            print("Final response:")
            print(response.text)
            break


        if len(sys.argv) > 2:
            if verbose:
                print(f"User prompt: {prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


main()
from openai import OpenAI

client = OpenAI()


def list_assistants():
    try:
        # Fetch the list of assistants
        response = client.beta.assistants.list()

        if response.data:
            print("List of Assistants:")
            for assistants in response.data:
                print(f"- ID: {assistants.id}, Name: {assistants.name}")
        else:
            print("No assistants found.")
    except Exception as e:
        print(f"An error occurred: {e}")

"""
### Example code to use with above functions

from openai_exploration.assistant_usage import create_thread, check_status, list_assistants, get_response

list_assistants()

"""
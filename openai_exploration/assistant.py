from openai import OpenAI
import time
#openai.api_key = "YOUR_API_KEY"

client = OpenAI()

#assistant_id = "YOUR_ASSISTANT_ID"

#list_assistants doesn't work yet. Getting error with openai.beta.assistant call (no function available)
def list_assistants():
    try:
        # Fetch the list of assistants
        response = client.beta.assistant.list()

        if response.data:
            print("List of Assistants:")
            for assistants in response.data:
                print(f"- ID: {assistants.id}, Name: {assistants.name}")
        else:
            print("No assistants found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_thread(assistant_id, prompt):
    # Create a thread
    thread = client.beta.threads.create()
    my_thread_id = thread.id

    # Create a message
    message = client.beta.threads.messages.create(
        thread_id=my_thread_id,
        role="user",
        content=prompt
    )

    # Run
    run = client.beta.threads.runs.create(
        thread_id=my_thread_id,
        assistant_id=assistant_id,
    )
    return run.id, thread.id

def check_status(run_id, thread_id):
    run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id,
    )
    return run.status

def get_response(thread_id):
    return client.beta.threads.messages.list(thread_id)

"""
## Example code to use with above functions

my_run_id, my_thread_id = create_thread(assistant_id, "Your Prompt Here")

status = check_status(my_run_id, my_thread_id)

while status != "completed":
    status = check_status(my_run_id, my_thread_id)
    time.sleep(2)

response = openai.beta.threads.messages.list(thread_id=my_thread_id)

if response.data:
    print(response.data[0].content[0].text.value)
"""
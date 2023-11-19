import openai
import time
openai.api_key = "YOUR_API_KEY"

assistant_id = "YOUR_ASSISTANT_ID"

def create_thread(assistant_id, prompt):
    # Create a thread
    thread = openai.beta.threads.create()
    my_thread_id = thread.id

    # Create a message
    message = openai.beta.threads.messages.create(
        thread_id=my_thread_id,
        role="user",
        content=prompt
    )

    # Run
    run = openai.beta.threads.runs.create(
        thread_id=my_thread_id,
        assistant_id=assistant_id,
    )
    return run.id, thread.id

def check_status(run_id, thread_id):
    run = openai.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id,
    )
    return run.status

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
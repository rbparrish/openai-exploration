from openai import OpenAI

client = OpenAI()


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
### Example code to use with above functions

from openai_exploration.assistant_usage import create_thread, check_status, list_assistants, get_response
import json

## Submit query and create thread
my_run_id, my_thread_id = create_thread(assistant_id, "Your Prompt Here")

## Get response once status is complete

status = check_status(my_run_id, my_thread_id)

while status != "completed":
    status = check_status(my_run_id, my_thread_id)
    time.sleep(2)

full_response_object = get_response(my_thread_id)

## Read Response

# Simple text response
full_response_object.data[0].content[0].text.value

#dictionary of full response
json.loads(full_response_object.model_dump_json(indent=2, exclude_unset=True))

"""
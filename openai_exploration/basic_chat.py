import json
from openai import OpenAI

client = OpenAI()


# def show_json(obj):
#    display(json.loads(obj.model_dump_json()))

# user_content_example = "Compose a poem that explains my love for Maria, my wife, whom is a fan of art and life."
def create_poem(user_content):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a poetic assistant, skilled in explaining love with creative flair. Compose a poem "
                        "based on the input of the user."},
            {"role": "user",
             "content": user_content}
        ]
    )

    return completion.choices[0].message

# print(completion.choices[0].message)

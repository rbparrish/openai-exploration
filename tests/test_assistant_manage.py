import openai
from openai_exploration.assistant_manage import get_assistants


def test_get_assistants_real_api_call():

    # Call the function
    assistants_list = get_assistants().data

    # Assert that the function returns at least two assistants
    assert len(assistants_list) > 1, "No response to function"

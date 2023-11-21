from openai_exploration.assistant_usage import create_thread, check_status, get_response


assistant_id = "asst_3mVmeNeegxopjNWPb4thdvuw"

def test_create_thread():

    # Call the function
    my_run_id, my_thread_id = create_thread(assistant_id,
                     "Can you tell me what types of information I should include in my PRD?")

    # Assert two strings are returned
    assert isinstance(my_run_id, str) and isinstance(my_thread_id, str), "two strings were not returned"

def test_get_status():

    # Get prerequisite information
    my_run_id, my_thread_id = create_thread(assistant_id,
                                            "Can you tell me what types of information I should include in my PRD?")

    # Call the function
    status = check_status(my_run_id, my_thread_id)

    assert status == 'completed' or status == 'in_progress' or status == 'queued', "unexpected status response"

def test_get_response():

    # Get full response object
    my_thread_id = 'thread_nPv6m6dtrmQrosXmXFFlOxQg'
    full_response = get_response(my_thread_id)

    # Pull out primary text response
    simple_text_response = full_response.data[0].content[0].text.value

    # Check if response is as expected
    assert simple_text_response[:40] == "Sure, a comprehensive Product Requiremen", "response not as expected"

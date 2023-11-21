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

    assert status == 'completed' or status == 'in_progress', "unexpected status response"

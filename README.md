# Openai Exploration
Personal exploration of &amp; helpful tools for using OpenAI

Python version & packages to install to use this project:
- Versions last tested 3.10.13 + pytest 7.4.3
- OpenAI CLI: pip install openai-cli
- Testing Framework: pip install pytest

The following use cases are implemented:
- Single request and response from ChatGPT (see [basic_chat.py](openai_exploration/basic_chat.py))
- Usage of an already created assistant (see [assistant_usage.py](openai_exploration/assistant_usage.py))
- Managing assistants (see [assistant_manage.py](openai_exploration/assistant_manage.py))

Use cases I'm planning to explore next:
- Using a custom GPT from python
- How to use a custom GPT from an assistant

Basic implementation coming soon:
- Creating and managing a list of assistants
- Move usage examples of how to leverage the code into separate documentation
- Implement basic test cases

Example Usage in Python Console for Code found in the bottom of each file

Example Usage CLI for test suite
- `pytest` will run through full set of tests
- `pytest -k test_get_response will run through a single file of tests

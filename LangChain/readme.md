# Famous Person Search Readme

This repository contains code that integrates with the OpenAI API to perform a famous person search based on user input. It utilizes the `langchain` library, which provides convenient abstractions for working with language models and conversation memories.

## Prerequisites
- Python 3.x
- OpenAI API key

## Setup
1. Clone this repository to your local machine.
2. Install the required dependencies by running the following command:
3. Set your OpenAI API key as an environment variable named `OPENAI_API_KEY`. Replace `openai_key` in the `constant.py` file with your actual API key.

## Usage
1. Run the code using the following command:
2. Access the application by opening the provided URL in your web browser.
3. The application will display a title and a text input field where you can enter the topic you want to search.
4. After entering the input, the application will retrieve information about the famous person and display it.
5. The retrieved information will be stored in a conversation buffer memory for future reference.
6. You can expand the "Person Name" section to view the conversation history for the famous person.
7. You can also expand the "Major Events" section to view the major events that occurred on the person's date of birth.

## Customization
If you want to modify the code or add additional functionality, you can refer to the following sections:

### Prompt Templates
- The `PromptTemplate` class is used to define the prompts for each input. You can modify the templates in the code to customize the prompts according to your requirements.

### Conversation Buffer Memories
- The `ConversationBufferMemory` class is used to store and retrieve conversation history. You can create additional instances of this class and modify the code to store different types of information.

### Language Models
- The code uses the `OpenAI` class from the `langchain.llms` module to interact with the OpenAI language model. You can modify the parameters of the `OpenAI` class to change the behavior of the language model.

### Sequential Chain
- The `SequentialChain` class from the `langchain.chains` module is used to chain multiple conversation steps together. You can modify the chain configuration by adding or removing `LLMChain` instances in the `chains` list.

## License
This code is licensed under the [MIT License](LICENSE).

Feel free to explore, modify, and use this code to integrate with the OpenAI API and perform famous person searches in your own applications.


# Import AzureChatOpenAI class from langchain_openai package
# This class helps us connect LangChain with Azure OpenAI chat models
from langchain_openai import AzureChatOpenAI

# Import load_dotenv function
# This function loads variables from .env file
from dotenv import load_dotenv

# Import os module
# os.getenv() is used to read environment variables
import os


# Load all variables from .env file into environment
# After this, Python can access them using os.getenv()
load_dotenv()


# Creating an OBJECT of AzureChatOpenAI class
# "model" is the object/instance
# AzureChatOpenAI(...) is the constructor call
model = AzureChatOpenAI(

    # Azure OpenAI endpoint URL
    # os.getenv() reads value from .env file
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),

    # Azure OpenAI API key
    # Used for authentication/security
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),

    # Azure OpenAI API version
    # Azure requires API version for requests
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),

    # Azure deployment name
    # This tells Azure which deployed model to use
    azure_deployment=os.getenv("AZURE_OPENAI_COMPLETION_DEPLOYMENT")
)


# invoke() sends prompt/question to the model
# "What is the capital of India?" is the USER INPUT/PROMPT
# Result is stored inside "result" variable
result = model.invoke("What is the capital of India?")


# Print complete AIMessage object
# This contains:
# - content
# - metadata
# - token usage
# - model info
print(result)


# Print only actual response text/content
# .content extracts only the generated answer
print(result.content)
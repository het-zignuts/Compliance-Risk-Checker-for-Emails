from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import PydanticOutputParser
from response_schema import RiskAnalysisResponse
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv() # load the env variables from .env file

MODEL_NAME=os.getenv("MODEL") # get the LLM Model name

with open("prompt_template.txt", "r") as file: # read the prompt template
    template=file.read()
parser=PydanticOutputParser(pydantic_object=RiskAnalysisResponse) # get the pydantic parser and instantiate it for the RisAnalysisResponse Schema.
prompt=PromptTemplate(input_variables=["email_body"], partial_variables={"format_instructions": parser.get_format_instructions()}, template=template) # generate the prompt by substituting the vars inside the template
llm=ChatGroq(model=MODEL_NAME, api_key=os.getenv("GROQ_API_KEY"), temperature=0) # get the LLM instance with the API Key and temperature setting
 # temperature = 0 here implies determinism.

chain = prompt | llm | parser
# Build a langchain of prompt, llm and parser
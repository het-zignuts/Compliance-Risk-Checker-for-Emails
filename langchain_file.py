from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import PydanticOutputParser
from response_schema import RiskAnalysisResponse
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

MODEL_NAME=os.getenv("MODEL")

with open("prompt_template.txt", "r") as file:
    template=file.read()
parser=PydanticOutputParser(pydantic_object=RiskAnalysisResponse)
prompt=PromptTemplate(input_variables=["email_body"], partial_variables={"format_instructions": parser.get_format_instructions()}, template=template)
llm=ChatGroq(model=MODEL_NAME, api_key=os.getenv("GROQ_API_KEY"), temperature=0)
 
chain = prompt | llm | parser
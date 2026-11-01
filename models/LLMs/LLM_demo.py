from langchain_openai import OpenAI # this is used to import openai library that will help to connect to it

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct') # model name mention kiye ki kaunsa model use krna hai

result = llm.invoke("What is the capital of India") # model use kiye 

print(result)
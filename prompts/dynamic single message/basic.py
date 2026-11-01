from langchain_core.prompts import PromptTemplate ## yeh import krte hasi
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# detailed way
## iss trah prompt template bnate hai 
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name':'nitish'}) ## iss trah fill krte hai

result = model.invoke(prompt)

print(result.content)
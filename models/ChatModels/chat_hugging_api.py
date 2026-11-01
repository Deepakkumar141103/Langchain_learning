from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
# hugging face k case me hi yeh niche wala line use krte hai,
# jab hame chat krna hota hai tab as this line help 
# # ChatHuggingFace wraps that loaded model so we can use it
# through LangChain's chat-model interface. 
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)
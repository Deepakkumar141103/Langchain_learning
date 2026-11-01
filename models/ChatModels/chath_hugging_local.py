from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# hugging face pipeline is used for dwonloading model so niche wala code is used for dwnoading model 
llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
# ab yeh sawal a skta hai jaise embedding wale me locally dowload kiye to isme kyu to huggingface ke text
# model ko aese hi download kiya jata hai waise download embedding model ko kiya jta hai 
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)
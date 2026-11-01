from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf', # yhn btaye kii uss folder me kaunsa file extension wale ko upload krna hai 
    loader_cls=PyPDFLoader # upload krne k liye kis uploader use krenge 
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
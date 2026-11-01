from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)
# dekho isko hum log normal text pr bhi lga skte hai means suppose docs me ek string rht to 
# splitter.split_text(doc) woh variable pass kr doo ho gya 

# now yhn chunk_overlap ka mtlb jitna part m break kiya to usme kuch common bhi rkh skte hai isme jyda chances hai kuch semantic meaning reh jaye 
result = splitter.split_documents(docs)
# now result aaya woh ek list hoga jisme har ek element me doo part ek content and ek metadata
print(result[0].page_content)
from dotenv import load_dotenv 
import os 
from pinecone import Pinecone 
from pinecone import ServerlessSpec 

from langchain_pinecone import PineconeVectorStore
from src.helper import download_hugging_face_embeddings, filter_to_minimal_docs, load_pdf, text_split




load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

exteracted_data = load_pdf(data="data/")
minimal_docs = filter_to_minimal_docs(exteracted_data)

text_chunks = text_split(minimal_docs)

embeddings = download_hugging_face_embeddings()

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key = pinecone_api_key)



index_name = "medical-bot"  # change if desired

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

index = pc.Index(index_name)

docserach = PineconeVectorStore.from_documents(documents=text_chunks, 
                                               embedding = 
                                               embeddings, index_name = index_name)

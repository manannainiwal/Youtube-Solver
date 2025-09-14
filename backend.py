import  os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain

def comp_process(apikey, url, question):

    #initialize llm
    OPENAI_API_KEY  = apikey
    os.environ[OPENAI_API_KEY] = apikey
    llm = ChatOpenAI(temperature = 0, openai_api_key = OPENAI_API_KEY)

    loader = YoutubeLoader.from_youtube_url(url)
    result = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
    chunks = text_splitter.split_documents(result)

    embeddings = OpenAIEmbeddings(openai_api_key = apikey)
    db = FAISS.from_documents(chunks, embedding=embeddings)
    docs = db.similarity_search(query=question)

    read_chain = load_qa_chain(llm = llm)
    answer = read_chain.invoke({"input_documents" : docs, "question" : question})

    return answer["output_text"]

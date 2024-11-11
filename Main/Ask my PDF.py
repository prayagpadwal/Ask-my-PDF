import os
import streamlit as st
import textract
from transformers import GPT2TokenizerFast
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI

# Set your OpenAI API key here
OPENAI_API_KEY = "Put your Open AI API key here"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # Address potential OpenMP library conflict

def load_pdf(file_data):
    # Process the PDF from uploaded data
    with open("temp_file.pdf", "wb") as f:
        f.write(file_data)
    text = textract.process("temp_file.pdf")
    return text.decode('utf-8')

def prepare_chat_model(text):
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    def count_tokens(text: str) -> int:
        return len(tokenizer.encode(text))
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512, chunk_overlap=24, length_function=count_tokens
    )
    chunks = text_splitter.create_documents([text])
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = FAISS.from_documents(chunks, embeddings)
    return ConversationalRetrievalChain.from_llm(OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.1, openai_api_key=OPENAI_API_KEY), db.as_retriever())

def add_to_chat(question, answer):
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    st.session_state.chat_history.append({'question': question, 'answer': answer})

# Streamlit interface
st.title('Ask my PDF')
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    text = load_pdf(uploaded_file.getvalue())
    qa_chain = prepare_chat_model(text)
    st.success('PDF Loaded. Start asking questions!')
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

user_input = st.text_input("Ask questions about the PDF:", key="question")
if user_input:
    if 'chat_history' in st.session_state:
        result = qa_chain({"question": user_input, "chat_history": st.session_state.chat_history})
        st.session_state.chat_history.append((user_input, result['answer']))
        st.text_area("Chat History", value='\n\n'.join(f"Q: {q}\nA: {a}" for q, a in st.session_state.chat_history), height=600, disabled=True)
    else:
        result = qa_chain({"question": user_input})
        st.session_state.chat_history = [(user_input, result['answer'])]
        st.text_area("Chat History", value=f"Q: {user_input}\nA: {result['answer']}", height=600, disabled=True)

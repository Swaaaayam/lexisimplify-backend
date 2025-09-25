import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in environment variables")

# Initialize Groq model
llm = ChatGroq(
    model="llama-3.1-70b-versatile",   # ✅ updated model
    api_key=GROQ_API_KEY,
    temperature=0.5
)

simplify_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a legal assistant in India. Explain legal text in plain, simple language."),
    ("human", "{clause}")
])

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a legal assistant. Use the given clause as context."),
    ("human", "Context: {context}\n\nQuestion: {question}")
])

def simplify_text(text: str) -> str:
    chain = simplify_prompt | llm
    return chain.invoke({"clause": text}).content

def answer_question(question: str, context: str = "") -> str:
    chain = qa_prompt | llm
    return chain.invoke({"context": context, "question": question}).content

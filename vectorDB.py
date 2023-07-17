from vectordb import Memory
from PyPDF2 import PdfReader
import streamlit as st

st.title("Vector Database Testing")
memory = Memory(chunking_strategy={'mode':'sliding_window', 'window_size': 128, 'overlap': 16})

doc_reader = PdfReader("file_directory\sample1.pdf")
text2=" "
for page in doc_reader.pages:
    text2 += page.extract_text()

metadata2 = {"title": "Introduction to Artificial Intelligence", "url": "https://example.com/introduction-to-artificial-intelligence"}

memory.save(text2, metadata2)

#query = "What is the relationship between AI and machine learning?" #Single question #memory spikes for a while 
 #user input question #memory increses till the query is executed
#n=int(input("enter number of questions: "))

#for i in range(n):
#    query=input("Enter your query: " )   #memory increases and remains constant for all the questions
#    results = memory.search(query, top_n=1)
    
#    results=results[0]
 #   print(type(results))
  #  results=results['chunk']

   # print(results)
query=st.text_input("Enter your query: ")
results = memory.search(query, top_n=1)
results=results[0]
results=results['chunk']

st.write("Response: ",results)

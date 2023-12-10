import streamlit as st
from annotated_text import annotated_text

st.title("Langchain Chunk Visualizer")
st.write("Inspired by https://www.chunkviz.com/ by Greg Kamradt")
#Split the input text into reasonable chunks to be embedded, one after another, with some overlap.
from langchain.text_splitter import CharacterTextSplitter

# Input text from https://medium.com/@cronozzz.rocks/splitting-large-documents-text-splitters-langchain-7c7bfa899267
long_text = """By Vinamra Sulgante
In the realm of data processing and text manipulation, there’s a quiet hero that often doesn’t get the recognition it deserves — the text splitter. While it might not have a flashy costume or a catchy theme song, it plays a crucial role in dissecting, organizing, and understanding textual data. In this comprehensive guide, we will embark on a journey into the fascinating world of text splitters, exploring their various techniques, applications, and how they can turn raw text into a structured treasure trove.
Understanding the Need for Text Splitters
Text is an integral part of our digital world. We encounter it everywhere, from articles and reports to code snippets and social media updates. Often, we need to break down lengthy text into smaller, more manageable pieces. This is where text splitters come into play. They are the tools that dissect text into chunks, making it easier to work with, analyze, and extract meaningful information.
But why do we need text splitters? Imagine you have a massive document, and you want to analyze it for sentiment, extract keywords, or count specific occurrences. Doing this manually would be an arduous task. Text splitters automate this process, allowing you to break down text into smaller units, such as sentences, words, or even custom-defined tokens.
The Anatomy of Text Splitters
At a fundamental level, text splitters operate along two axes:
How the text is split: This refers to the method or strategy used to break the text into smaller chunks. It could involve splitting at specific characters, words, sentences, or even custom-defined tokens.
How the chunk size is measured: This relates to the criteria used to determine when a chunk is complete. It might involve counting characters, words, tokens, or some custom-defined metric.
These axes give us a versatile toolkit to customize text splitting according to our specific requirements.
Getting Started with Text Splitters
Let’s begin our exploration of text splitters by understanding how to get started with them. The default and often recommended text splitter is the Recursive Character Text Splitter. This splitter takes a list of characters and employs a layered approach to text splitting.
Here are some key parameters that you can customize when using the Recursive Character Text Splitter:
Character Set Customization: You can define which characters should be used for splitting. By default, it operates on a list of characters including “\\n\\n”, “\\n”, and space.
Length Function: This determines how the length of chunks is calculated. You can opt for the default character count or use a custom function, especially useful for languages with complex scripts.
Chunk Size Control: The chunk_size parameter allows you to specify the maximum size of your chunks, ensuring they are as granular or broad as needed.
Chunk Overlap: To maintain context between chunks, you can set the chunk_overlap parameter, ensuring information isn't lost at chunk boundaries.
Metadata Inclusion: Enabling add_start_index includes the starting position of each chunk within the original document in the metadata.
Now that we’ve laid the foundation, let’s explore the specific types of text splitters and their unique features.
Character Text Splitter: Slicing Like a Pro
The Character Text Splitter is often the first tool in a developer’s arsenal. It performs a simple yet crucial task — splitting a string of text into individual characters. It’s like sending your text through a letter factory, where each character gets its own tiny conveyor belt.
This splitter is not limited by language or content type. It doesn’t care if you’re dealing with English, Chinese, or even emoji-laden text. It treats every character equally and fairly.
The key takeaway is that the Character Text Splitter is the most granular of all text splitters, breaking text down to its smallest building blocks.
Humor Break: Unlike some text splitters, the Character Text Splitter doesn’t discriminate against punctuation marks. They all get their moment in the spotlight!"""

text_for_analysis = st.text_area("Input Text", long_text, height=400)
st.write(f'Length: {len(text_for_analysis)} characters.')

chunk_size = st.slider("Chunk Size", 0, 1000, 250)

# Splitting up the text into smaller chunks for indexing
text_splitter = CharacterTextSplitter(        
    separator = " ",
    chunk_size = chunk_size,
    chunk_overlap  = 0, #striding over the text
    length_function = len,
    is_separator_regex = False,
)
my_list = text_splitter.split_text(text_for_analysis)

text = []

for i in range(len(my_list)):
    text.append((f"{my_list[i]}", str(i+1)))

annotated_text(text)

annotated_text((f"      TOTAL CHUNKS:  {len(text)}",f"{len(text)}"))

st.write(text)
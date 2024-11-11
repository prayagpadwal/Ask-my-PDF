# Ask my PDF

Welcome to "Ask my PDF", a Streamlit-powered application that transforms how you interact with PDF documents. This tool allows users to upload any PDF and engage in an interactive dialogue where they can ask questions directly about the content of the document. The app utilizes state-of-the-art Natural Language Processing (NLP) to parse and understand text, enabling it to respond with contextually relevant answers.

## Features

- **PDF Upload**: Upload PDF documents and extract their content for querying.
- **Interactive Chat Interface**: Ask questions about the uploaded document and receive answers as if you are chatting with an expert on the document's content.
- **Session State Management**: Maintains the context of the conversation, allowing for a seamless interaction experience throughout the session.

## Technology Stack

- **Streamlit**: Manages the web interface and user interactions.
- **Textract**: Extracts text from PDF files.
- **Transformers (GPT-2 Tokenizer)**: Processes the extracted text to prepare it for embedding.
- **OpenAI Embeddings**: Generates embeddings from the processed text to facilitate contextual understanding.
- **FAISS**: Handles efficient similarity search in large databases of embeddings.
- **OpenAI's GPT-3.5**: Provides the conversational model that generates responses based on the embedded text and user queries.

## Getting Started

### Prerequisites

Before you can run "Ask my PDF", ensure you have the following installed:
- Python 3.8+
- pip

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/prayagpadwal/ask-my-pdf.git
cd ask-my-pdf
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

To start the application, run:

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your web browser to start using the app. Upload a PDF file and begin asking questions about its content directly through the chat interface.

## Contributing

Contributions to "Ask my PDF" are welcome! Whether it's bug fixes, feature requests, or improvements to the documentation, please feel free to make a pull request or open an issue.

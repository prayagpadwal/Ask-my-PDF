# Ask my PDF

"Ask my PDF" is a Streamlit application designed to enable interactive conversations with the content of PDF documents. Leveraging advanced NLP technologies, this app parses text from PDFs allowing users to ask questions and receive contextual answers instantly.

## Features

- **PDF Upload**: Users can easily upload and extract text from PDF files for analysis.
- **Interactive Chat**: Engage with the PDF through a dynamic chat interface that understands and responds to user inquiries based on the document's content.
- **Session State Management**: Maintains chat continuity, providing a seamless conversational experience with the document.

![snippet](https://github.com/user-attachments/assets/e429cd24-a256-467f-b088-7aa2a8d8e88e)


## Technology Stack

The application integrates several advanced technologies:

- **Streamlit**: For building and hosting the web interface.
- **Textract**: Extracts text from PDFs.
- **Transformers (GPT-2 Tokenizer)**: Facilitates text processing for NLP tasks.
- **LangChain**: Manages NLP workflows, including embeddings and conversational chains.
- **FAISS**: Provides efficient similarity search for handling large text databases.
- **OpenAI API (GPT-3.5)**: Empowers the app with cutting-edge AI conversational capabilities.

## Installation

### Prerequisites

You need Python 3.8 or higher installed on your machine to run "Ask my PDF". Additionally, an OpenAI API key is required to access AI models which may incur costs depending on your usage level.

### Setting Up Your Environment

Clone the repository and install the necessary Python packages:

```bash
git clone https://github.com/prayagpadwal/ask-my-pdf.git
cd ask-my-pdf
pip install -r requirements.txt
```

### Dependencies

Ensure all required libraries are installed by running:

```bash
pip install streamlit textract transformers langchain faiss-cpu openai
```

Note: `FAISS` requires a CPU or GPU installation depending on your system capabilities; the above command installs `FAISS` for CPU.

### OpenAI API Key

The application uses OpenAI's GPT-3.5, which is a paid service. You will need to [sign up for OpenAI](https://platform.openai.com/signup), set up billing, and obtain an API key. The costs will vary based on the number of tokens processed by your interactions with the app.

## Usage

To run the application:

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser to interact with the application. Upload a PDF and start asking questions about its content directly through the chat interface.

## Contributing

We welcome contributions to improve the app, whether it's new features, bug fixes, or documentation. Please feel free to fork the repository, make changes, and submit a pull request.

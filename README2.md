# Machine Learning Literature Search Engine

## Prerequisites

Before you begin, ensure you have Python 3.8+ installed on your machine. You will also need the following packages:

- FastAPI
- Uvicorn
- Whoosh
- Jinja2

Install all required libraries using:

```
pip install fastapi uvicorn whoosh jinja2
```

```
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
pip install -r requirements.txt
```

## File Structure
- main.py: The FastAPI application code
- Index/: Directory where Whoosh indexes are stored after processing.
- templates/: HTML templates for the web interface.
- Processed/: Folder containing processed text files ready for indexing.
- Raw/: Folder containing raw text files.

## Running the Application
To run the application, go to the project directory and run:

```
uvicorn main:app --reload
```
## Indexing Documents
Ensure that your documents are processed from the raw folder to the processed folder, then indexed into the Index folder. Run the whoosh script in the  'Code' folder.

## Searching Documents
Once the application is running, you can perform searches through the web interface accessible at:

```
http://127.0.0.1:8000/
```

## Testing
To test the application, ensure you follow these steps:

- Place some sample documents in the raw folder.
- Process the documents as described in the documentation.
- Start the server and use the web interface to perform searches.

Contact
For support or questions, contact [Stef] at [ec23947@qmul.ac.uk].

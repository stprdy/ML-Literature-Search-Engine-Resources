import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from whoosh.qparser import QueryParser
from whoosh.index import open_dir

app = FastAPI()

INDEX_ROOT = r'C:\Users\steph\OneDrive\Documents\GitHub\ML-Literature-Search-Engine-Resources'

templates = Jinja2Templates(directory=os.path.join(INDEX_ROOT, 'templates'))

def get_index_directories(root_dir):
    for dirpath, dirnames, _ in os.walk(root_dir):
        if 'Index' in dirnames:
            yield os.path.join(dirpath, 'Index')

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, query: str = Form(...)):
    results = perform_search(query)
    print(results)  
    return templates.TemplateResponse("results.html", {"request": request, "query": query, "results": results})

def perform_search(search_query):
    results = []
    for index_dir in get_index_directories(INDEX_ROOT):
        try:
            ix = open_dir(index_dir)
            with ix.searcher() as searcher:
                query = QueryParser("content", ix.schema).parse(search_query)
                whoosh_results = searcher.search(query, limit=10)
                results.extend([{
                    'title': hit['title'],  # Assuming 'title' field exists in the index
                    'score': hit.score, 
                    'snippet': hit.highlights("content", top=3),  # Assuming 'content' field exists in the index
                    'path': hit['path']  # Assuming 'path' field exists in the index
                } for hit in whoosh_results])
        except Exception as e:
            print(f"Error accessing index at {index_dir}: {e}")
    results = sorted(results, key=lambda x: x['score'], reverse=True)[:10]
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

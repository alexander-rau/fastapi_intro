from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()


template1 = Jinja2Templates(directory = "../templates")

@app.get("/{book}/{id}", response_class = HTMLResponse)
async def read(request: Request, book: str, id: int):
   return template1.TemplateResponse("index.html", {"request": request, "book": book, "id": id})

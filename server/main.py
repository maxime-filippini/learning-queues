from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/assets", StaticFiles(directory="../client/dist/assets"), name="assets")
templates = Jinja2Templates("../client/dist")


@app.get("/health")
def health_check():
    return JSONResponse(content={"message": "All good"}, status_code=200)


@app.get("/", response_class=HTMLResponse)
def index(req: Request):
    return templates.TemplateResponse(request=req, name="index.html")

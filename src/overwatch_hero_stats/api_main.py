from fastapi import FastAPI
from . import __version__



app = FastAPI(
    title="Hero API",
    description="This is the hero API.",
    version=__version__,
)

@app.get("/", tags=["Hero API"], description="Health Check")
def health_check():
    return {"Message": "we up"}

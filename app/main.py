from fastapi import FastAPI
from routers import company,job
from database import Base,engine
from models import job as job_model, company as company_model
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
print(engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(company.router)
app.include_router(job.router)

@app.get("/")
def read_root():
    return {"Hello":"world"}

@app.get("/about")
def read_about():
    return {"about": "This is about page"}


@app.get("/contact")
def read_contact():
    return {"about": "This is about contact"}

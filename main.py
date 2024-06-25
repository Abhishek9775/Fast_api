from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Job(BaseModel):
    company_name: str
    job_title: str
    job_description: str
    experience: int
    package_upto: float
    skill: List[str]
    location: str
    job_type: str
    email: str

jobs = []

@app.post("/job/")
def create_job(job: Job):
    jobs.append(job)
    return job

@app.get("/")
def get_all_jobs():
    return jobs

@app.get("/jobs/{job_id}")
def read_job(job_id: int):
    if job_id >= len(jobs) or job_id < 0:
        raise HTTPException(status_code=404, detail="Job not found")
    return jobs[job_id]

def get_1():
    return {'mango': '20', 'apple': 30}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

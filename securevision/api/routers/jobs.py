from fastapi import APIRouter
router = APIRouter()

# Minimal job status stub; in production we'd query DB Job table or Celery backend
@router.get("/{job_id}")
def get_job(job_id: int):
    return {"id": job_id, "status": "queued"}

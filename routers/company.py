from fastapi import APIRouter
from Schemas.company import CompanyCreate,CompanyUpdate

router = APIRouter(prefix="/company",tags=["company"])
Company = []

@router.post("/")
def create_company(company:CompanyCreate):
    company.append(company)
    return company

@router.get("/{company_id}")
def get_all_company(company_id: int):
    return {"company_id":company_id}

@router.get("/{company_id}")
def get_company(company_id: int):
    return Company[company_id]


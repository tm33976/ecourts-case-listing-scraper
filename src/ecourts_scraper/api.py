from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from datetime import datetime
from .scraper import ECourtsScraper

app = FastAPI(title="eCourts Scraper API")
s = ECourtsScraper()

class SearchResponse(BaseModel):
    found: bool
    when: str
    date: str
    serial_number: str | None = None
    court_name: str | None = None

@app.get("/search", response_model=SearchResponse)
def api_search(cnr: str | None = Query(None), case_type: str | None = Query(None),
               case_number: str | None = Query(None), year: str | None = Query(None),
               when: str = Query("today")):
    res = s.find_case_listing(cnr=cnr, case_type=case_type, case_number=case_number, year=year, when=when)
    if not res:
        raise HTTPException(status_code=404, detail="Case not found")
    return res

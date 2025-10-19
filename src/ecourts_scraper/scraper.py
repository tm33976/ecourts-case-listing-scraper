import requests, re, os
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from .utils import save_json, ensure_data_dir

BASE_LISTING_URL = "https://services.ecourts.gov.in/ecourtindia_v6/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

class ECourtsScraper:
    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update(HEADERS)

    def _format_date(self, target: datetime) -> str:
        return target.strftime("%d-%m-%Y")

    def find_case_listing(self, *, cnr: Optional[str] = None, case_type: Optional[str] = None,
                          case_number: Optional[str] = None, year: Optional[str] = None,
                          when: str = "today") -> Dict[str, Any]:
        """
        Mock HTML search (for testing). Returns a simulated listing result if the pattern matches.
        """
        if when not in ("today", "tomorrow"):
            raise ValueError("when must be 'today' or 'tomorrow'")

        target_date = datetime.now() + (timedelta(days=1) if when == "tomorrow" else timedelta(days=0))

    
        text = "<html><body><div>Serial No: 42 | Civil Case 123 / 2025 | District Court Delhi</div></body></html>"
        soup = BeautifulSoup(text, "html.parser")

        search_patterns = []
        if cnr:
            search_patterns.append(re.escape(cnr.strip()))
        elif case_type and case_number and year:
          
            p = (
                f"{re.escape(case_type.strip())}\\s*(?:Case\\s*)?"
                f"{re.escape(case_number.strip())}\\s*[/|\\-]?\\s*{re.escape(year.strip())}"
            )
            search_patterns.append(p)

        text_all = soup.get_text()
        for pat in search_patterns:
            m = re.search(pat, text_all, flags=re.IGNORECASE)
            if m:
                return {
                    "found": True,
                    "when": when,
                    "date": target_date.strftime("%Y-%m-%d"),
                    "serial_number": "42",
                    "court_name": "District Court Delhi",
                }

        return {"found": False, "when": when, "date": target_date.strftime("%Y-%m-%d")}

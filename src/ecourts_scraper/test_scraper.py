from .scraper import ECourtsScraper
from .utils import ensure_data_dir, save_json
import os, json

def run_tests():
    s = ECourtsScraper()

    res = s.find_case_listing(case_type="Civil", case_number="123", year="2025")
    assert res["found"], "Case should be found in mock HTML"
    assert "District Court Delhi" in res["court_name"]

    d = ensure_data_dir()
    assert os.path.isdir(d), "Data dir should exist"

    test_file = save_json({"ok": True}, "test.json")
    with open(test_file) as f:
        data = json.load(f)
    assert data["ok"] is True

    print("✅ All tests passed successfully!")

if __name__ == "__main__":
    run_tests()

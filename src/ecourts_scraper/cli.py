import typer
from datetime import datetime
from .scraper import ECourtsScraper
from .utils import save_json

app = typer.Typer(help="eCourts Scraper CLI — fetches mock or live court listings.")

@app.command("search")
def search(
    cnr: str = typer.Option(None, help="CNR number of the case"),
    case_type: str = typer.Option(None, help="Type of the case (e.g. Civil, Criminal)"),
    case_number: str = typer.Option(None, help="Case number"),
    year: str = typer.Option(None, help="Case year (e.g. 2023)"),
    today: bool = typer.Option(False, "--today", help="Check if the case is listed today"),
    tomorrow: bool = typer.Option(False, "--tomorrow", help="Check if the case is listed tomorrow"),
):
    """
    Search for a case listing (mock mode).  
    If found, displays serial number and court name, and saves output as JSON.
    """
    s = ECourtsScraper()

    # Determine which days to check
    targets = []
    if today:
        targets.append("today")
    if tomorrow:
        targets.append("tomorrow")
    if not targets:
        targets = ["today"]  # default

    results = []
    for t in targets:
        typer.echo(f"🔎 Checking case listing for: {t}")
        res = s.find_case_listing(
            cnr=cnr, case_type=case_type, case_number=case_number, year=year, when=t
        )
        if res["found"]:
            typer.echo(
                f"✅ Found! Serial No: {res['serial_number']} | Court: {res['court_name']}"
            )
        else:
            typer.echo(f"❌ Not listed for {t}.")
        results.append(res)

    # Save results to file
    fname = f"search_results_{int(datetime.now().timestamp())}.json"
    save_path = save_json({"results": results}, fname)
    typer.echo(f"💾 Results saved to: {save_path}")


if __name__ == "__main__":
    app()

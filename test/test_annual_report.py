from annual_report.annual_report import AnnualReport
from pathlib import Path

def test_annual_report():

    site_test = "https:deepgram.com"
    annual_report = AnnualReport(site_test)

    # test site web 
    assert site_test == annual_report.site

    annual_report.scraper_with_google()

    # print("result: ", annual_report.result)

    assert len(annual_report.result)!=0

    annual_report.save_as_csv("pdfdrive_annual_report")

    assert Path("pdfdrive_annual_report.csv").exists()


    annual_report.save_as_csv("pdfdrive_annual_report")

    assert Path("pdfdrive_annual_report.json").exists()



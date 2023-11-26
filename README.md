## Annual Report

The purpose of this project is to extract all the available annual report files from a particular website. The project aims to retrieve these documents systematically and comprehensively, ensuring that no report is missed. The extracted reports will be stored in a structured format for further analysis and processing. The final output will be a complete and accurate collection of all the annual reports available on the website.


## How to Install

```
pip install annual_report

```

## How to use


```python

import annual_report


 annual_report = AnnualReport("https://pdfdrive.com")
 annual_report.scraper_with_google()
 annual_report.save_with_json("./result")
 annual_report.save_with_csv("./result")

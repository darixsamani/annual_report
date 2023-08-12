## Annual Report
    the objectives of this project, is to retrieve all annual report documents on a given website


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

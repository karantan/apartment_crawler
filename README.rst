Apartment Crawler
=================
Apartment Crawler is a scrapy web crawler that is already configured for
several sites like `nepremicnine.net` and `bolha.com`.

Features
--------
- SQLAlchemy
- Sentry
- Mailgun

Installation
------------
Install by running:
    `make`

Add `local_settings.py` which will overwrite `settings.py` and then add
starting URLs to `crawler_settings.py`.

Run crowlers e.g.:
	`cd apartment_crawler`
	`scrapy crawl nepremicnine`

Contribute
----------
- Issue Tracker: github.com/karantan/apartment_crawler/issues
- Source Code: github.com/karantan/apartment_crawler
Support
-------
If you are having issues, please let us know.

License
-------
The project is licensed under the MIT License.

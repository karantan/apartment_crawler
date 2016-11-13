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
    ``make``

Add ``local_settings.py`` which will overwrite ``settings.py`` and then add
starting URLs to ``crawler_settings.py`` e.g.:

.. code-block:: python

	bolha_urls = [
	    'http://www.bolha.com/nepremicnine/stanovanja?reType=2-sobno%7C%7C1.5-sobno%7C%7C2.5-sobno&viewType=30&location=Osrednjeslovenska%2FDom%C5%BEale%2F%7C%7COsrednjeslovenska%2FKamnik%2F%7C%7COsrednjeslovenska%2FTrzin%2F%7C%7COsrednjeslovenska%2FVrhnika%2F%7C%7COsrednjeslovenska%2FBrezovica+pri+Ljubljani%2F%7C%7COsrednjeslovenska%2FLjubljana%2F%7C%7COsrednjeslovenska%2FMenge%C5%A1%2F&hasImages=Oglasi+s+fotografijami',
	]

	nepremicnine_urls = [
	    'https://www.nepremicnine.net/QUERY-PARAMS.../1/',
	    'https://www.nepremicnine.net/QUERY-PARAMS.../2/',
	    'https://www.nepremicnine.net/QUERY-PARAMS.../3/',
	    'https://www.nepremicnine.net/QUERY-PARAMS.../4/',
	]

	salomon_urls = []


Run crowlers e.g.:
	``cd apartment_crawler``

	``scrapy crawl nepremicnine``

Run crowlers in production mode:

``scrapy crawl nepremicnine -a mode=production``

Atm the only difference is that production mode will try to send emails.

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

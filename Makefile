# convenience makefile to run buildout and tests

.DEFAULT_GOAL := build


build:
	virtualenv -p python3 env
	@env/bin/pip install -r requirements.txt
	@if [ -f develop_requirements.txt ]; then env/bin/pip install -r develop_requirements.txt; fi;

clean:
	@rm -rf env

run:
	@env/bin/scrapy crawl apartment

sort:
	@env/bin/isort -rc apartment


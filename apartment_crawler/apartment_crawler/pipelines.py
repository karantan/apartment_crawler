# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from apartment_crawler import settings
from apartment_crawler.models import Apartment
from apartment_crawler.models import create_tables
from apartment_crawler.models import db_connect
from sqlalchemy.orm import sessionmaker
from mako.template import Template

import requests
import logging

logger = logging.getLogger()


def send_message(link):
    email_template = Template(filename='apartment_crawler/email.mako')
    resp = requests.post(
        'https://api.mailgun.net/v3/{}/messages'.format(settings.MAILGUN_DOMAIN),
        auth=('api', settings.MAILGUN_API_KEY),
        data={
            'from': 'Apartment Crawler <mailgun@{}>'.format(
                settings.MAILGUN_DOMAIN),
            'to': settings.RECEIVERS,
            'subject': 'New apartment found',
            'text': 'Testing some Mailgun awesomness!',
            'html': email_template.render(link=link),
        })
    try:
        resp.raise_for_status()
    except Exception as e:
        logger.error(e)


class ApartmentCrawlerPipeline(object):
    def __init__(self):
        """Initializes database connection and sessionmaker."""
        engine = db_connect()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save apartment in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        apartment_exists = session.query(Apartment).filter_by(
            url=item['url'])

        if not apartment_exists.count():
            apartment = Apartment(**item)
            try:
                session.add(apartment)
                session.commit()
            except Exception as e:
                logger.error(e)
                session.rollback()
                raise
            finally:
                session.close()

        if hasattr(spider, 'mode') and spider.mode == 'production':
            send_message(item['url'])

        return item

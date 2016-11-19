from apartment_crawler.spiders import nepremicnine

import mock
import unittest


# from responses import fake_response_from_file


class TestNepremicnine(unittest.TestCase):

    def setUp(self):
        self.spider = nepremicnine.NepremicnineSpider()

    # def _test_item_results(self, results, expected_length):
    #     count = 0
    #     permalinks = set()
    #     for item in results:
    #         self.assertIsNotNone(item['content'])
    #         self.assertIsNotNone(item['title'])
    #     self.assertEqual(count, expected_length)

    # def test_parse(self):
    #     results = self.spider.parse(fake_response_from_file('osdir/sample.html'))
    #     self._test_item_results(results, 10)

    def test_filter_by_size(self):
        pass

    @mock.patch('apartment_crawler.spiders.nepremicnine.filters')
    def test_filter_by_more_info_by_obcina_true(self, filters):
        data = {
            'obcina': ['Ljubljana'],
            'regija': '*',
            'vrsta': '*',
        }
        filters.__getitem__.side_effect = lambda key: data[key]

        more_info = (
            'Posredovanje: Prodaja | Vrsta: Stanovanje | '
            'Regija: LJ-mesto | Upravna enota: Lj. Moste-Polje | '
            'Občina: Ljubljana'
        )
        res = self.spider.filter_by_more_info(more_info)
        self.assertTrue(res)

    @mock.patch('apartment_crawler.spiders.nepremicnine.filters')
    def test_filter_by_more_info_by_obcina_false(self, filters):
        data = {
            'obcina': ['Maribor'],
            'regija': '*',
            'vrsta': '*',
        }
        filters.__getitem__.side_effect = lambda key: data[key]

        more_info = (
            'Posredovanje: Prodaja | Vrsta: Stanovanje | '
            'Regija: LJ-mesto | Upravna enota: Lj. Moste-Polje | '
            'Občina: Ljubljana'
        )
        res = self.spider.filter_by_more_info(more_info)
        self.assertFalse(res)

    @mock.patch('apartment_crawler.spiders.nepremicnine.filters')
    def test_filter_by_more_info_by_regija_true(self, filters):
        data = {
            'obcina': '*',
            'regija': ['LJ-mesto'],
            'vrsta': '*',
        }
        filters.__getitem__.side_effect = lambda key: data[key]

        more_info = (
            'Posredovanje: Prodaja | Vrsta: Stanovanje | '
            'Regija: LJ-mesto | Upravna enota: Lj. Moste-Polje | '
            'Občina: Ljubljana'
        )
        res = self.spider.filter_by_more_info(more_info)
        self.assertTrue(res)

    @mock.patch('apartment_crawler.spiders.nepremicnine.filters')
    def test_filter_by_more_info_by_regija_false(self, filters):
        data = {
            'obcina': '*',
            'regija': ['MB-mesto'],
            'vrsta': '*',
        }
        filters.__getitem__.side_effect = lambda key: data[key]

        more_info = (
            'Posredovanje: Prodaja | Vrsta: Stanovanje | '
            'Regija: LJ-mesto | Upravna enota: Lj. Moste-Polje | '
            'Občina: Ljubljana'
        )
        res = self.spider.filter_by_more_info(more_info)
        self.assertFalse(res)

    @mock.patch('apartment_crawler.spiders.nepremicnine.filters')
    def test_filter_by_more_info_by_vrsta_true(self, filters):
        data = {
            'obcina': '*',
            'regija': ['*'],
            'vrsta': ['Stanovanje'],
        }
        filters.__getitem__.side_effect = lambda key: data[key]

        more_info = (
            'Posredovanje: Prodaja | Vrsta: Stanovanje | '
            'Regija: LJ-mesto | Upravna enota: Lj. Moste-Polje | '
            'Občina: Ljubljana'
        )
        res = self.spider.filter_by_more_info(more_info)
        self.assertTrue(res)

    @mock.patch('apartment_crawler.spiders.nepremicnine.filters')
    def test_filter_by_more_info_by_vrsta_false(self, filters):
        data = {
            'obcina': '*',
            'regija': ['*'],
            'vrsta': ['Hiša'],
        }
        filters.__getitem__.side_effect = lambda key: data[key]

        more_info = (
            'Posredovanje: Prodaja | Vrsta: Stanovanje | '
            'Regija: LJ-mesto | Upravna enota: Lj. Moste-Polje | '
            'Občina: Ljubljana'
        )
        res = self.spider.filter_by_more_info(more_info)
        self.assertFalse(res)

    @mock.patch('apartment_crawler.spiders.nepremicnine.filters')
    def test_filter_by_size_in_range(self, filters):
        data = {
            'min_velikost': 50,
            'max_velikost': 75,
        }
        filters.__getitem__.side_effect = lambda key: data[key]

        apartment_title = (
            'Prodaja, počitniški objekt, apartma: AMBROŽ POD KRVAVCEM, 58.2 m2'
        )
        res = self.spider.filter_by_size(apartment_title)
        self.assertTrue(res)

    @mock.patch('apartment_crawler.spiders.nepremicnine.filters')
    def test_filter_by_size_not_in_range(self, filters):
        data = {
            'min_velikost': 50,
            'max_velikost': 75,
        }
        filters.__getitem__.side_effect = lambda key: data[key]

        apartment_title = (
            'Prodaja, počitniški objekt, apartma: AMBROŽ POD KRVAVCEM, 78.2 m2'
        )
        res = self.spider.filter_by_size(apartment_title)
        self.assertFalse(res)

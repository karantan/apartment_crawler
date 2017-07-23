bolha_urls = [
    'http://www.bolha.com/nepremicnine/stanovanja/?reType=2-sobno%7C%7C2.5-sobno%7C%7C3-sobno%7C%7C3.5-sobno&viewType=30&location=Osrednjeslovenska%2FLjubljana%2FBe%C5%BEigrad%2F%7C%7COsrednjeslovenska%2FLjubljana%2FDravlje%2F%7C%7COsrednjeslovenska%2FLjubljana%2FMoste%2F%7C%7COsrednjeslovenska%2FLjubljana%2FPolje%2F%7C%7COsrednjeslovenska%2FLjubljana%2FRudnik%2F%7C%7COsrednjeslovenska%2FLjubljana%2FTrnovo%2F%7C%7COsrednjeslovenska%2FLjubljana%2F%C5%A0i%C5%A1ka%2F%7C%7COsrednjeslovenska%2FLjubljana%2F%C4%8Crnu%C4%8De%2F%7C%7COsrednjeslovenska%2FLjubljana%2FCenter%2F%7C%7COsrednjeslovenska%2FLjubljana%2FJar%C5%A1e%2F%7C%7COsrednjeslovenska%2FLjubljana%2FOstalo%2F%7C%7COsrednjeslovenska%2FLjubljana%2FRo%C5%BEnik%2F%7C%7COsrednjeslovenska%2FLjubljana%2F%C5%A0marna+gora%2F&priceSortField=75940%7C178505&producedYear=2012+in+ve%C4%8D%7C%7C2010+do+2011%7C%7C2000+do+2009%7C%7C1990+do+1999&adTypeH=00_Prodam%2F',
]

nepremicnine_urls = [
    'https://www.nepremicnine.net/oglasi-prodaja/ljubljana-mesto/stanovanje/3-sobno/cena-od-140000-do-180000-eur/',
]

nepremicnine_filters = {
    'min_price': 50000,
    'max_price': 180000,
    'obcina': ['Ljubljana'],
    'regija': ['*'],  # wild card - it matches everything
    'vrsta': ['Stanovanje'],
    'min_velikost': 55,
    'max_velikost': 75,
}

salomon_urls = []

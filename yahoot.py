from bs4 import BeautifulSoup, SoupStrainer
from requests import Session
from json import loads


class yahoot(object):
    def __init__(self):
        self.strainer = SoupStrainer(attrs={"type":"application/json"})
        self.session = Session()

    def search(
        self,
        from_station: str,
        to_station: str: str
    ) -> dict:
        url = f"https://transit.yahoo.co.jp/search/print?from={from_station}&to={to_station}&y=2023&m=02&d=17&hh=17&m1=4&m2=4&type=1&ticket=ic&expkind=1&userpass=1&ws=3&s=0&al=1&shin=1&ex=1&hb=1&lb=1&sr=1&no=1"
        response = self.session.get(url).text
        soup = BeautifulSoup(response, "lxml", parse_only=self.strainer)
        return loads(soup.find("script").text)
        
if __name__ == "__main__":
    print(yahoot().search("東京", "新宿"))





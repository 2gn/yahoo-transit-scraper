from requests import get as req_get
from pyquery import PyQuery as pq
import urllib.parse
from datetime import datetime


def build_yahoo_transit_url(
    from_station,
    to_station,
    year=None,
    month=None,
    day=None,
    hour=None,
    minute=None
):
    base_url = "https://transit.yahoo.co.jp/search/print"

    # Use current time if not provided
    now = datetime.now()
    year = year or now.year
    month = month or now.month
    day = day or now.day
    hour = hour or now.hour
    minute = minute or now.minute

    params = {
        "from": from_station,
        "to": to_station,
        "fromgid": "",
        "togid": "",
        "flatlon": "",
        "tlatlon": "",
        "y": year,
        "m": f"{month:02}",
        "d": f"{day:02}",
        "hh": f"{hour:02}",
        "m1": str(minute // 10),
        "m2": str(minute % 10),
        "type": "1",
        "ticket": "ic",
        "expkind": "1",
        "userpass": "1",
        "ws": "3",
        "s": "0",
        "al": "1",
        "shin": "1",
        "ex": "1",
        "hb": "1",
        "lb": "1",
        "sr": "1",
        "no": "1"
    }

    query_string = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    return f"{base_url}?{query_string}"

def parse_transit_summary(html):
    """
    Extract departure time, arrival time, and IC fare from Yahoo Transit HTML.

    Args:
        html (str): HTML content of the transit result.

    Returns:
        dict: Dictionary with 'departure', 'arrival', and 'price'.
    """
    doc = pq(html)

    try:
        departure = doc(".time span").eq(0).text().split("発")[0].strip()
        arrival = doc(".time .mark").eq(0).text().strip("着")
        price = doc(".fare .mark").eq(0).text().strip("円")
        return {
            "departure": departure,
            "arrival": arrival,
            "price": f"{price}円"
        }
    except Exception as e:
        print(f"Error parsing transit summary: {e}")
        return None


def main():
    # Example usage:
    url = build_yahoo_transit_url("新宿", "大宮", 2025, 4, 18, 23, 48)

    data = req_get(url).text

    result = parse_transit_summary(data)

    print(result)


if __name__ == "__main__":
    main()

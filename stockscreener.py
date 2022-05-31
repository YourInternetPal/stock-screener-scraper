import requests
from bs4 import BeautifulSoup


class StockScreener:
    def __init__(self):
        self.BASE_URL = "https://<URL_REMOVED>/"
        self.HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

    def get_data(self, ticker, required_data):
        scraped_data = {}
        page_url = "{0}{1}".format(self.BASE_URL, ticker)
        page_request = requests.get(page_url, headers=self.HEADERS)
        if page_request.status_code == 200:
            page = BeautifulSoup(page_request.content, 'html.parser')
            data_table = page.find("table", {'class': 'snapshot-table2'})
            table_headers = data_table.find_all("td", {'class': 'snapshot-td2-cp'})
            table_data = data_table.find_all("td", {'class': 'snapshot-td2'})

            for index, data in enumerate(table_headers):
                if data.text in required_data:
                    scraped_data[data.text] = table_data[index].text
            return scraped_data
        else:
            return None
from re import sub
import asyncio
import nest_asyncio
from colorama import Fore
from decimal import Decimal
from typing import Optional
import httpx
import bs4


# https://stackoverflow.com/questions/46827007/runtimeerror-this-event-loop-is-already-running-in-python
nest_asyncio.apply()

username: Optional[str] = None
password: Optional[str] = None

# Older versions of python require calling loop.create_task() rather than on asyncio.
# Make this available more easily.
global loop

DIVIDEND_TAX_LOWER_THRESHOLD = Decimal(7.5)
LOGIN_URL = 'https://online.sjdaccountancy.com/system/login'
DIVIDENDS_URL = 'https://online.sjdaccountancy.com/dividends'
DASHBOARD_URL = 'https://online.sjdaccountancy.com/dashboard/index'

class SJDMetric:
    """A scraped metric description from SJD"""
    key: str
    xpath: str
    html: str
    result: Decimal



class ReportedProfits(SJDMetric):
    key = 'reported_profits'
    xpath = 'span:nth-of-type(2)'


class OwedToDirector(SJDMetric):
    key = 'owed_to_director'
    xpath = 'span:nth-of-type(3)'


class UnpaidInvoices(SJDMetric):
    key = 'unpaid_invoices'
    xpath = 'span:nth-of-type(4)'


class Reader:
    def __init__(self):
        self.username = username
        self.password = password
        self.login_payload = {
            'username': self.username,
            'password': self.password,
            'btn_submit': 'Login'
        }

        self.login_payload = {
            'username': "jon@howapped.com",
            'password': "Ddu&K!Ro78",
            'btn_submit': 'Login'
        }

    def scrape(self, html:str, metric):
        return self.__clean_currency(html.select(metric.xpath)[0].text)

    def __clean_currency(self, money:str):
        """Utility fn to convert scraped str to Decimal"""
        return Decimal(sub(r'[^\d.]', '', money))

    async def get_overview(self):
        async with httpx.AsyncClient() as client:
            resp = await client.post(LOGIN_URL, data=self.login_payload, cookies={})
            resp.raise_for_status()
            resp = await client.get(DASHBOARD_URL)

        soup = bs4.BeautifulSoup(resp.content, 'html.parser')
        # company overview div
        div = soup.find("div", class_="threecolwidget")
        return {
            ReportedProfits.key: self.scrape(div, ReportedProfits()),
            OwedToDirector.key: self.scrape(div, OwedToDirector()),
            UnpaidInvoices.key: self.scrape(div, UnpaidInvoices()),
        }


    async def get_total_dividends_withdrawn(self):
        div = 0

        async with httpx.AsyncClient() as client:
            resp = await client.post(LOGIN_URL, data=self.login_payload, cookies={})
            resp.raise_for_status()
            resp = await client.get(DIVIDENDS_URL)
            content = resp.content
            # scrape dividends and sum
            soup = bs4.BeautifulSoup(content, 'html.parser')
            dividend_values = soup.select("table tr td:nth-of-type(2)")
            dividend_values = [self.__clean_currency(value.text) for value in dividend_values]
            div = sum(dividend_values)
            return div


async def tasks():
    reader = Reader()
    tasks = []
    task_returns = {}
    task_ids = ['total_dividends_withdrawn', 'overview']

    for task_id in task_ids:
        tasks.append((task_id, loop.create_task(getattr(reader, f'get_{task_id}')())))

    for n, t in tasks:
        task_returns[n] = await t
        print(Fore.WHITE + f"Task completed.", flush=True)

    return task_returns

def calulate_using_received_metrics(**kwargs):
    r = Reader()
    total_div = kwargs.get('total_dividends_withdrawn')
    overview = kwargs.get('overview')
    reported_profits = overview.get('reported_profits')
    owed_to_director = overview.get('owed_to_director')
    unpaid_invoices = overview.get('unpaid_invoices')

    est_dividend_tax_owed = total_div * \
            round((DIVIDEND_TAX_LOWER_THRESHOLD / 100), 2)


    return reported_profits - est_dividend_tax_owed

async def main():
    print(Fore.YELLOW + f"main() Start SJD.", flush=True)
    global loop

    loop = asyncio.get_event_loop()
    task_returns = loop.run_until_complete(tasks())
    final = calulate_using_received_metrics(**task_returns)
    return final

    print(Fore.GREEN + f"Total Cleared Profits: {final}", flush=True)
    print(Fore.YELLOW + f"main() End SJD.", flush=True)
    return final

async def run():
    return 20

if __name__ == '__main__':
    main()

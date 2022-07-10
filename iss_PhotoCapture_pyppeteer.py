import asyncio
from pyppeteer import launch
from time import sleep
import iss_location

async def asyncmain():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://iss-live.github.io')
    sleep(30)
    await page.screenshot({'path': str("'" + iss_location.lat() + '_' + iss_location.long() + '.png' + "'"), 'fullPage': 'true'})
    await browser.close()

def main():
    asyncio.get_event_loop().run_until_complete(asyncmain())


if __name__ == "main":
    main()

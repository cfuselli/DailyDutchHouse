import argparse
import importlib

# Import the website you want to scrape


args = argparse.ArgumentParser()
args.add_argument("--website", "-w", type=int, help="Website to scrape")
args.add_argument("--method", "-m", type=str, help="Method to scrape the website", choices=["req", "sel", "pyp"], default=None)
# add debug argument
args.add_argument("--debug", "-d", action="store_true", help="Print debug information")
args = args.parse_args()


website_n = args.website
method = args.method
debug = args.debug

website = importlib.import_module(f"websites.website_{website_n}").website



print(f"Getting data from website: {website.url}\n\n\n")
print(">>>>>>>>>>>>>> Scraped data:")

website.scrape_example(print_html=debug)
for i, house in enumerate(website.houses[:2]):
    print(f"House info:")
    house.print()

if method == "sel":
    print(">>>>>>>>>>>>>> Scraped data with selenium:")
    website.scrape_selenium(print_html=debug)
    for i, house in enumerate(website.houses[:2]):
        print(f"House info:")
        house.print()

if method == "req":
    print(">>>>>>>>>>>>>> Scraped data with requests html:")
    website.scrape_requests_html(print_html=debug)
    for i, house in enumerate(website.houses[:2]):
        print(f"House info:")
        house.print()

if method == "pyp":
    print(">>>>>>>>>>>>>> Scraped data with pyppeteer:")
    website.scrape_pyppeteer(print_html=debug)
    for i, house in enumerate(website.houses[:2]):
        print(f"House info:")
        house.print()
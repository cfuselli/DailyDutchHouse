from websites.website_4 import website


print(f"Getting data from website: {website.url}\n\n\n")
website.scrape_test()
print("\n\n\n")
print(f"Getting data from website: {website.url}\n\n\n")
print(">>>>>>>>>>>>>> Scraped data:")

website.scrape_example()
for i, house in enumerate(website.houses[:2]):
    print(f"House info:")
    house.print()

print(">>>>>>>>>>>>>> Scraped data with selenium:")
website.scrape_selenium()
for i, house in enumerate(website.houses[:2]):
    print(f"House info:")
    house.print()

print(">>>>>>>>>>>>>> Scraped data with requests html:")
website.scrape_requests_html()
for i, house in enumerate(website.houses[:2]):
    print(f"House info:")
    house.print()


print(">>>>>>>>>>>>>> Scraped data with pyppeteer:")
website.scrape_pyppeteer()
for i, house in enumerate(website.houses[:2]):
    print(f"House info:")
    house.print()





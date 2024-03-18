from playwright.sync_api import sync_playwright
import psycopg2
from psycopg2.extras import execute_values

def main():
    with sync_playwright() as p:
        
        ## Scrape data
        browser = p.chromium.launch(headless=False) # or firefox or webkit ## headless False to see the browser
        page = browser.new_page()
        page.goto("https://coinmarketcap.com", timeout=30000)
        
        # Scrolling down to reveal ungenerated content
        for i in range(5):
            page.mouse.wheel(0, 2000)
            page.wait_for_timeout(1000)
        
        # Scraping the data
        trs_xpath = "//table[@class='sc-14cb040a-3 dsflYb cmc-table  ']/tbody/tr"
        trs_list = page.query_selector_all(trs_xpath)
        
        master_list = []
        
        for tr in trs_list:
            coin_dict = {}
            tds = tr.query_selector_all("//td")
            
            coin_dict['id'] = tds[1].inner_text()
            coin_dict['Name'] = tds[2].query_selector("//p[@color='text']").inner_text()
            coin_dict['Symbol'] = tds[2].query_selector("//p[@color='text3']").inner_text()
            coin_dict['Price'] = float(tds[3].inner_text().replace("$", "").replace(",", ""))
            coin_dict['Market_Cap_USD'] = int(tds[7].inner_text().replace("$", "").replace(",", ""))
            coin_dict['Volume'] = int(tds[8].query_selector('//p[@color="text"]').inner_text().replace("$", "").replace(",", ""))
            
            master_list.append(coin_dict)
            
        # tuples
        list_of_tuples = [tuple(dic.values()) for dic in master_list]
        print(list_of_tuples)
        # for element in master_list:
        #     print (element)
        ## Connect to database
        
        browser.close()  # End by closing the browser

if __name__ == "__main__":
    main()

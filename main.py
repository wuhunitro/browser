from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

# add a vpn extension
chrome_options.add_extension('extensions/VPN.crx')

# remove banner and software flags that point towards chrome automation
chrome_options.add_experimental_option("excludeSwitches",
                                       ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

print('launching chrome...')

driver = webdriver.Chrome(options=chrome_options)

driver.execute_script(
  "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

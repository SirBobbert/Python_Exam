from shutil import which
from selenium import webdriver
    
def init_webdriver():
    FIREFOXPATH = which("firefox")
    CHROMEPATH = which("chrome") or which("chromium")
    """Simple Function to initialize and configure Webdriver"""
    if FIREFOXPATH != None:
        print(FIREFOXPATH)#cm
        from selenium.webdriver.firefox.options import Options

        options = Options()
        options.binary = FIREFOXPATH
        options.add_argument("-headless")
        return webdriver.Firefox(firefox_options=options, log_path="geckodriver.log")

    elif CHROMEPATH != None:
        print(CHROMEPATH)#cm
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.binary_location = CHROMEPATH
        options.add_argument("--headless")
        return webdriver.Chrome(chrome_options=options, service_args=['--verbose'], service_log_path="chromedriver.log")
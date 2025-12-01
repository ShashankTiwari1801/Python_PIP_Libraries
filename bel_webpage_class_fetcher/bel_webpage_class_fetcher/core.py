from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''

'''
def load_url(
        url: str,
        wait_for_class: str,
        output_file_name: str = "temp.html",
        driver_path: str = "geckodriver",
        headless: bool = True
):

    firefox_options = Options()
    if headless:
        firefox_options.add_argument("--headless")
    firefox_options.add_argument("--disable-gpu")

    try:
        service = Service(driver_path) if driver_path else Service()

        driver = webdriver.Firefox(service=service, options=firefox_options)

        driver.get(url)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, wait_for_class))
        )

        content = driver.page_source
        with open(output_file_name, "w", encoding="utf-8") as f:
            f.write(content)

    finally:
        driver.quit()
    
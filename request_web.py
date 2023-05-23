from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": r"pdf\new",
    "download.prompt_for_download": False,  # to auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,   # to open pdf externally
    "safebrowsing.enabled": True
})

# Initialize the driver
webdriver_service = Service(r"C:\Users\Stephanie\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
driver.get('https://www.pfwb.be/documents-parlementaires')

next_page_xpath = r'//*[@id="__layout"]/div/main/div/div/div/div[2]/div[4]/nav/ul/li[11]/button/i/svg/use'
target_element_xpath = "//div[@class='form-input']"
next_button_selector = "#__layout > div > main > div > div > div > div.inner > div.pagination > nav > ul > li:nth-child(11) > button > i > svg"


# Get the filtered elements
time.sleep(10)

try:
    # Wait until the form is loaded
    form_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div[2]/div[3]/div'))
    )

    # Click the button to access the list of document types
    button_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div[2]/div[3]/div/div/div[1]/div[2]/div[2]'))
    )
    button_element.click()

    # Interact with the filter
    filter_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/div/div/ul/li[21]/span'))
    )
    filter_element.click()


except TimeoutException:
    print("Timeout: The element did not load within 10 seconds.")


# Loop through all pages
time.sleep(2)

while True:
    for file_link_number in range(1, 19):
        # Try to find the file link and click it
        try:
            file_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div[2]/ul/li[' + str(file_link_number) + ']/a/div[3]/div/span'))
            )
            file_link.click()

            # Try to find the download link and click it
            download_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div/div/div/main/div/div/div/div[2]/div/div/div/a[2]'))
            )
            # download_link.click()
            file_url = download_link.get_attribute('href')

            # Navigate to the file URL
            driver.get(file_url)

            # Navigate back to the previous page
            driver.back()

        except (TimeoutException, NoSuchElementException):
            print(
                "Timeout or No Such Element: The element did not load within 10 seconds.")
            continue  # Skip to the next file link if this one failed

     # Try to find the next button and click it
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, next_button_selector))
        )
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        print('next page')
        next_button.click()
    except TimeoutException:
        print("No more pages.")

    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_form_submission():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.qa-territory.online/forms/post")

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Alejandro")

    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit']"
    )
    submit_button.click()

    WebDriverWait(driver, 10).until(
        lambda browser: "Alejandro" in browser.find_element(
            By.TAG_NAME, "body"
        ).text
    )

    response_text = driver.find_element(By.TAG_NAME, "body").text

    assert "Alejandro" in response_text

    driver.quit()

from selenium import webdriver


def test_user_can_login() -> None:
    driver = webdriver.Chrome()
    driver.get("https://your-app.com/login")
    driver.find_element_by_name("username").send_keys("john@example.com")
    driver.find_element_by_name("password").send_keys("password123")
    driver.find_element_by_name("login").click()
    assert driver.title == "Dashboard"
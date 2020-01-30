from appium import webdriver

desired_caps = {
    "deviceName": "emulator-5556",
    "platformName": "android",
    "appPackage": "com.android.calculator2",
    "appActivity": ".Calculator",
    "noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.find_element_by_id("com.android.calculator2:id/digit_7").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_8").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()
result = driver.find_element_by_id("com.android.calculator2:id/result").get_attribute("text")
assert result == '15'

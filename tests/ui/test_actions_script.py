# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# interactions_xpath = "//a[contains(text(),'Interactions')]"
# drag_drops_xpath = "//a[contains(text(),'Drag and Drop ')]"
# static_xpath = "//a[contains(text(),'Static ')]"
#
# def test_actions():
#     driver = webdriver.Chrome()
#     driver.get("https://demo.automationtesting.in/FileUpload.html")
#     driver.maximize_window()
#     wait = WebDriverWait(driver, 10)
#
#     # Direct click to interaction element
#     # interaction_ele = wait.until(EC.presence_of_element_located((By.XPATH, interactions_xpath)))
#     # interaction_ele.click()
#
#     # Mouse hover to the interaction element
#     actions = ActionChains(driver)
#     interaction_ele = wait.until(EC.presence_of_element_located((By.XPATH, interactions_xpath)))
#     actions.move_to_element(interaction_ele).click().perform()
#     time.sleep(5)
#
#     # Direct click drag and drop element
#     # drag_ele = wait.until(EC.presence_of_element_located((By.XPATH, drag_drops_xpath)))
#     # drag_ele.click()
#     # time.sleep(5)
#
#     # Mouse hover to the drag and drop element
#     drag_ele = wait.until(EC.presence_of_element_located((By.XPATH, drag_drops_xpath)))
#     actions.move_to_element(drag_ele).click().perform()
#
#     # Direct click static element
#     # static_ele = wait.until(EC.presence_of_element_located((By.XPATH, static_xpath)))
#     # static_ele.click()
#     # time.sleep(5)
#
#     # Mouse hover to the static element
#     static_ele = wait.until(EC.presence_of_element_located((By.XPATH, static_xpath)))
#     actions.move_to_element(static_ele).click().perform()
#     print("Successfully completed actions")
#

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

interactions_xpath = "//a[contains(text(),'Interactions')]"
drag_drops_xpath = "//a[contains(text(),'Drag and Drop ')]"
static_xpath = "//a[contains(text(),'Static ')]"

def test_actions(driver):
    driver.get("https://demo.automationtesting.in/FileUpload.html")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    actions = ActionChains(driver)

    interaction_ele = wait.until(EC.presence_of_element_located((By.XPATH, interactions_xpath)))
    actions.move_to_element(interaction_ele).click().perform()
    time.sleep(5)

    drag_ele = wait.until(EC.presence_of_element_located((By.XPATH, drag_drops_xpath)))
    actions.move_to_element(drag_ele).click().perform()

    static_ele = wait.until(EC.presence_of_element_located((By.XPATH, static_xpath)))
    actions.move_to_element(static_ele).click().perform()

    print("Successfully completed actions")


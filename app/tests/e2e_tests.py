from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def run_tests():
    print("Starting Selenium E2E tests...")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.binary_location = "/usr/bin/chromium"

    service = Service(executable_path="/usr/bin/chromedriver")

    FRONTEND_URL = "http://frontend.taskapp.svc.cluster.local"
    driver = webdriver.Chrome(service=service, options=options)
    passed = 0
    failed = 0

    try:
        print("Test 1: Page loads...")
        driver.get(FRONTEND_URL)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        assert "Task Manager" in driver.find_element(By.TAG_NAME, "h1").text
        print("PASS: Page loaded successfully")
        passed += 1

        print("Test 2: Tasks are displayed...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h3"))
        )
        tasks = driver.find_elements(By.TAG_NAME, "h3")
        assert len(tasks) > 0
        print(f"PASS: Found {len(tasks)} tasks")
        passed += 1

        print("Test 3: Learn Kubernetes task exists...")
        page_text = driver.find_element(By.TAG_NAME, "body").text
        assert "Learn Kubernetes" in page_text
        print("PASS: Learn Kubernetes task found")
        passed += 1

    except Exception as e:
        print(f"FAIL: {e}")
        failed += 1

    finally:
        driver.quit()

    print(f"Results: {passed} passed, {failed} failed")
    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed!")
        sys.exit(0)

if __name__ == "__main__":
    run_tests()

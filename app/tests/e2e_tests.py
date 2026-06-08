from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.reporter import AllureReporter
from allure_commons.logger import AllureFileLogger
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from allure_commons.model2 import TestResult, TestStepResult, Status, StatusDetails, Attachment
from allure_commons.utils import uuid4, now
import sys
import os
import traceback

ALLURE_RESULTS_DIR = "/tmp/allure-results"
os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)

logger = AllureFileLogger(ALLURE_RESULTS_DIR)

def write_test_result(name, status, steps, message=None):
    result = TestResult(
        uuid=uuid4(),
        name=name,
        status=status,
        start=now(),
        stop=now(),
        steps=steps,
    )
    if message:
        result.statusDetails = StatusDetails(message=message)
    logger.report_result(result)

def take_screenshot(driver):
    return driver.get_screenshot_as_png()

def run_tests():
    print("Starting Selenium E2E tests...")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.binary_location = "/usr/bin/chromium"

    service = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    FRONTEND_URL = "http://frontend.taskapp.svc.cluster.local"
    passed = 0
    failed = 0

    tests = [
        {
            "name": "Test 1: Page loads",
            "fn": lambda d: (
                d.get(FRONTEND_URL),
                WebDriverWait(d, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1"))),
                assert_true("Task Manager" in d.find_element(By.TAG_NAME, "h1").text, "Task Manager heading not found")
            )
        },
        {
            "name": "Test 2: Tasks are displayed",
            "fn": lambda d: (
                WebDriverWait(d, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h3"))),
                assert_true(len(d.find_elements(By.TAG_NAME, "h3")) > 0, "No tasks found on page")
            )
        },
        {
            "name": "Test 3: Learn Kubernetes task exists",
            "fn": lambda d: assert_true(
                "Learn Kubernetes" in d.find_element(By.TAG_NAME, "body").text,
                "Learn Kubernetes task not found"
            )
        },
    ]

    for test in tests:
        name = test["name"]
        step = TestStepResult(name=name, start=now())
        try:
            test["fn"](driver)
            step.status = Status.PASSED
            step.stop = now()
            write_test_result(name, Status.PASSED, [step])
            print(f"PASS: {name}")
            passed += 1
        except Exception as e:
            step.status = Status.FAILED
            step.stop = now()
            step.statusDetails = StatusDetails(message=str(e))
            write_test_result(name, Status.FAILED, [step], message=str(e))
            print(f"FAIL: {name} — {e}")
            failed += 1

    driver.quit()

    print(f"\nResults: {passed} passed, {failed} failed")
    print(f"Allure results saved to: {ALLURE_RESULTS_DIR}")

    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed!")
        sys.exit(0)

def assert_true(condition, message):
    if not condition:
        raise AssertionError(message)

if __name__ == "__main__":
    run_tests()

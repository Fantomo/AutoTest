# -*- encoding:utf-8 -*-

import unittest

from utils.config import REPORT_DIR

from utils.HTMLTestRunner import HTMLTestRunner
from test.case.LoginTest import LoginTest


def test_login():
    login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

    test_case = unittest.TestSuite([login])

    html_file = open(REPORT_DIR + "\\LoginTestReport.html", "wb")

    return test_case, html_file


if __name__ == "__main__":
    tests_case, htm_file = test_login()
    runner = HTMLTestRunner(
        stream=htm_file,
        title="LoginAutoTest",
        description="testLoginAutoTest"
    )
    runner.run(tests_case)

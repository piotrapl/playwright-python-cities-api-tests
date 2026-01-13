import unittest
import HtmlTestRunner

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("tests")

    runner = HtmlTestRunner.HTMLTestRunner(
        output="reports",
        report_name="API_Test_Report",
        combine_reports=True,
        add_timestamp=True
    )

    runner.run(suite)
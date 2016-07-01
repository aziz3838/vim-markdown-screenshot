import unittest
import vim_markdown_screenshot as sut


@unittest.skip("Don't forget to test!")
class VimMarkdownScreenshotTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_markdown_screenshot_example()
        self.assertEqual("Happy Hacking", result)

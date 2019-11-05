import unittest
import smtpsend
import configemail

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertNotEqual(smtpsend.send_email("Test subject", """\
<html>
  <head></head>
  <body>
       <a href={pagesCat}>{pagesCat}</a><br>
       <a href={pagesDog}>{pagesDog}</a><br>
       <a href={pagesFox}>{pagesFox}</a>
  </body>
</html>
""".format(pagesCat=smtpsend.pagesCat, pagesDog=smtpsend.pagesDog, pagesFox=smtpsend.pagesFox)),'Subject: {}\n\n{}'.format(smtpsend.subject, smtpsend.msg))


    def test_get_email(self):
            self.assertEqual(smtpsend.get_email('E:\Webdriver\chromedriver'),smtpsend.driver)

    def test_chek_link(self):

        self.assertGreater(smtpsend.check_link(smtpsend.quantity),3)

if __name__ == '__main__':
    unittest.main()

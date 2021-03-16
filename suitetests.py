import unittest
from eesignin import eesigninCase
from eesignup import eesignupCase
from eeaddcourse import eeaddcourseCase
# get all tests from SearchProductTest and HomePageTest class
eesignin = unittest.TestLoader().loadTestsFromTestCase(eesigninCase)
eesignup = unittest.TestLoader().loadTestsFromTestCase(eesignupCase)
eeaddcourse = unittest.TestLoader().loadTestsFromTestCase(eeaddcourseCase)
# create a test suite combining search_test and home_page_test
suitetests = unittest.TestSuite([eesignin, eesignup, eeaddcourse])
# run the suite
unittest.TextTestRunner(verbosity=2).run(suitetests)
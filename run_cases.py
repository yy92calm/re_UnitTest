#-*- coding=utf-8 -*-
import unittest
import os
from BaseUnit.re_suite import reTestSuite

#destination
case_path = os.path.join(os.getcwd(),"Cases")

#find all cases in folders
def all_cases():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test_*.py",top_level_dir=None)
    caseList = []
    for test_suite in discover:
        for test in test_suite:
            for tt in test:
                caseList.append(tt)
    return caseList

if __name__ == "__main__":
    suit = reTestSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    for case in all_cases():
        suit.addTest(case)
        caseResult = runner.run(suit)
        if caseResult.testsRun > (len(caseResult.errors)+len(caseResult.failures)):
            print case,"Succ"
        else:
            print case,"Fail"
        suit.removeTest(case)
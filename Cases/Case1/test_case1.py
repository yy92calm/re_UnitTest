#-*- coding=utf-8 -*-
import sys
sys.path.append('../../')
from BaseUnit.re_testcase import reTestCase

class Case1(reTestCase):

    def test(self):
        raise Exception("error in case1")
        print "This is case1"
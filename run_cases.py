# coding:utf-8
import unittest
import os

case_path = os.path.join(os.getcwd(),"Cases")

def all_cases():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test_*.py",top_level_dir=case_path)
    print discover
    return discover

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_cases())
import os
import sys
import pytest
import argparse

"""

This file is an entrypoint for tests

Usage:
    

"""


if __name__ == "__main__":

    print("Running code integration tests...")

    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        argv = []

    # Use argparse to easily parse keyword-like arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', type=str, default='all', help='Specify which tests to run: all, or a substring of the test name to match (e.g. "test_routing")')
    # see: https://docs.pytest.org/en/stable/example/markers.html#using-k-expr-to-select-tests-based-on-their-name

    args = parser.parse_known_args(argv)[0]

    #this file
    this_file_path = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(this_file_path)


    if args.k == "all":
        retcode = pytest.main([tests_dir, "--cache-clear"])
        # retcode = pytest.main([tests_dir, "--cache-clear", "-v", "-s"]) # s option to show print statements in test output, useful for debugging
    
    else:
        retcode = pytest.main([tests_dir, "--cache-clear", "-k", args.k])
        # retcode = pytest.main([tests_dir, "--cache-clear", "-k", args.tests, "-v", "-s"]) # s option to show print statements in test output, useful for debugging
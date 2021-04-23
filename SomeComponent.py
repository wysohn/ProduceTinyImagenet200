import os
import sys
import argparse

## Parse args
parser = argparse.ArgumentParser("SomeComponent")
parser.add_argument("--< Your 1st Input name >", type=str, help="<description>")
parser.add_argument("--< Your 2nd Input name >", type=str, help="<description>")
parser.add_argument("--< Your 1st Output name >", type=str, help="<description>")
args = parser.parse_args()

# first_input = args.< Your 1st Input name >

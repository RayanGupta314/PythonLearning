#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('codelength')
arguments=parser.parse_args()
codelength = arguments.codelength
print(codelength)


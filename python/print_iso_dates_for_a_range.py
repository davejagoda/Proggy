#!/usr/bin/env python3

import argparse
import datetime

import dateparser

parser = argparse.ArgumentParser()
parser.add_argument("-t0", "--t0", required=True)
parser.add_argument("-t1", "--t1", required=True)
args = parser.parse_args()

t0 = dateparser.parse(args.t0).date()
t1 = dateparser.parse(args.t1).date()
while t0 < t1:
    print(t0)
    t0 += datetime.timedelta(days=1)

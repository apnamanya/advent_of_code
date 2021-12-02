#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Retrieve input for a provided day in Advent of Code."""
import argparse
import os
import sys

import requests

# Instuctions on retrieving your session key for use with this script:
# https://github.com/wimglenn/advent-of-code-wim/issues/1

def parse_arguments():
    """Parse command-line arguments using argparse."""
    parser = argparse.ArgumentParser(description="Input getter")
    parser.add_argument("-d", "--day", help="The day to retrieve", required=True)
    parser.add_argument("-y", "--year", help="The year of event to retrieve", required=True)

    return parser.parse_args()


def get_input(day, year):
    """Retrieve the input for the AoC day."""
    print(f"Day parsed is day{day}.")
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    pwd = os.path.realpath(os.path.dirname(__file__))

    with open(os.path.join(pwd, "session.txt"), "r") as filep:
        cookie = filep.readline().strip()

    yeardir = os.path.join(pwd, f"{year}")
    if not os.path.isdir(yeardir):
        os.mkdir(yeardir, 0o755)

    sess = requests.Session()
    jar = requests.cookies.RequestsCookieJar()
    jar.set("session", cookie)
    res = sess.get(url, cookies=jar)


    with open(f"{year}/input_day{day}.txt", "w") as filep:
        filep.write(res.text.strip())


def main():
    """Execute the script."""
    args = parse_arguments()
    print(f"Getting the input for day{args.day}")
    

    get_input(args.day, args.year)

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
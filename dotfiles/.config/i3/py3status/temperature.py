#!/usr/bin/env python3

import argparse
import os

import requests
from bs4 import BeautifulSoup


def parse_args():
    parser = argparse.ArgumentParser("temperature")
    parser.add_argument(
        "--py3status", help="call notify-send instead of printing", action="store_true"
    )
    args = parser.parse_args()
    return args


def custom_selector(tag):
    return (
        tag.name == "span"
        and tag.has_attr("class")
        and bool(set(["gewaesser", "wasser_temp"]) & set(tag.get("class")))
    )


def main():
    args = parse_args()
    response = requests.get("https://meteonews.ch/de/Wassersport/M06650000/Luzern")
    html = BeautifulSoup(response.content, features="lxml")
    spans = html.find_all(custom_selector)

    next_value = None
    result = {"Vierwaldstättersee": None, "Reuss": None}
    for span in spans:
        text = span.get_text().split(",")[0]
        if text in result.keys():
            next_value = text
            continue

        if next_value:
            result[next_value] = text
            next_value = None

    see = result["Vierwaldstättersee"]
    fluss = result["Reuss"]

    print(f"{see}°C")
    if not args.py3status:
        os.system(
            f'notify-send -t 5000 -i plugin-water "Vierwaldstättersee: {see}°C\nReuss: {fluss}°C"'
        )


if __name__ == "__main__":
    main()

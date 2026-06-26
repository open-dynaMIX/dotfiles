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


def main():
    args = parse_args()
    response = requests.get("https://meteonews.ch/de/Wetter/G2659811/Luzern")
    soup = BeautifulSoup(response.content, "html.parser")
    water_bodies = {
        "Vierwaldstättersee": "292",
        "Reuss": "219"
    }
    result = {"Vierwaldstättersee": None, "Reuss": None}

    for name, water_id in water_bodies.items():
        # Find the container block safely by its system ID
        container = soup.find(attrs={"data-chart-id": "ModuleChartWaterTemperature", "data-water-id": water_id})

        if container:
            # Find the tag explicitly containing the label "heute"
            heute_tag = container.find(string=lambda text: text and "heute" in text.lower())
            if heute_tag:
                # The temperature value is sitting right next to it in the sibling block
                temperature = heute_tag.find_next(class_="data-value").text.strip()
                result[name] = temperature
            else:
                print(f"Could not find today's data text for {name}")
        else:
            print(f"Container for {name} missing.")

    print(result['Vierwaldstättersee'])
    if not args.py3status:
        os.system(
            f'notify-send -t 5000 -i plugin-water "Vierwaldstättersee: {result['Vierwaldstättersee']}\nReuss: {result['Reuss']}"'
        )


if __name__ == "__main__":
    main()

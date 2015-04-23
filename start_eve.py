#!/usr/local/bin/python3
# coding=utf-8

import os

from sh import machine, grep


def main():
    """
    main
    """
    x = os.popen("ps aux | grep vbox | grep -v grep").read().strip()

    if len(x) < 300 or len(x) > 400:
        print("check eve", len(x))
        machine_eve = grep(machine("ls"), "eve").strip()

        if "Stopped" in machine_eve or "Saved" in machine_eve:
            machine("start", "eve")
            print(1)
        elif "Running" in machine_eve:
            print(0)
        else:
            for i in range(10):
                machine_eve = machine_eve.replace("   ", "  ")

            print("\033[31mError:", machine_eve, "\033[0m")
    else:
        print("0")


if __name__ == "__main__":
    main()

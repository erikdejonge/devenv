#!/usr/local/bin/python3
# coding=utf-8

import os
import time
from sh import docker_machine, grep, Command


def main():
    """
    main
    """
    if os.path.exists(os.path.expanduser("~/.upgradingeve")):
        print("0")
        return

    machine_eve = grep(docker_machine("ls"), "eve").strip()

    if "Stopped" in machine_eve or "Saved" in machine_eve:
        os.system('docker-machine -D start eve')
    elif "Running" in machine_eve:
        pass
    else:
        for i in range(10):
            machine_eve = machine_eve.replace("   ", "  ")

        print("\033[31mError:", machine_eve, "\033[0m")


if __name__ == "__main__":
    main()

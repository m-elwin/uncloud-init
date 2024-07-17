#!/usr/bin/env python3
""" Perform initial setup steps that are done by cloud-init
    See uncloud-init/README.md for more details.
"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="uncloud-init.py",
        description="Perform only the essential cloud-init steps needed for an Ubuntu Linux install")
    parser.add_argument("config",
        nargs="?",
        default="/etc/cloud/cloud.cfg.d/99-installer.cfg",
        help="Path to file usually stored at /etc/cloud/99-installer.cfg")

    args = parser.parse_args()
    print(f"my arg: {args.config}")



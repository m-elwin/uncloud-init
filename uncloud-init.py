#!/usr/bin/env python3
""" Perform initial setup steps that are done by cloud-init
    See uncloud-init/README.md for more details.

    The config file is yaml file, but this script must not depend on pyyaml.
"""

import argparse

def flat_parse_yaml(yaml):
    """ Return a dictionary of keys and values for yaml.

        The file we work with do not meaningfully use lists or hierarchy or other
        yaml features so indendation is ignored and lists are parsed as single values
    """
    lines = yaml.splitlines()
    keyvals = [line.lstrip(' -').split(":") for line in lines if len(line) > 0]
    return { keyval[0] : keyval[1].lstrip() for keyval in keyvals if len(keyval) == 2}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="uncloud-init.py",
        description="Perform only the essential cloud-init steps needed for an Ubuntu Linux install")
    parser.add_argument("config",
        nargs="?",
        default="/etc/cloud/cloud.cfg.d/99-installer.cfg",
        help="Path to file usually stored at /etc/cloud/99-installer.cfg")

    args = parser.parse_args()

    with open(args.config) as config_file:
        config_raw = config_file.read()
        
        # unescape the literal newlines 
        config_unescaped = config_raw.replace("\\n", "\n")

        # remove line continuation characters
        config = "".join(config_unescaped.split("\\"))
        yaml_dict = flat_parse_yaml(config)
        print(yaml_dict)

        print(f"Setting timezone to {yaml_dict['timezone']}")
        print(f"Setting locale to {yaml_dict['locale']}")

        # For some reason "gecos" is the key under which the user's real name is stored
        print("Creating User Account:")
        print(f"  Full Name: {yaml_dict['gecos']}")
        print(f"  Username: {yaml_dict['name']}")
        print(f"  Groups: {yaml_dict['groups']}")
        print(f"  Password Hash: {yaml_dict['passwd']}")

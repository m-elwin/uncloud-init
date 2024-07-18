#!/usr/bin/env python3
""" Perform initial setup steps that are done by cloud-init
    See uncloud-init/README.md for more details.

    The config file is yaml file, but this script must not depend on pyyaml.
"""

import argparse

def get_value(key, text):
    """ Get the value of a yaml key in the cloud config file 
    
        key - the yaml key to lookup.
        text - full text of the yaml file
        
        Assumes the value is immediately after the key, not on a newline. 
        That assumption is valid for the particular yaml file this script parses.
    """
    start = text.find(f"{key}: ") + len(f"{key}: ")
    end   = start + text[start:].find("\n")
    return text[start:end]

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
        config = config_file.read()
        
        # The userdata contains the information we need from the setup.
        # It is written by subiquity
        userdata_raw = config[config.find("userdata_raw:"):-1].split('"')[1]
        # unescape the data
        userdata_unescaped = userdata_raw.replace("\\n", "\n")
        # remove line continuation characters
        userdata = "".join(userdata_unescaped.split("\\"))
        print(f"userdata:\n{userdata}\n")
        # Get the locale
        locale = get_value("locale", userdata)
        print(f"locale={locale}")
        
        # Get the timezone
        timezone = get_value("timezone", userdata)
        print(f"timezone={timezone}")
    
        # Get the user's full name
        fullname = get_value("gecos", userdata)
        print(f"fullname={fullname}")

        # Get the groups the user should be in
        groups =  get_value("groups", userdata)
        print(f"groups={groups}")

        # Get the user's username
        user = get_value("name", userdata)
        print(f"user={user}")
        

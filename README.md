# Uncloud Init
Basic package for performing the cloud-init role of finishing the Ubuntu 24.04 Subiquity user setup on first boot.
Does not require cloud-init to be installed.

Aims to complete all cloud-init tasks that subiquity assigns to cloud init for a *Desktop* Install.

Based on some (uncareful)  source-code reading, the only required task for a minimal Desktop install is to:
1. Set the locale
2. Set the timezone
3. Set up the user and groups. 

After completing all its tasks, this script deletes the cloud-init configuration created by subiquity and completely uninstalls itself.

For more details about the context where this package is useful (namely creating a custom Ubuntu Desktop Install ISO in a certain way) see 
[MS in Robotics Minimal Ubuntu](https://nu-msr.github.io/hackathon/ubuntu_minimal.html)

# Why?
While cloud-init may make writing installers easier for the Ubuntu developers (now cloud, server, and desktop all use the same system), it is Ubuntu-specific technology and,
on a desktop install, it is annoying having it installed for a few reasons:
1. It runs every time on boot, just to check if it should disable itself
2. It should never need to be run except on the first installation
3. It brings in many dependencies.

Why not just uninstall cloud-init after the first job?

1. It runs every time on boot, just to check if it should disable itself
2. It should never need to be run except on the first installation
3. It brings in many dependencies.

Why not just uninstall cloud-init after the first job?
1. The point of making a custom installer is to avoid  needing to uninstall packages after installation and instead start with a clean configuration that
never had those packages in the first place.  It's a tangled web, but cloud-init brings in netplan.io, and part of this build's goal is to avoid netplan.

# Building the Deb
1. Install `devscripts`
2. The debian build process creates files one directory up from the source tree.  Be aware when building.
1. From within the source tree run `dpkg-source -b .` This must be done once.
2. Then run `debuild -uc -us` to unofficially build the package and test it.
3. To build the signed source package (for PPA uploading) run `debuild -k<keyid> -S`
# Files:
- test/99-installer.cfg: An example configuration file, used for testing
- uncloud-init.service: Systemd unit to run the uncloud-init service
- Makefile: Used to install the files to the system
- debian/ the package directory. This package is only useful for an Ubuntu installation so it uses the (Debian Native Package Format)[https://www.debian.org/doc/manuals/debmake-doc/ch05.en.html#native]

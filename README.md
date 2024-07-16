# Uncloud Init
Basic package for performing the cloud-init role of finishing the Ubuntu 24.04 Subiquity user setup on first boot.
Does not require cloud-init to be installed.

Aims to complete all cloud-init tasks that subiquity assigns to cloud init for a *Desktop* Install.

Based on some (uncareful)  source-code reading, the only required task for a minimal Desktop install is to
1. Set up the username and password (based on the information subiquity provides to cloud init)

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


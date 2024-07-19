# Don't need to do anything to build, but debian will do this step
uncloud-init:
	@echo "Built uncloud-init. run make install to install"

# Copy the files to the expected locations
install:
	mkdir -p $(DESTDIR)/usr/sbin
	mkdir -p $(DESTDIR)/usr/lib/systemd/system/
	cp uncloud-init $(DESTDIR)/usr/sbin/uncloud-init
	cp uncloud-init.service $(DESTDIR)/usr/lib/systemd/system/uncloud-init.service

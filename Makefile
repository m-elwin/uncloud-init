# Don't need to do anything to build, but debian will do this step
uncloud-init:
	@echo "Built uncloud-init. run make install to install"

# Copy the files to the expected locations
install:
	mkdir -p $(DESTDIR)/sbin
	mkdir -p $(DESTDIR)/lib/systemd/system
	cp uncloud-init $(DESTDIR)/sbin/uncloud-init
	cp uncloud-init.service $(DESTDIR)/lib/systemd/system/uncloud-init.service

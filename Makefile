# Copy the files to the expected locations
install:
	cp uncloud-init.py $(DESTDIR)/usr/sbin/uncloud-init.py
	cp uncloud-init.service $(DESTDIR)/usr/lib/systemd/system/uncloud-init.service

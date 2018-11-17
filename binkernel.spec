Name: kernel
Summary: The Linux Kernel
Version: 4.19.2_HP_Envy_x360_bq1xx
Release: 1
License: GPL
Group: System Environment/Kernel
Vendor: The Linux Community
URL: http://www.kernel.org
Provides:  kernel-4.19.2-HP-Envy-x360-bq1xx
%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define debug_package %{nil}

%description
The Linux Kernel, the operating system core itself

%package headers
Summary: Header files for the Linux kernel for use by glibc
Group: Development/System
Obsoletes: kernel-headers
Provides: kernel-headers = %{version}
%description headers
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%install
mkdir -p %{buildroot}/boot
%ifarch ia64
mkdir -p %{buildroot}/boot/efi
cp $(make image_name) %{buildroot}/boot/efi/vmlinuz-4.19.2-HP-Envy-x360-bq1xx
ln -s efi/vmlinuz-4.19.2-HP-Envy-x360-bq1xx %{buildroot}/boot/
%else
cp $(make image_name) %{buildroot}/boot/vmlinuz-4.19.2-HP-Envy-x360-bq1xx
%endif
make %{?_smp_mflags} INSTALL_MOD_PATH=%{buildroot} KBUILD_SRC= modules_install
make %{?_smp_mflags} INSTALL_HDR_PATH=%{buildroot}/usr KBUILD_SRC= headers_install
cp System.map %{buildroot}/boot/System.map-4.19.2-HP-Envy-x360-bq1xx
cp .config %{buildroot}/boot/config-4.19.2-HP-Envy-x360-bq1xx
bzip2 -9 --keep vmlinux
mv vmlinux.bz2 %{buildroot}/boot/vmlinux-4.19.2-HP-Envy-x360-bq1xx.bz2

%clean
rm -rf %{buildroot}

%post
if [ -x /sbin/installkernel -a -r /boot/vmlinuz-4.19.2-HP-Envy-x360-bq1xx -a -r /boot/System.map-4.19.2-HP-Envy-x360-bq1xx ]; then
cp /boot/vmlinuz-4.19.2-HP-Envy-x360-bq1xx /boot/.vmlinuz-4.19.2-HP-Envy-x360-bq1xx-rpm
cp /boot/System.map-4.19.2-HP-Envy-x360-bq1xx /boot/.System.map-4.19.2-HP-Envy-x360-bq1xx-rpm
rm -f /boot/vmlinuz-4.19.2-HP-Envy-x360-bq1xx /boot/System.map-4.19.2-HP-Envy-x360-bq1xx
/sbin/installkernel 4.19.2-HP-Envy-x360-bq1xx /boot/.vmlinuz-4.19.2-HP-Envy-x360-bq1xx-rpm /boot/.System.map-4.19.2-HP-Envy-x360-bq1xx-rpm
rm -f /boot/.vmlinuz-4.19.2-HP-Envy-x360-bq1xx-rpm /boot/.System.map-4.19.2-HP-Envy-x360-bq1xx-rpm
fi

%preun
if [ -x /sbin/new-kernel-pkg ]; then
new-kernel-pkg --remove 4.19.2-HP-Envy-x360-bq1xx --rminitrd --initrdfile=/boot/initramfs-4.19.2-HP-Envy-x360-bq1xx.img
elif [ -x /usr/bin/kernel-install ]; then
kernel-install remove 4.19.2-HP-Envy-x360-bq1xx
fi

%postun
if [ -x /sbin/update-bootloader ]; then
/sbin/update-bootloader --remove 4.19.2-HP-Envy-x360-bq1xx
fi

%files
%defattr (-, root, root)
/lib/modules/4.19.2-HP-Envy-x360-bq1xx
%exclude /lib/modules/4.19.2-HP-Envy-x360-bq1xx/build
%exclude /lib/modules/4.19.2-HP-Envy-x360-bq1xx/source
/boot/*

%files headers
%defattr (-, root, root)
/usr/include

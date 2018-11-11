# Jenkins-Compile-Kernel-for-HP-ENVY-x360-Convertible-15-bq1xx-with-Touchscreen-Support
Jenkins Pipeline for Automated Kernel Compilation for HP ENVY x360 Convertible 15-bq1xx with Touchscreen Support

This is all based on https://bugzilla.kernel.org/show_bug.cgi?id=198715#c14


Successful build 11-11-18 - System boots, Touchscreen working

Note the installed kernel is not installing as the 1st kernel in Grub. 





=========================================================================================================
Build Environment

CentOS Linux release 7.5.1804 (Core) running jenkins-2.138.3-1.1.noarch and java-1.8.0-openjdk-devel

Jenkins Server is a qumu/kvm guest with 2xvCPU and 2GB RAM

/jenkins/kernel virtual disk mounted from ssd on host

=========================================================================================================

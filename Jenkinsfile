timestamps {

node () {

stage ('Downloading Kernel Source') {
sh """
cd /jenkins/kernel/
 if [[ ! -e linux-4.19.2 ]]; then
	wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.19.2.tar.xz
	tar -xf linux-4.19.2.tar.xz
	fi
"""

}
	stage ('Install build dependencies') {
		sh """
		cd /jenkins/kernel/linux-4.19.2
		sudo yum install -y yum-utils
		sudo yum-builddep kernel.spec -y
		sudo yum-builddep binkernel.spec -y
		sudo yum-builddep kernel -y
		"""
	}
	stage ('Apply patch to kernel source') {
		sh """
		cd /jenkins/kernel/linux-4.19.2
		sudo patch -p1 -i "${env.WORKSPACE}@script/hp-acpi-hack.patch"
"""
}
stage ('Update .config') {
	sh """
	cd /jenkins/kernel/linux-4.19.2
  sudo cp -f "${env.WORKSPACE}@script/config" ./.config
	sudo make olddefconfig
	"""
}
stage ('Add Displaylink support') {
	sh """
  echo testing

	"""
}
	stage ('Compile Kernel') {
		sh """
		cd /jenkins/kernel/linux-4.19.2
		# sudo make binrpm-pkg -j 2
    sudo make clean
    sudo make rpm-pkg -j 2
"""
}
	stage ('Cleanup') {
		sh """
		cd /jenkins/kernel/linux-4.19.2
		sudo patch -p1 -i "${env.WORKSPACE}@script/hp-acpi-hack.patch" -R
    # sudo make distclean
"""
	}
}
}

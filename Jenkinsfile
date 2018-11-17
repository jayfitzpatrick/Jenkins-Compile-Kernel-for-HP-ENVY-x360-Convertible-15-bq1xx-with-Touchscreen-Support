timestamps {

node () {

//	stage ('Download Latest Stable Kernel from GIT') {
// sh """
// cd /jenkins/kernel/
// if [[ ! -e linux-stable ]]; then
// git clone git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
// cd linux-stable
// git checkout -b linux-4.19.y
// git fetch
// touch .scmversion
// # cp "${env.WORKSPACE}@script/binkernel.spec" ./
//
// fi
// cd linux-stable
//  """
// 	}

//	stage ('Switching Kernel Version') {
//	sh """
//	 cd /jenkins/kernel/linux-stable/
//	 if [[ ! -e v4.19.2 ]]; then
//	 	sudo make mrproper
//		sudo 	make clean
//		git checkout -b v4.19.2
// 		git fetch
// 	touch v4.19.2
// fi
//	 """
// }

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
		cd /jenkins/kernel/linux-stable
		sudo yum install -y yum-utils
		sudo yum-builddep kernel.spec -y
		sudo yum-builddep binkernel.spec -y
		sudo yum-builddep kernel -y
		"""
	}
	stage ('Apply patch to kernel source') {
		sh """
		cd /jenkins/kernel/linux-4.19.2
		patch -p1 -i "${env.WORKSPACE}@script/hp-acpi-hack.patch"
"""
}
stage ('Update .config') {
	sh """
	cd /jenkins/kernel/linux-4.19.2
  sudo make mrproper
	cp -f "${env.WORKSPACE}@script/config" ./.config
	sudo make olddefconfig
	"""
}
	stage ('Compile Kernel') {
		sh """
		cd /jenkins/kernel/linux-4.19.2
		sudo make binrpm-pkg -j 2
"""
}
	stage ('Cleanup') {
		sh """
		cd /jenkins/kernel/linux-4.19.2
		patch -p1 -i "${env.WORKSPACE}@script/hp-acpi-hack.patch" -R
"""
	}
}
}

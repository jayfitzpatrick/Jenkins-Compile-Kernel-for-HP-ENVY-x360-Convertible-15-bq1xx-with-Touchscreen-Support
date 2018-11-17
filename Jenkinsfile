timestamps {

node () {

	stage ('Download Latest Stable Kernel from GIT') {
 		env.myVar='findme'
sh """
cd /jenkins/kernel/
if [[ ! -e linux-stable ]]; then
git clone git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
cd linux-stable
git checkout stable
git fetch
touch .scmversion

fi
cd linux-stable

 """
	}
//	stage ('Switching Kernel Version') {
//		sh """
//		 cd /jenkins/kernel/linux-stable/
//		 if [[ ! -e v4.19.2 ]]; then
//	 git checkout -b v4.19.2
//	 git fetch
//	 touch v4.19.2
//	 fi
//		 """
}
	stage ('Install build dependencies') {
		sh """
		cd /jenkins/kernel/linux-stable
		sudo yum install -y yum-utils
		sudo yum-builddep kernel.spec -y
		sudo yum-builddep kernel -y
		"""
	}
	stage ('Apply patch to kernel source') {
		sh """
		cd /jenkins/kernel/linux-stable
		git checkout stable
		git fetch
		patch -p1 -i "${env.WORKSPACE}@script/hp-acpi-hack.patch"
"""
}
stage ('Update .config') {
	sh """
	cd /jenkins/kernel/linux-stable
	cp -f "${env.WORKSPACE}@script/config" ./.config
	sudo make olddefconfig
	"""
}
	stage ('Compile Kernel') {
		sh """
		cd /jenkins/kernel/linux-stable
		sudo make binrpm-pkg -j 2
"""
}
	stage ('Cleanup') {
		sh """
		cd /jenkins/kernel/linux-stable
		patch -p1 -i "${env.WORKSPACE}@script/hp-acpi-hack.patch" -R
"""
	}
}
}

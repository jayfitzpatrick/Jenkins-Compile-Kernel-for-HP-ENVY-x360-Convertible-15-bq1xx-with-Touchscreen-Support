timestamps {

node () {

	stage ('Download Latest Stable Kernel from GIT') {
 		env.myVar='findme'
sh """
cd /jenkins/kernel/
if [[ ! -e linux-stable ]]; then
git clone git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
cd linux-stable
git checkout -b stable v4.19.2
git pull
touch .scmversion

fi
cd linux-stable

 """
	}
	stage ('Switching Kernel Version') {
		sh """
		 cd /jenkins/kernel/
	 git checkout -b stable v4.19.2
		 """
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
		git pull
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

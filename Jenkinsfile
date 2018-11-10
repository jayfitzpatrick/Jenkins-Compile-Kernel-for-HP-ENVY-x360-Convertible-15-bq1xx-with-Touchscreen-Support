timestamps {

node () {

	stage ('Download Latest Stable Kernel from GIT') {
 		env.myVar='findme'
sh """
cd /jenkins/kernel/
if [[ ! -e linux-stable ]]; then
git clone git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
fi
cd linux-stable
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
def workspace = pwd()
		sh """
		cd /jenkins/kernel/linux-stable
		patch -p1 -i "${env.WORKSPACE}/hp-acpi-hack.patch"
"""
stage ('Update .config') {
	sh """
	cd /jenkins/kernel/linux-stable
	sudo cp -f "${env.WORKSPACE}/.config" ./
	"""
	stage ('Cleanup') {
		sh """
		cd /jenkins/kernel/linux-stable
		patch -p1 -i "${env.WORKSPACE}/hp-acpi-hack.patch" -R
"""
	}
}
}
}
}

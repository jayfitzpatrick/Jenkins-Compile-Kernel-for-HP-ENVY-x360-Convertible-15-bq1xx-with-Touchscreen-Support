// Powered by Infostretch

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
git tag -l | less
git checkout -b stable v4.19.1
git pull
logger "${env.myVar}"
 """
	}
	stage ('Apply patch to kernel source') {
			patch -p1 -i "${env.WORKSPACE}\hp-acpi-hack.patch"
	}
}
}

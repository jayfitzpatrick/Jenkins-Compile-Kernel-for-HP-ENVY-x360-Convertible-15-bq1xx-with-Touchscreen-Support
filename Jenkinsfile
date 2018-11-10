// Powered by Infostretch

timestamps {

node () {

	stage ('Download Latest Stable Kernel and Touchscreen Patch') {
 		env.myVar='findme'
sh """
cd /jenkins/kernel/
git clone git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
cd linux-stable

sudo wget https://raw.githubusercontent.com/jayfitzpatrick/Jenkins-Compile-Kernel-for-HP-ENVY-x360-Convertible-15-bq1xx-with-Touchscreen-Support/master/hp-acpi-hack.patch -O /jenkins/kernel/hp-acpi-hack.patch
logger "${env.myVar}"
 """
	}
}
}

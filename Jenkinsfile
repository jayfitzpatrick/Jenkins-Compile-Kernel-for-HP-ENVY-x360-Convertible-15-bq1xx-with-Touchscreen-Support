pipeline {
    agent any
    environment {
        KBUILD = "4.19.4"
    }

    // ----------------

    stages {
        stage('Compiling Kernel') {
            steps {
                script {
                    sh """
                    cd /jenkins/kernel/
                     if [[ ! -e linux-"${KBUILD}" ]]; then
                    	wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-"${KBUILD}".tar.xz
                    	tar -xf linux-"${KBUILD}".tar.xz
                    	fi
                      cd linux-"${KBUILD}"
                      sudo yum install -y yum-utils rsync
                      sudo yum-builddep kernel.spec -y
                      sudo yum-builddep binkernel.spec -y
                      sudo yum-builddep kernel -y
                      sudo patch -p1 -i "${env.WORKSPACE}@script/hp-acpi-hack.patch"


                      if [[ ! -e /jenkins/kernel/linux-"${KBUILD}"/drivers/video/displaylink  ]]; then
                        sudo mkdir /jenkins/kernel/linux-"${KBUILD}"/drivers/video/displaylink -p
                    fi
                      sudo cp -f "${env.WORKSPACE}@script/evdi_Kconfig" /jenkins/kernel/linux-"${KBUILD}"/drivers/video/displaylink/Kconfig
                      sudo cp -f "${env.WORKSPACE}@script/config" ./.config
                      sudo make olddefconfig

                      rm -Rf evdi
                      git clone https://github.com/DisplayLink/evdi.git

                      sudo rsync -a evdi/* /jenkins/kernel/linux-"${KBUILD}"/drivers/video/displaylink/
                      grep -q -F 'obj-\$(CONFIG_STM)   += video/displaylink/' /jenkins/kernel/linux-"${KBUILD}"/drivers/Makefile || echo 'obj-\$(CONFIG_STM)   += video/displaylink/' >> /jenkins/kernel/linux-"${KBUILD}"/drivers/Makefile
                    grep -q -F 'source "drivers/video/displaylink/Kconfig"' /jenkins/kernel/linux-"${KBUILD}"/drivers/Kconfig || echo 'source "drivers/video/displaylink/Kconfig"' >> /jenkins/kernel/linux-"${KBUILD}"/drivers/Kconfig
                    # sudo make binrpm-pkg -j 2
                    sudo make clean
                    sudo make rpm-pkg -j 2
                    sudo patch -p1 -i "${env.WORKSPACE}@script/hp-acpi-hack.patch" -R
                    # sudo make distclean
                  """

                }
            }
        }
    }
}

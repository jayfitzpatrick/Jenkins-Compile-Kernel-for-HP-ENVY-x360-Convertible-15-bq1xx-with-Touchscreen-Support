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

Missing drivers
Sensors ●
Accelerometer (2: 1 for hard drive protection/CoolSense , 1 for display panel rotation detection to lock
keyboard and ClickPad function; STMicro HP2DCTR×2)
● Gyroscope / E-compass / Accelerometer (ST Micro HP9DS1TR)

Unable to find any source for these 

=========================================================================================================

Outstanding issues: (both were in place on last running kernel 4.18.17-200.fc28.x86_64)



Crash while using Display port adaptor over USB-C port connected to a Dell k17a docking station

Poss related to this: http://www.displaylink.com/downloads/ubuntu
and This
https://github.com/displaylink-rpm/displaylink-rpm.git


[drm] DM_MST: starting TM on aconnector: 0000000003f57a9e [id: 54]
[ 1619.498450] [drm] DM_MST: reusing connector: 00000000edb91c42 [id: 80] [master: 0000000003f57a9e]
[ 1619.498464] [drm] DM_MST: reusing connector: 000000004cfc8169 [id: 83] [master: 0000000003f57a9e]
[ 1619.498468] [drm] DM_MST: reusing connector: 00000000af74c3ed [id: 86] [master: 0000000003f57a9e]
[ 1622.000915] WARNING: CPU: 4 PID: 1324 at drivers/gpu/drm/amd/amdgpu/../display/dc/core/dc_link_dp.c:879 perform_clock_recovery_sequence+0x1f4/0x2a0 [amdgpu]
[ 1622.000918] Modules linked in: ccm fuse xt_CHECKSUM ipt_MASQUERADE tun rfcomm nf_nat_tftp nf_conntrack_tftp xt_CT ip6t_rpfilter ip6t_REJECT nf_reject_ipv6 xt_conntrack devlink ip_set nfnetlink ebtable_nat ebtable_broute bridge stp llc ip6table_nat nf_nat_ipv6 ip6table_mangle ip6table_raw ip6table_security iptable_nat nf_nat_ipv4 nf_nat nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 iptable_mangle iptable_raw iptable_security ebtable_filter ebtables ip6table_filter ip6_tables bnep sunrpc dm_cache_smq vfat fat dm_cache dm_bio_prison dm_persistent_data amdkfd amd_iommu_v2 amdgpu arc4 r8822be(C) mac80211 uvcvideo chash btusb i2c_algo_bit gpu_sched btrtl drm_kms_helper btbcm hid_sensor_gyro_3d hid_sensor_accel_3d btintel hid_sensor_magn_3d hid_sensor_rotation hid_sensor_incl_3d videobuf2_vmalloc hid_sensor_trigger
[ 1622.000956]  videobuf2_memops hid_sensor_iio_common wmi_bmof bluetooth snd_hda_codec_realtek industrialio_triggered_buffer videobuf2_v4l2 kfifo_buf snd_hda_codec_generic snd_hda_codec_hdmi videobuf2_common industrialio kvm_amd videodev snd_hda_intel ttm cfg80211 kvm media snd_hda_codec hp_wmi snd_hwdep drm snd_hda_core ecdh_generic sparse_keymap snd_seq irqbypass crct10dif_pclmul crc32_pclmul snd_seq_device snd_pcm ghash_clmulni_intel snd_timer joydev snd rtsx_pci_ms memstick sp5100_tco rfkill soundcore i2c_piix4 k10temp wmi hp_accel video lis3lv02d input_polldev pinctrl_amd pcc_cpufreq hp_wireless i2c_scmi acpi_cpufreq binfmt_misc xfs libcrc32c rtsx_pci_sdmmc mmc_core crc32c_intel hid_sensor_hub rtsx_pci serio_raw i2c_hid
[ 1622.001004] CPU: 4 PID: 1324 Comm: Xorg Tainted: G        WC        4.19.1-HP-Envy-x360-bq1xx+ #9
[ 1622.001005] Hardware name: HP HP ENVY x360 Convertible 15-bq1xx/83C6, BIOS F.17 03/29/2018
[ 1622.001044] RIP: 0010:perform_clock_recovery_sequence+0x1f4/0x2a0 [amdgpu]
[ 1622.001046] Code: 07 89 54 03 14 48 83 c0 0c 48 39 c8 75 de 83 44 24 04 01 40 84 f6 74 0b 83 7c 24 04 63 0f 86 8f fe ff ff 83 7c 24 04 63 76 1c <0f> 0b ba 64 00 00 00 48 c7 c6 40 7f fa c0 48 c7 c7 e0 d8 fc c0 31
[ 1622.001047] RSP: 0018:ffff9d49836a36a0 EFLAGS: 00010202
[ 1622.001049] RAX: 0000000000000018 RBX: ffff9d49836a3780 RCX: 0000000000000018
[ 1622.001050] RDX: 0000000000000000 RSI: 0000000000000001 RDI: 0000000000000002
[ 1622.001050] RBP: ffff898994a3ce00 R08: ffff9d49836a36c8 R09: 0000000000000010
[ 1622.001051] R10: ffffd31284c05840 R11: 0000000000000002 R12: ffff9d49836a36fc
[ 1622.001052] R13: ffff9d49836a3700 R14: 0000000000000002 R15: ffff9d49836a3704
[ 1622.001054] FS:  00007f180c9e2ac0(0000) GS:ffff898996f00000(0000) knlGS:0000000000000000
[ 1622.001055] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 1622.001055] CR2: 000055f0e7fe4548 CR3: 0000000208e46000 CR4: 00000000003406e0
[ 1622.001057] Call Trace:
[ 1622.001100]  dc_link_dp_perform_link_training+0x68/0x230 [amdgpu]
[ 1622.001109]  ? drm_dp_dpcd_access+0xd5/0x100 [drm_kms_helper]
[ 1622.001145]  perform_link_training_with_retries+0x4e/0x70 [amdgpu]
[ 1622.001180]  enable_link_dp+0x160/0x280 [amdgpu]
[ 1622.001220]  ? dm_helpers_dp_write_dpcd+0x27/0x40 [amdgpu]
[ 1622.001253]  ? core_link_write_dpcd+0x1f/0x30 [amdgpu]
[ 1622.001286]  core_link_enable_stream+0x2f7/0xc70 [amdgpu]
[ 1622.001321]  dce110_apply_ctx_to_hw+0x646/0x660 [amdgpu]
[ 1622.001356]  dc_commit_state+0x2c0/0x590 [amdgpu]
[ 1622.001388]  ? set_freesync_on_streams+0xf0/0x2f0 [amdgpu]
[ 1622.001424]  ? mod_freesync_set_user_enable+0x173/0x1c0 [amdgpu]
[ 1622.001463]  amdgpu_dm_atomic_commit_tail+0x38f/0xdc0 [amdgpu]
[ 1622.001500]  ? amdgpu_dm_atomic_check+0x3b1/0x3e0 [amdgpu]
[ 1622.001507]  ? _cond_resched+0x15/0x30
[ 1622.001509]  ? wait_for_completion_timeout+0x3a/0x180
[ 1622.001515]  commit_tail+0x3d/0x70 [drm_kms_helper]
[ 1622.001522]  drm_atomic_helper_commit+0x10d/0x120 [drm_kms_helper]
[ 1622.001527]  drm_atomic_helper_set_config+0x5c/0x90 [drm_kms_helper]
[ 1622.001543]  drm_mode_setcrtc+0x5b2/0x610 [drm]
[ 1622.001554]  ? drm_mode_getcrtc+0x170/0x170 [drm]
[ 1622.001562]  drm_ioctl_kernel+0xaa/0xf0 [drm]
[ 1622.001572]  drm_ioctl+0x39e/0x400 [drm]
[ 1622.001580]  ? drm_mode_getcrtc+0x170/0x170 [drm]
[ 1622.001603]  amdgpu_drm_ioctl+0x46/0x80 [amdgpu]
[ 1622.001608]  do_vfs_ioctl+0xa9/0x620
[ 1622.001611]  ksys_ioctl+0x60/0x90
[ 1622.001613]  __x64_sys_ioctl+0x16/0x20
[ 1622.001617]  do_syscall_64+0x5b/0x170
[ 1622.001621]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
[ 1622.001623] RIP: 0033:0x7f1809c69c57
[ 1622.001625] Code: 00 00 90 48 8b 05 49 82 2c 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 2e 0f 1f 84 00 00 00 00 00 b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 19 82 2c 00 f7 d8 64 89 01 48
[ 1622.001626] RSP: 002b:00007fff4ddd9358 EFLAGS: 00003246 ORIG_RAX: 0000000000000010
[ 1622.001627] RAX: ffffffffffffffda RBX: 00007fff4ddd9390 RCX: 00007f1809c69c57
[ 1622.001628] RDX: 00007fff4ddd9390 RSI: 00000000c06864a2 RDI: 0000000000000017
[ 1622.001629] RBP: 00007fff4ddd9390 R08: 0000000000000000 R09: 00000000011dab40
[ 1622.001630] R10: 00007fff4ddd9450 R11: 0000000000003246 R12: 00000000c06864a2
[ 1622.001630] R13: 0000000000000017 R14: 0000000000000000 R15: 00000000011dab40
[ 1622.001632] ---[ end trace c6767203f1de790d ]---

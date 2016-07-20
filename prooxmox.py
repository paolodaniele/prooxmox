#!/usr/bin/python

import os
import sys, traceback
import socket

def main():
	try:
		print '''
__________                                           
\______   \_______  _______  ___ _____   _______  ___
 |     ___/\_  __ \/  _ \  \/  //     \ /  _ \  \/  /
 |    |     |  | \(  <_> >    <|  Y Y  (  <_> >    < 
 |____|     |__|   \____/__/\_ \__|_|  /\____/__/\_ \
 \033[1;m


 \033[1;32m+ -- -- +=[ Author: Paolo Daniele | Homepage: www.paolodaniele.it\033[1;m

		'''
		def start1():
			while True:
				print '''
1) Add Proxmox repositories & Update 
2) Install Proxmox
3) Help
4) Reboot System
5) Exit

			'''

				option0 = raw_input("\033[1;36mprox > \033[1;m")
			
				while option0 == "1":
					print '''
1) Debian Jessie
2) Debian Wheezy
3) Update
4) Remove all Proxmox linux repositories
5) View the contents of sources.list file

					'''
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("wget -O- 'http://download.proxmox.com/debian/key.asc' | apt-key add -")
						cmd2 = os.system("echo '# Proxmox repositories | Added by Prooxmox\ndeb http://download.proxmox.com/debian jessie pve-no-subscription' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("wget -O- 'http://download.proxmox.com/debian/key.asc' | apt-key add -")
                                                cmd4 = os.system("echo '# Proxmox repositories | Added by Prooxmox\ndeb http://download.proxmox.com/debian wheezy pve-no-subscription' >> /etc/apt/sources.list")
					elif repo == "3":
						cmd3 = os.system("apt-get update -m")
					elif repo == "4":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Proxmox repositories | Added by Prooxmox\n", "deb http://download.proxmox.com/debian jessie pve-no-subscription\n","deb http://download.proxmox.com/debian wheezy pve-no-subscription\n"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print " "
						print "\033[1;31mAll Proxmox repositories have been deleted !\033[1;m"
						print " "
					elif repo == "back":
						start1()
					elif repo == "gohome":
						start1()
					elif repo == "5":
						file = open('/etc/apt/sources.list', 'r')

						print file.read()

					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						

				if option0 == "3":
					print ''' 
****************** +Commands+ ******************


\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m

		'''
				if option0 == "4":
					os.system('/sbin/shutdown -r now')
				if option0 == "5":
					sys.exit(0)

				def start():
					while option0 == "2":
						print '''
\033[1;36m**************************** Proxmox Installation begin *****************************\033[1;m
	1) Install Proxmox on Debian Jessie
	2) Install Proxmox on Debian Wheezy part 1
	3) Install Proxmox on Debian Wheezy part 2 (after reboot)

	This version add a phantom ip address to get proxmox installation valid, when it's over you can change with your real ip address

			 '''
						print "\033[1;32mSelect your distro to begin install Proxmox VE .\033[1;m"

						print " "
						option1 = raw_input("\033[1;36mprox > \033[1;m")
						if option1 == "back":
							start1()
						elif option1 == "gohome":
							start1()
						if option1 == "1":
							name = socket.gethostname()
							cmd = os.system("echo '10.70.1.200  " + name + " pvelocalhost' >> /etc/hosts")
							cmd1 = os.system("apt-get install proxmox-ve ntp ssh postfix ksm-control-daemon open-iscsi systemd-sysv")	
						if option1 == "2":
							name = socket.gethostname()
							cmd2 = os.system("echo '10.70.1.200  " + name + " pvelocalhost' >> /etc/hosts")
                                                        cmd3 = os.system("apt-get install pve-firmware pve-kernel-2.6.32-26-pve")
							cmd4 = os.system("apt-get install pve-headers-2.6.32-26-pve")
							cmd5 = os.system("apt-get install proxmox-ve-2.6.32 ntp ssh lvm2 postfix ksm-control-daemon vzprocps open-iscsi bootlogd")
						if option1 == "3":
							cmd6 = os.system("apt-get install proxmox-ve-2.6.32 ntp ssh lvm2 postfix ksm-control-daemon vzprocps open-iscsi bootlogd")

				start()
		start1()
	except KeyboardInterrupt:
		print "Shutdown requested...Goodbye..."
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()

#! /usr/bin/env python

from netmiko import ConnectHandler

output = {}


DLL = {
        'device_type' : 'linux',
        'username' : 'khir',
        'password' : 'khir',
        'host' : '172.16.218.1',
	}
dell = ConnectHandler(**DLL)

Host_1 = {
        'device_type' : 'linux',
        'username' : 'khir',
        'password' : 'khir',
        'host' : '192.168.122.38',
	}
dell = ConnectHandler(**DLL)
hst1 = ConnectHandler(**Host_1)

def IP_MAC():
	pass = "khir"
	Dhcp_lease = "sudo virsh net-dhcp-leases default"
	
	Res = dell.send_command("echo %s | sudo -S %s" %(pass, Dhcp_lease))
	
	#save the IP Address to MAC mapping in the dictionary
	for row in Res[2:]:
        output[row.split()[2]] = (row.split()[4]).split('/')[0]
	print (output)
	
        #set the static arp entry for each dictionary key value pair mapping
        for items in output:
             Static_Entry = "sudo arp -s "+ items + " " + output[items]

             Mac_entry = hst1.send_command("echo %s | sudo -S %s" %(pass, Static_Entry)


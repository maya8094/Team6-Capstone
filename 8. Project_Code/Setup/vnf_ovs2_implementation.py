import os


''' The Interface IPs + Networks can be fetched using the ifconfig 
    enp0s3_ip = 192.168.122.38 
    enp0s3_net = 192.168.122.0/24
    enp0s8_ip = 192.168.29.68 
    enp0s8_net = 192.168.29.0/24 '''
	
default_gw = '192.168.122.1' 
malc_ip = '192.168.29.99' 
CEO_ip = '192.168.29.55' 
h2_eth1_ip = '192.168.29.176' 
test_vm_ip = '192.168.29.7'
suspicious_ip = '192.168.112.99'

# enp0s3 - Interface IP Address
enp0s3_ip = " ifconfig enp0s3 | grep 'inet addr:' | awk '{ print $2 }' "
enp0s3_ip = (os.popen(enp0s3_ip)).read()
enp0s3_ip = (enp0s3_ip.split(':'))[1]
enp0s3_ip = str(enp0s3_ip.replace('\n',''))
#  enp0s3 - Network IP Address
enp0s3_mask = " ifconfig enp0s3 | grep 'Mask:' | awk '{ print $4 }' "
enp0s3_mask = (os.popen(enp0s3_mask)).read()
enp0s3_mask = (enp0s3_mask.split(':'))[1]
enp0s3_mask = enp0s3_mask.replace('\n','')
if enp0s3_mask == "255.255.255.0":
        temp1 = enp0s3_ip.split('.')
        temp1[3] = '0'
        enp0s3_net = '.'.join(temp1)
	enp0s3_net = str(enp0s3_net + '/24')

# enp0s8 - Interface IP Address
enp0s8_ip = " ifconfig enp0s8 | grep 'inet addr:' | awk '{ print $2 }' "
enp0s8_ip = (os.popen(enp0s8_ip)).read()
enp0s8_ip = (enp0s8_ip.split(':'))[1]
enp0s8_ip = str(enp0s8_ip.replace('\n',''))
#  enp0s8 - Network IP Address
enp0s8_mask = " ifconfig enp0s8 | grep 'Mask:' | awk '{ print $4 }' "
enp0s8_mask = (os.popen(enp0s8_mask)).read()
enp0s8_mask = (enp0s8_mask.split(':'))[1]
enp0s8_mask = enp0s8_mask.replace('\n','')
if enp0s8_mask == "255.255.255.0":
        temp2 = enp0s8_ip.split('.')
        temp2[3] = '0'
        enp0s8_net = '.'.join(temp2)
	enp0s8_net = str(enp0s8_net + '/24')


''' VNF Flow Entries on Open vSwitch - vswitch2 
   table1 is Firewall VNF
   table2 is QoS VNF
   table5 is VLAN VNF '''

os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=0,cookie=100,priority=1200,in_port=2,actions=goto_table:1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=0,cookie=101,priority=1201,in_port=1,actions=goto_table:1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=163,priority=307,arp,in_port=1,nw_dst='+malc_ip+',actions=drop" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=164,priority=308,ip,in_port=1,nw_dst='+malc_ip+',actions=drop" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=165,priority=309,arp,in_port=1,nw_src='+malc_ip+',actions=drop" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=166,priority=310,ip,in_port=1,nw_src='+malc_ip+',actions=drop" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=167,priority=312,tcp:'+h2_eth1_ip+',in_port=1,nw_dst='+h2_eth1_ip+',tp_dst=22,actions=drop" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=168,priority=313,tcp:'+h2_eth1_ip+',in_port=1,nw_dst='+suspicious_ip+',tcp_dst=80,actions=drop" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=169,priority=330,ip,in_port=1,nw_dst=4.4.4.4,actions=drop" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=299,priority=115,arp,in_port=2,nw_dst='+default_gw+',actions=goto_table:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=298,priority=115,ip,in_port=2,nw_dst='+default_gw+',actions=goto_table:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=297,priority=115,arp,in_port=1,nw_src='+default_gw+',actions=goto_table:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=296,priority=115,ip,in_port=1,nw_src='+default_gw+',actions=goto_table:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=204,priority=113,arp,in_port=1,nw_src='+enp0s8_ip+',nw_dst='+enp0s8_net+',actions=goto_table:5" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=215,priority=116,ip,in_port=1,nw_src='+enp0s8_ip+',nw_dst='+enp0s8_net+',actions=goto_table:5" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=205,priority=114,ip,in_port=2,nw_src='+enp0s8_net+',nw_dst='+enp0s8_ip+',actions=goto_table:5" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=214,priority=115,arp,in_port=2,nw_src='+enp0s8_net+',nw_dst='+enp0s8_ip+',actions=goto_table:5" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=271,priority=150,ip,in_port=1,nw_dst='+CEO_ip+',actions=goto_table:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=272,priority=151,ip,in_port=1,nw_src='+CEO_ip+',actions=goto_table:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=273,priority=21,actions=goto_table:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=281,priority=152,arp,in_port=1,nw_dst='+CEO_ip+',actions=goto_table:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=282,priority=153,arp,in_port=1,nw_src='+CEO_ip+',actions=goto_table:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=244,priority=143,arp,in_port=1,nw_dst='+enp0s3_net+',actions=output:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=245,priority=146,ip,in_port=1,nw_dst='+enp0s3_net+',actions=output:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=249,priority=144,ip,in_port=2,nw_dst='+enp0s3_ip+',actions=output:1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=250,priority=145,arp,in_port=2,nw_dst='+enp0s3_ip+',actions=output:1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=247,priority=147,ip,in_port=1,nw_dst='+test_vm_ip+',actions=output:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=248,priority=148,arp,in_port=1,nw_dst='+test_vm_ip+',actions=output:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=287,priority=147,ip,in_port=2,nw_src='+test_vm_ip+',actions=output:1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=288,priority=148,arp,in_port=2,nw_src='+test_vm_ip+',actions=output:1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=261,priority=161,ip,in_port=2,nw_dst='+default_gw+',actions=output:1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=262,priority=162,arp,in_port=2,nw_dst='+default_gw+',actions=output:1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=277,priority=10,ip,in_port=1,nw_src='+enp0s8_ip+',actions=goto_table:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=1,cookie=278,priority=10,ip,in_port=1,nw_src='+enp0s3_ip+',actions=goto_table:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=2,cookie=381,priority=250,arp,in_port=1,nw_dst='+CEO_ip+',actions=set_queue:3,output:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=2,cookie=382,priority=251,arp,in_port=1,nw_src='+CEO_ip+',actions=set_queue:3,output:1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=2,cookie=371,priority=250,ip,in_port=1,nw_dst='+CEO_ip+',actions=set_queue:3,output:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=2,cookie=372,priority=251,ip,in_port=1,nw_src='+CEO_ip+',actions=set_queue:3,output:1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=2,cookie=377,priority=200,ip,in_port=1,nw_src='+enp0s8_ip+',actions=set_queue:2,output:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=2,cookie=378,priority=200,ip,in_port=1,nw_src='+enp0s3_ip+',actions=set_queue:2,output:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=2,cookie=385,priority=20,in_port=1,actions=set_queue:2,output:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=2,cookie=386,priority=20,in_port=2,actions=set_queue:2,output:1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=5,cookie=541,priority=501,in_port=1,vlan_tci=0,actions=mod_vlan_vid:20,output:2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=5,cookie=543,priority=503,in_port=2,dl_vlan=20,actions=strip_vlan,output:1" ')



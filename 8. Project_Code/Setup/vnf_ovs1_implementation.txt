import os


''' VNF Flow Entries on Open vSwitch - vswitch1 '''

# Traffic from Default br0 Bridge Redirected to br-traffic Bridge
os.system('  docker exec -it vswitch1 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=0,cookie=110,priority=20,in_port=1,actions=output:2" ')
os.system('  docker exec -it vswitch1 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=0,cookie=111,priority=20,in_port=2,actions=output:1" ')
# ARP VNF Flow Entry which directs to the SDN Controller running ARP Application   
os.system('  docker exec -it vswitch1 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=0,cookie=108,priority=427,in_port=1,arp,actions=CONTROLLER:65535" ')
# DNS VNF Flow Entry which directs to the SDN Controller running DNS Application 
os.system('  docker exec -it vswitch1 /bin/sh -c "ovs-ofctl add-flow br-data -O OpenFlow13 table=0,cookie=109,priority=428,udp,in_port=1,tp_dst=53,actions=CONTROLLER:65535" ')


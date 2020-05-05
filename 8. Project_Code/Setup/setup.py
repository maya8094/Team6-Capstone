import os


''' Bridge Creation on the Host VM '''

os.system('ovs-vsctl add-br br0')
os.system('ovs-vsctl add-br br-sdn')
os.system('ovs-vsctl add-br br-traffic')
os.system('ovs-vsctl add-br br-conn')


''' Bridge Activation on the Host VM 
    Creation of Three Bridges 
    br0 is the Host Bridge
    br-sdn is the Bridge for SDN Infrastructure Communication
    br-traffic is the Bridge for Traffic 
    br-conn is the Bridge Connecting two Open vSwitches'''

os.system('ifconfig br0 up')
os.system('ifconfig br-sdn up')
os.system('ifconfig br-traffic up')
os.system('ifconfig br-conn up')


''' Initiate Open vSwitches on Docker Containers '''

os.system('docker run -i -t --rm --name vswitch1 --cap-add=NET_ADMIN -d globocom/openvswitch')
os.system('docker run -i -t --rm --name vswitch2 --cap-add=NET_ADMIN -d globocom/openvswitch')


''' Connecting Bridges with Open vSwitch - vswitch1 Docker Interfaces '''

os.system('ovs-docker add-port br0 eth1 vswitch1')
os.system('ovs-docker add-port br-traffic eth2 vswitch1')
os.system('ovs-docker add-port br-sdn eth4 vswitch1')
os.system('ovs-docker add-port br-conn eth3 vswitch1')


''' Connecting Bridges with Open vSwitch - vswitch2 Docker Interfaces '''

os.system('ovs-docker add-port br-traffic eth2 vswitch2')
os.system('ovs-docker add-port br-sdn eth4 vswitch2')
os.system('ovs-docker add-port br-conn eth1 vswitch2')


''' Connecting Bridges with the Host Interfaces '''

os.system('ovs-vsctl add-port br-sdn ens9')   # Carries SDN Traffic out of the Host
os.system('ovs-vsctl add-port br-traffic ens10')   # Carries User Traffic out of the Host


''' Adding Default Route to Divert Traffic through the Open vSwitch br0 Bridge ''' 

os.system('ip route add 0.0.0.0/24 dev br0')


''' Setting up configuration inside Open vSwitch - vswitch1 Docker Container '''

os.system('  docker exec -it vswitch1 /bin/sh -c "ovs-vsctl add-br br-data" ')  # Created Bridge inside Open vSwitch
os.system('  docker exec -it vswitch1 /bin/sh -c "ovs-vsctl set-controller br-data tcp:192.168.80.150:6633" ')  # TCP connection with SDN Controller
os.system('  docker exec -it vswitch1 /bin/sh -c "ovs-vsctl set bridge br-data protocols=OpenFlow10,OpenFlow13" ')  # Setting up OpenFlow Protocol
# vswitch1 Docker Container Interfaces
os.system('  docker exec -it vswitch1 /bin/sh -c "ifconfig eth1 up" ')  
os.system('  docker exec -it vswitch1 /bin/sh -c "ifconfig eth2 up" ')
os.system('  docker exec -it vswitch1 /bin/sh -c "ifconfig eth3 up" ')
os.system('  docker exec -it vswitch1 /bin/sh -c "ifconfig eth4 up" ')
# Attaching vswitch1 Docker Container Interfaces to the Bridge
os.system('  docker exec -it vswitch1 /bin/sh -c "ovs-vsctl add-port br-data eth1" ')   
os.system('  docker exec -it vswitch1 /bin/sh -c "ovs-vsctl add-port br-data eth2" ')
os.system('  docker exec -it vswitch1 /bin/sh -c "ovs-vsctl add-port br-data eth3" ')
os.system('  docker exec -it vswitch1 /bin/sh -c "ovs-vsctl add-port br-data eth4" ')


''' Setting up configuration inside Open vSwitch - vswitch2 Docker Container '''

os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-vsctl add-br br-data" ')  # Created Bridge inside Open vSwitch
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-vsctl set-controller br-data tcp:192.168.80.150:6633" ')  # TCP connection with SDN Controller
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-vsctl set bridge br-data protocols=OpenFlow10,OpenFlow13" ')  # Setting up OpenFlow Protocol
# vswitch2 Docker Container Interfaces
os.system('  docker exec -it vswitch2 /bin/sh -c "ifconfig eth1 up" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ifconfig eth2 up" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ifconfig eth4 up" ')
# Attaching vswitch1 Docker Container Interfaces to the Bridge
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-vsctl add-port br-data eth1" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-vsctl add-port br-data eth2" ')
os.system('  docker exec -it vswitch2 /bin/sh -c "ovs-vsctl add-port br-data eth4" ')


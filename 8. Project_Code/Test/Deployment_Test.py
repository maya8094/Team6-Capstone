#TEAM_06:  DEPLOYMENT TESTS SCRIPTS

import os
from netmiko import ConnectHandler

SDN_controller_1 = "192.168.122.244"
SDN_controller_2 = "192.168.122.117"
Host_1 = "192.168.122.38"
Host_2 = "192.168.122.54"
test_vm = "192.168.122.62"


def ssh_dev(ip_addr):
    linux = {
        'device_type': 'linux',
        'username': 'root',
        'password': 'khir',
        'ip': ip_addr, }
    return (linux)


def opsdeploy():
    """
    Check if OpenStack is deployed successfully by SSH/VPN login into the Dell Server
    """
    cmd = 'sudo openstack --version'
    p1 = os.popen(cmd)
    output = p1.read()
    return (output)

def ops_vm_creation():
    """
    In OpenStack check if VMs are successfully created and running either using OpenStack GUI or CL
    """
    cmd = 'sudo virsh net-dhcp-leases default | grep ipv4 | wc -l'
    p1 = os.popen(cmd)
    output = p1.read()
    return (output)

def ops_vm_ip_chk():
    """
    Check if created VMs have IP address allocated on ports
    """
    cmd = 'sudo virsh net-dhcp-leases default | grep /24 | wc -l'
    p1 = os.popen(cmd)
    output = p1.read()
    return (output)

def ops_vm_vitualbri_chk():
    """
    Check creation of virtual network bridges for management and data communication
    anything above 4 to check
    """
    cmd = 'sudo virsh net-list --all | grep active | wc -l'
    p1 = os.popen(cmd)
    output = p1.read()
    return (output)

def docker_install():
    """
    Check if Docker is successfully installed on all VMs by SSH/VPN login into the VMs (for all 5 devices)
    """
    dev = ssh_dev()
    net_connect = ConnectHandler(**dev)
    cmd = 'docker --version'
    send_cmd = net_connect.send_command_timing(cmd) # disconnect session
    return(send_cmd)

def controller1_install():
    """
    Check if sdn controller_1 is installed
    """
    dev = ssh_dev(SDN_controller_1)
    net_connect = ConnectHandler(**dev)
    cmd = 'docker ps -a | grep ryu'
    send_cmd = net_connect.send_command_timing(cmd)  # disconnect session
    return (send_cmd)

def controller2_install():
    """
    Check if sdn controller_2 is installed
    """
    dev = ssh_dev(SDN_controller_2)
    net_connect = ConnectHandler(**dev)
    cmd = 'docker ps -a | grep ryu'
    send_cmd = net_connect.send_command_timing(cmd)  # disconnect session
    return (send_cmd)

def host1_ovs_install():
    """
    Check if OVS_1 is installed
    """
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd = 'docker ps -a | grep ovs'
    send_cmd = net_connect.send_command_timing(cmd)  # disconnect session
    return (send_cmd)

def host2_ovs_install():
    """
    Check if OVS_2 is installed
    """
    dev = ssh_dev(Host_2)
    net_connect = ConnectHandler(**dev)
    cmd = 'docker ps -a | grep ovs'
    send_cmd = net_connect.send_command_timing(cmd)  # disconnect session
    return (send_cmd)


def host1_ovs1_flowtable_chk():
    """
    Check if OVS_1 flows are installed
    """
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd = 'docker exec -it vswitch1 /bin/sh -c "ovs-ofctl dump-flows -O OpenFlow13 br-data | wc -l"'
    send_cmd = net_connect.send_command_timing(cmd)  # disconnect session
    return (send_cmd)

def host2_ovs2_flowtable_chk():
    """
    Check if OVS_2 flows are installed
    """
    dev = ssh_dev(Host_2)
    net_connect = ConnectHandler(**dev)
    cmd = 'docker exec -it vswitch2 /bin/sh -c "ovs-ofctl dump-flows -O OpenFlow13 br-data | wc -l"'
    send_cmd = net_connect.send_command_timing(cmd)  # disconnect session
    return (send_cmd)



#TEAM_06:  PERFORMANCE TESTS SCRIPTS

from netmiko import ConnectHandler


Host_1 = "192.168.122.38"
Host_2_intra = "192.168.122.54"
Host_2_inter = "192.168.122.176"

def ssh_dev(ip_addr):
    linux = {
        'device_type': 'linux',
        'username': 'root',
        'password': 'khir',
        'ip': ip_addr, }
    return (linux)

#L2, L3 and ARP Tests
def intra_domain_conn():
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd = 'ping ' + Host_2_intra + ' -c 4'
    send_cmd = net_connect.send_command_timing(cmd)
    return(send_cmd)

#L2, L3 and ARP Tests
def inter_domain_conn():
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd = 'ping ' + Host_2_inter + ' -c 4'
    send_cmd = net_connect.send_command_timing(cmd)
    return(send_cmd)

#Firewall perf tests:
def ssh_blocked():
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd ="ssh root@192.168.29.99" #should block i.e not successful
    send_cmd = net_connect.send_command_timing(cmd)
    return (send_cmd)

def ssh_allowed():
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd ="ssh root@192.168.122.54" #should allow i.e successful
    send_cmd = net_connect.send_command_timing(cmd)
    return (send_cmd)

def ping_block():
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd = "ping 9.9.9.9 -c 4 "  # should block i.e not successful
    send_cmd = net_connect.send_command_timing(cmd)
    return (send_cmd)


#VLAN tag test
def vlan_tag_chk():
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd = 'docker exec -it vswitch2 /bin/sh -c "ovs-ofctl dump-flows -O OpenFlow13 br-data | grep table=5 | wc -l "'
    send_cmd = net_connect.send_command_timing(cmd)
    return (send_cmd)

#QOS Config Test
def qos_perf_chk():
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd ='docker exec -it vswitch2 /bin/sh -c "ovs-ofctl dump-flows -O OpenFlow13 br-data | grep table=2 | grep priority=20, | grep :eth2 "'
    send_cmd = net_connect.send_command_timing(cmd)
    return (send_cmd)







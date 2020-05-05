#TEAM_06:  COMPATIBILITY TESTS SCRIPTS

from netmiko import ConnectHandler

Host_1 = "192.168.122.38"

def ssh_dev(ip_addr):
    linux = {
        'device_type': 'linux',
        'username': 'root',
        'password': 'khir',
        'ip': ip_addr, }
    return (linux)


def of_ovs_contrl():
    """
    Using OVS CLI, verify OpenFlow connection between OVS switches and SDN controllers
    """
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd = 'docker exec -it vswitch1 /bin/sh -c "ovs-vsctl show | grep Controller " '
    send_cmd1 = net_connect.send_command_timing(cmd)  # disconnect session
    cmd = 'docker exec -it vswitch1 /bin/sh -c "ovs-vsctl show | grep connect " '
    send_cmd2 = net_connect.send_command_timing(cmd)
    return (send_cmd1, send_cmd2)

def flow_chk():
    """
    Verify deployment of proactive flows
    between SDN controllers and application software by checking count of flow-entries
    """
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd ='docker exec -it vswitch1 /bin/sh -c "ovs-ofctl -O OpenFlow13 dump-flows br-data | wc -l " '   #cmd to verify proactive implementation
    send_cmd = net_connect.send_command_timing(cmd)
    return(send_cmd)



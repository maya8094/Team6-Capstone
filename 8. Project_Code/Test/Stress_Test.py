#TEAM_06:  STRESS TESTS SCRIPTS

from netmiko import ConnectHandler


SDN_controller_2 = "192.168.122.117"
Host_2 = "192.168.122.54"


def ssh_dev(ip_addr):
    linux = {
        'device_type': 'linux',
        'username': 'root',
        'password': 'khir',
        'ip': ip_addr, }
    return (linux)

def cntrl_redundancy():
    """
     Check if SDN CONTROLLER_2 is up and running after SDN_CONTROLLER_1 failure
    """
    dev = ssh_dev(SDN_controller_2)
    net_connect = ConnectHandler(**dev)
    cmd = 'docker service ps ryunode  | grep Running | wc -l'
    send_cmd = net_connect.send_command_timing(cmd)
    return(send_cmd)


def ovs_redundancy():
    """
    Check if OVS_2 is up and running after OVS_1 failure
    """
    dev = ssh_dev(Host_2)
    net_connect = ConnectHandler(**dev)
    cmd = 'docker service ps vswitch  | grep Running | wc -l'
    send_cmd = net_connect.send_command_timing(cmd)  # disconnect session
    return (send_cmd)

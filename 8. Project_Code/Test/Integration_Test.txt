#TEAM_06:  INTEGRATION TESTS SCRIPTS

from netmiko import ConnectHandler

SDN_controller_1 = "192.168.122.244"
SDN_controller_2 = "192.168.122.117"
Host_1 = "192.168.122.38"
Host_2 = "192.168.122.54"
test_vm = "192.168.122.62"
Dell_Server = "172.16.218.1"

def ssh_dev(ip_addr):
    linux = {
        'device_type': 'linux',
        'username': 'root',
        'password': 'khir',
        'ip': ip_addr, }
    return (linux)

def vms_conn():
    """
    Ping VMs to check successful Intra-domain connectivity
    """
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd = 'ping ' + SDN_controller_1 + ' -c 4'
    send_cmd1 = net_connect.send_command_timing(cmd)  # disconnect session
    cmd = 'ping ' + Dell_Server + ' -c 4'
    send_cmd2 = net_connect.send_command_timing(cmd)
    return (send_cmd1, send_cmd2)

def host1_ovs_bridge():
    """
    Verify successful bridging between container ports, VM interfaces and Linux bridges to support multiple service chaining
    """
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd = 'ovs-vsctl show | grep Bridge'
    send_cmd = net_connect.send_command_timing(cmd)  # disconnect session
    return (send_cmd)

def conn_ovs_sdn():
    """
    Connection between OVS and SDN_Controller_1
    """
    dev = ssh_dev(Host_1)
    net_connect = ConnectHandler(**dev)
    cmd = 'docker exec -it vswitch1 /bin/sh -c "ping 192.168.122.244 -c 4"'
    send_cmd = net_connect.send_command_timing(cmd)  # disconnect session
    return (send_cmd)




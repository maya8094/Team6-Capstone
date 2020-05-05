from Compatibility_Test import *  
from Deployment_Test import *
from Integration_Test import *
from Performance_Test import *
from Stress_Test import *


'''
Deployment Test Output
''' 
print ("\n ********** DEPLOYMENT TEST ********** \n\n")
output = Deployment_Test.opsdeploy()
print ("\n ##### Output of Deployment Test - OpenStack Deployment ##### \n")
print (output)
output = Deployment_Test.ops_vm_creation()
print ("\n ##### Output of Deployment Test - OpenStack VM Creation ##### \n")
print (output)
output = Deployment_Test.ops_vm_ip_chk()
print ("\n ##### Output of Deployment Test - OpenStack VM IP Address Allocation ##### \n")
print (output)
output = Deployment_Test.ops_vm_vitualbri_chk()
print ("\n ##### Output of Deployment Test - Creation of Virtual Network Bridges ##### \n")
print (output)
output = Deployment_Test.docker_install()
print ("\n ##### Output of Deployment Test - Docker Installation ##### \n")
print (output)
output = Deployment_Test.controller1_install()
print ("\n ##### Output of Deployment Test - SDN Controller1 Installation ##### \n")
print (output)
output = Deployment_Test.controller2_install()
print ("\n ##### Output of Deployment Test - SDN Controller2 Installation ##### \n")
print (output)
output = Deployment_Test.host1_ovs_install()
print ("\n ##### Output of Deployment Test - OVS1 Installation ##### \n")
print (output)
output = Deployment_Test.host2_ovs_install()
print ("\n ##### Output of Deployment Test - OVS2 Installation ##### \n")
print (output)
output = Deployment_Test.host1_ovs1_flowtable_chk()
print ("\n ##### Output of Deployment Test - OVS1 Flows Installation ##### \n")
print (output)
output = Deployment_Test.host2_ovs2_flowtable_chk()
print ("\n ##### Output of Deployment Test - OVS2 Flows Installation ##### \n")
print (output)


'''
Integration Test Output
'''
print ("\n ********** INTEGRATION TEST ********** \n\n")
output = Integration_Test.vms_conn()
print ("\n ##### Output of Integration Test - Intra-domain VM Connectivity ##### \n")
print (output)
output = Integration_Test.host1_ovs_bridge()
print ("\n ##### Output of Integration Test - Bridge Connectivity ##### \n")
print (output)
output = Integration_Test.conn_ovs_sdn()
print ("\n ##### Output of Integration Test - OVS-SDN Connectivity ##### \n")
print (output)


'''
Compatibility Test Output
'''
print ("\n ********** COMPATIBILITY TEST ********** \n\n")
output = Compatibility_Test.of_ovs_contrl()
print ("\n ##### Output of Compatibility Test - OVS-SDN OpenFlow Connectivity ##### \n")
print (output)
output = Compatibility_Test.flow_chk()
print ("\n ##### Output of Compatibility Test - Check Proactive Flows ##### \n")
print (output)


'''
Performance Test Output
'''
print ("\n ********** PERFORMANCE TEST ********** \n\n")
output = Performance_Test.intra_domain_conn()
print ("\n ##### Output of Performance Test - L2, L3 and ARP VNF Intra-domain Test ##### \n")
print (output)
output = Performance_Test.inter_domain_conn()
print ("\n ##### Output of Performance Test - L2, L3 and ARP VNF Inter-domain Test ##### \n")
print (output)
output = Performance_Test.ssh_blocked()
print ("\n ##### Output of Performance Test - Firewall VNF SSH Block Test ##### \n")
print (output)
output = Performance_Test.ssh_allowed()
print ("\n ##### Output of Performance Test - Firewall VNF SSH Allow Test ##### \n")
print (output)
output = Performance_Test.ping_block()
print ("\n ##### Output of Performance Test - Firewall VNF Ping Block Test ##### \n")
print (output)
output = Performance_Test.vlan_tag_chk()
print ("\n ##### Output of Performance Test - VLAN VNF Tagging Test ##### \n")
print (output)
output = Performance_Test.qos_perf_chk()
print ("\n ##### Output of Performance Test - QoS VNF Test ##### \n")
print (output)


'''
Stress Test Output
'''
print ("\n ********** STRESS TEST ********** \n\n")
output = Stress_Test.cntrl_redundancy()
print ("\n ##### Output of Stress Test - SDN Controller Redundancy Test ##### \n")
print (output)
output = Stress_Test.ovs_redundancy()
print ("\n ##### Output of Stress Test - OVS Redundancy Test ##### \n")
print (output)



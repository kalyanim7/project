import sys

print('Reading Template - /home/oracle/Oracle/Middleware/wlserver10.3/common/templates/domains/wls.jar')
readTemplate('/home/oracle/Oracle/Middleware/wlserver10.3/common/templates/domains/wls.jar')

# Admin Server SSL and Non-SSL
print('Creating Server - Admin Server')
cd('Servers/AdminServer')
set('ListenAddress','192.168.0.1')
set('ListenPort', 7001)

create('AdminServer','SSL')
cd('SSL/AdminServer')
set('Enabled', 'True')
set('ListenPort', 7002)

# Security
print('Creating Password')
cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('weblogic1')
cd('/Servers/AdminServer')
cmo.setTunnelingEnabled(true)

# Start Up
print('Setting StartUp Options')
setOption('CreateStartMenu', 'false')
setOption('ServerStartMode', 'prod')

# Setting the JDK home. 
setOption('JavaHome',sys.argv[1])
setOption('OverwriteDomain', 'true')

# Create Domain to File System
print('Writing Domain To File System')
# Change the path to your domain accordingly
writeDomain('/home/oracle/Oracle/Middleware/user_projects/domains/TPDomain')
closeTemplate()

# Read the Created Domain
print('Reading the Domain from In Offline Mode')
readDomain('/home/oracle/Oracle/Middleware/user_projects/domains/TPDomain')

# Creating Managed Servers
#Change the ports accordingly for TPMS1,TPMS2 and TPMS3
print('Creating Server - TPMS1 on Port # 12000')
cd('/')
create('TPMS1', 'Server')
cd('Server/TPMS1')
set('ListenPort', 12000)
set('ListenAddress', '192.168.0.1')

print('Creating Server - TPMS2 on Port # 11000')
cd('/')
create('TPMS2', 'Server')
cd('Server/TPMS2')
set('ListenPort', 11000)
set('ListenAddress', '192.168.0.1')

print('Creating Server - TPMS3 on Port # 10001')
cd('/')
create('TPMS3', 'Server')
cd('Server/TPMS3')
set('ListenPort', 10001)
set('ListenAddress', '192.168.0.1')

# Create and configure a cluster and assign the TPMS1 and TPMS2 Managed Servers to that cluster.
print('Creating Cluster - test_cluster and adding TPMS1, TPMS2, TPMS3')
cd('/')
create('test_cluster', 'Cluster')
assign('Server', 'TPMS1,TPMS2,TPMS3','Cluster','test_cluster')
cd('Cluster/test_cluster')
set('ClusterMessagingMode', 'unicast')
set('WeblogicPluginEnabled', 'true')

# Create and configure a machine and assign the Managed Servers to that Machine
print('Creating Machine - test_machine and adding TPMS1, TPMS2, TPMS3')
cd('/')
create('test_machine', 'Machine')
assign('Server', 'TPMS1,TPMS2,TPMS3','Machine','test_machine')
cd('Machines/' + 'test_machine/')
create('test_machine', 'NodeManager')
cd('NodeManager/' + 'test_machine')
set('NMType', 'SSL')
set('ListenAddress', '192.168.0.1')
set('DebugEnabled', 'false')

# updating the changes
print('Finalizing the changes')
updateDomain()
closeDomain()

# Exiting
print('Exiting...')
exit()

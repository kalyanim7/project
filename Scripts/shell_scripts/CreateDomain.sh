java weblogic.WLST /root/Desktop/createDomain.py /root/Desktop/jdk1.8.0_91 
mkdir -p /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/AdminServer/logs /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/AdminServer/Security
mkdir -p /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/TPMS1/logs /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/AdminServer/Security
mkdir -p /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/TPMS2/logs /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/AdminServer/Security

echo -e "username=weblogic\npassword=weblogic1" >> /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/AdminServer/Security/boot.properties
echo -e "username=weblogic\npassword=weblogic1" >> /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/TPMS1/Security/boot.properties
echo -e "username=weblogic\npassword=weblogic1" >> /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/TPMS2/Security/boot.properties

nohup ./home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/startWeblogic.sh &


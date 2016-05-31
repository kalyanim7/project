java weblogic.WLST /root/Desktop/deployApp.py /root/Desktop/EmpApp.ear

cd /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/bin

nohup ./startManagedWebLogic.sh TPMS1 &

sleep 4m

nohup ./startManagedWebLogic.sh TPMS2 &

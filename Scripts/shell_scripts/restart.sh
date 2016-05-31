java weblogic.WLST /root/Desktop/stopall.py

cd /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain

nohup ./startWebLogic.sh &

cd bin

nohup ./startManagedWebLogic.sh TPMS1 &

sleep 4m

nohup ./startManagedWebLogic.sh TPMS2 &

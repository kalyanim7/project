echo "Enter the path of deployApp.py"
read dApp
echo "Enter the path of the EmpApp.ear"
read app
java weblogic.WLST dApp app

cd /home/oracle/Oracle/Middleware/user_projects/domains/TPDomain/bin

nohup ./startManagedWebLogic.sh TPMS1 &

sleep 4m

nohup ./startManagedWebLogic.sh TPMS2 &
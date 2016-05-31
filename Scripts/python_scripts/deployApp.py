import sys
connect('weblogic','weblogic1','http://192.168.0.1:7001')
deploy('employee',sys.argv[1],targets='TPMS1,TPMS2,TPMS3',timeout=0)

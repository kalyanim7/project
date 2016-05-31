cd ~
echo "Please Enter the path of the Java JDK" 
read temp
echo -e "export JAVA_HOME=$temp\nexport PATH=$PATH:$JAVA_HOME/bin" >> .bash_profile
su -
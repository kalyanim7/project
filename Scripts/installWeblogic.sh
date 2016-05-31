echo "Enter the path for weblogic.jar"
read web
echo "Enter the path for the Silent.xml"
read sxml
echo "Enter the path to store the log file"
read log
java -jar $web -mode=silent -silent.xml=sxml -log=log
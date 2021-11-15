#Passwd file and Shadow file are located in /etc folder.
#Shadow contains password hashes, if there have been any password changes it will reflect in this files modify date.
cd /etc
modify=$(stat shadow | grep Modify)

echo $modify






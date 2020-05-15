#! /bin/bash

echo "You will be prompted for a password that will be automatically"
echo "inserted into the following files: "
echo "      docker-compose.yml"
echo "      idastatus/init.sql"
echo "      idastatus/idastatus/settings.py"

echo ""
echo -n "Enter new password: "
read NEWPASSWD

echo ""
echo "Updating docker-compose.yml"
sed -i -e "s/CHANGE_THIS_BEFORE_RUNNING/$NEWPASSWD/" docker-compose.yml
retval=$?
if [ $retval -ne 0 ];
then
    echo "FAILED! while updating docker-compose.yml"
    exit
fi

echo "Updating idastatus/init.sql"
sed -i -e "s/CHANGE_THIS_BEFORE_RUNNING/$NEWPASSWD/" idastatus/init.sql
retval=$?
if [ $retval -ne 0 ];
then
    echo "FAILED! while updating idastatus/init.sql"
    exit
fi

echo "Updating idastatus/idastatus/settings.py"
sed -i -e "s/CHANGE_THIS_BEFORE_RUNNING/$NEWPASSWD/" idastatus/idastatus/settings.py
retval=$?
if [ $retval -ne 0 ];
then
    echo "FAILED! while updating idastatus/idastatus/settings.py"
    exit
fi

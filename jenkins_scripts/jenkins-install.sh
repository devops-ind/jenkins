#!/bin/bash
#set -x

check_status(){
if [ $? == 0 ]
then
echo "Success"
else
echo "Fail"
fi
}

# install jenkins plugins using plugins list
./jenkins-plugin.sh plugins
echo "Installing Plugins..."

# install plugins (copy plugins from backup)
cp -r plugins /var/lib/jenkins/
check_status

# initialize seed jobs
cp -r jobs /var/lib/jenkins/
echo "Setting up Seed Jobs"
check_status

# change ownership of new directories
chown jenkins:jenkins /var/lib/jenkins -R

# Restart jenkins
systemctl restart jenkins
echo "Jenkins is ready!"

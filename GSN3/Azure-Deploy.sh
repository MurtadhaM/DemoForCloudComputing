# NOTE: Run in Powershell Azure Shell
#Author: Murtadha Marzouq
#Describtion: This script will automatically deploy a Virtual Machine on Azure and install GNS3 to be used as a remote lab 
#Date: 09-03-2022

#-------------------------
#Phase 1: Run on Azure CLI
#-------------------------

# The closest data center to me 
$location = 'eastus2'
# User to use to connect
$user = "snake"
# password --Change
$password = convertto-securestring 'Sn1keDev@ps!' -asplaintext -force
$credential = new-object System.Management.Automation.PSCredential ($user, $password);
$domainname = "snakedevopsgns3"

# Start creation process
new-azresourcegroup -name GNS3 -location $location
New-AzureRmNetworkSecurityGroup -Name GNS3 -ResourceGroupName GNS3 -Location $location
# create a resource group under GNS3
$nsg=Get-AzureRmNetworkSecurityGroup -Name GNS3 -ResourceGroupName GNS3
$nsg | Add-AzureRmNetworkSecurityRuleConfig -Name DMZ_Traffic -Description "DMZ" -Access Allow -Protocol * -Direction Inbound -Priority 100 -SourceAddressPrefix * -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange * | Set-AzureRmNetworkSecurityGroup
# Create the VM (THIS MAY TAKE A FEW MINUTES)
new-azvm -resourcegroup GNS3 -location $location -name 'GNS3-SERVER' -image UbuntuLTS -size 'Standard_D4s_v3' -securitygroupname GNS3 -credential $credential -DomainNameLabel $domainname
#STOP ------------------------------------------------------------------------------------------------------------------
sudo bash gns3-remote-install.sh --with-iou --with-i386-repository

#INSTALL OMZ

sudo apt update
sudo apt install zsh-syntax-highlighting zsh-dev autojump
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# add another user called Dash
useradd dash
#create home directory
sudo mkdir /home/dash
#change permission of home
sudo chown dash /home/dash
# add to sudoers group
sudo sh -c "echo 'sudo:x:27:snake,dash' >> /etc/group"
# change the theme
omz theme use obraun


#-------------------------
#Phase 3: SSH, Configure, and Connect with GNS3 local client
#-------------------------
ssh snake@publicIP





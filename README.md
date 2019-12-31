# Network Automation using Python

Python is widely used to perform network automation. With its wide set of libraries (such as Netmiko and Paramiko), there are endless possibilities for network device interactions for different vendors. Let us understand one of the most widely used libraries for network interactions. We will be using Netmiko and Paramiko to perform our network interactions.

## Programing rules of thumb

If you use a set of text more than once make it a variable, that way it’s super easy to update it when you want to make a tweak to your program.
Lots of code examples have variable names like “a”, don’t do this, it’s not bad while you’re writing the code, but in 2 months when you or someone else is reading your code you will regret not typing out a descriptive variable.
If you find yourself doing the same thing repeatedly make it a function. Not just within the same program but between programs too. One of the big reasons you are automating is to save time, not having to re-write code over and over saves a lot of time.

## Followings are Network Automation scripts list

Following scripts are help you to automate your network easily

### Script 1: multi_vendor_configuration

This script will help you to configure multiple vendor devices from multiple configuration files.

Script Supported Vendors
  1. cisco_ios
  2. cisco_xr
  3. arista_eos
  4. juniper
  5. hp_procurve

You should put the all remote hosts IP into "host_file.txt" file

Then put verious vendor configs file into "config_files" Directory

When your script will finish to configured your network after that you colud find ERROR's inside the "output_files" directory

### Script 2: 02_ReadFromExcel_and_configure

This script will help you to configure multiple vendor devices from multiple configuration files and fetching devices information from Excel.

You should put all devices details like: hostname, ip, username, password, secret, vendor details inside the "devices_details.xlsx" excel file

Then crate configs file as name of device hostname and put those file inside the  "config_files" directory

After that you could run the script








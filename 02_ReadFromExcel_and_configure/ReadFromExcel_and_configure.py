#!/bin/python3

#!interpreter [Santu Das]!
#!Date: 04/09/2019

#----------------------------------------------------------------------------!
# Read Device details from Excel and configure devices via Netmiko | Python3 !
#-------------Must Install Netmiko and XLRD before run the Script------------!
#----------XLRD lib download cmd "sudo apt-get install python3-xlrd"---------!
#----------------------------------------------------------------------------!

import xlrd
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException


workbook = xlrd.open_workbook(r"data_file/devices_details.xlsx")

sheet = workbook.sheet_by_index(0)

for index in range(1, sheet.nrows):
    hostname = sheet.row(index)[0].value
    ipaddr = sheet.row(index)[1].value
    username = sheet.row(index)[2].value
    password = sheet.row(index)[3].value
    enable_password = sheet.row(index)[4].value
    vendor = sheet.row(index)[5].value

    device = {
        'device_type': vendor,
        'ip': ipaddr,
        'username': username,
        'password': password,
        'secret': enable_password }

    print ("=====================| Connecting to Device >> {0} >> {1} |".format(device['ip'],hostname))
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()

        print ("=====================| Finding Config file for >> {0} >> {1} |".format(device['ip'],hostname))
        try:
            with open(str('config_files/') + hostname + str('.cfg')) as f:
                commands_file = f.read().splitlines()
        except:
            print ("=====================| Config file for {0} is ! Not Found ! |".format(hostname) + "\n")
            continue
        
        print ("-------------------------| Configuring  >> {0} |".format(hostname))
        output = net_connect.send_config_set(commands_file)
        print (output)
        print ("| ", hostname, "| Successfully Configured")

        net_connect.disconnect()

    except NetMikoTimeoutException:
        print ("================| Something Wrong Happen with >> {0} >> {1} |\n".format(device['ip'],hostname))
        continue

    except AuthenticationException:
        print ("================| Authentication Failed with >> {0} >> {1} |\n".format(device['ip'],hostname))
        continue

    except Exception as unknown_error:
        print ("================| Something Unknown Happen with >> {0} >> {1} |\n".format(device['ip'],hostname))
        continue

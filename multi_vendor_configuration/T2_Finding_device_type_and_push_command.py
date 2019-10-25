#!interpreter [Santu Das]

from time import time
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_autodetect import SSHDetect
from paramiko.ssh_exception import SSHException
from netmiko.ssh_dispatcher import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException

username = input('Username: ')
password = getpass("Password: ")

# Devices_file
with open('host_file.txt') as f:
    devices_list = f.read().splitlines()

# Command files    
with open('config_files/commands_file_cisco_ios') as f:
    commands_list_cisco_ios = f.read().splitlines()

with open('config_files/commands_file_cisco_xr') as f:
    commands_list_cisco_xr = f.read().splitlines()

with open('config_files/commands_file_juniper') as f:
    commands_list_juniper = f.read().splitlines()

with open('config_files/commands_file_arista_eos') as f:
    commands_arista = f.read().splitlines()

with open('config_files/commands_file_hp_procurve') as f:
    commands_list_hp_procurve = f.read().splitlines()

word_list= []

for devices in devices_list:

    starting_time = time()
    
    print ("Connecting to device: " + devices)
    ip_address_of_device = devices
    remote_device = {"device_type":"autodetect",
                     "host": devices,
                     "username": username,
                     "password": password
                     }
    try:
        guesser = SSHDetect(**remote_device)
        device_type = guesser.autodetect()
        print("Device_type:", device_type)
        net_connect = ConnectHandler(**remote_device)

    except (AuthenticationException):
        print ('Authentication failure: ' + devices)
        continue
    except (NetMikoTimeoutException):
        print ('Timeout to device: ' + devices)
        continue
    except (EOFError):
        print ('End of file while attempting device ' + devices)
        continue
    except (SSHException):
        print ('SSH Issue. Are you sure SSH is enabled? ' + devices)
        continue
    except Exception as unknown_error:
        print ('Some other error: ' + str(unknown_error))
        continue
    
    # OutputFile
    text_file = open('output_file/output_file.txt','a')

    # Logic used to connect host to configuration file
    if device_type  == 'cisco_ios':
        print("Configuring....")
        output = net_connect.send_config_set(commands_list_cisco_ios, exit_config_mode=False, delay_factor=4)
        word_list.append('===================================================\n')
        word_list.append(str("Device_type: ") + (device_type) + str(" >> IP: ") + (devices) + str(" \n")
        word_list.append('---------------------------------------------------\n')
        word_list.append((output) + str('\n'))
        word_list.append('---------------------------------------------------\n')
        text_file.writelines(word_list)
        text_file.close()
        print(output)
        
    elif device_type  == 'cisco_xr':
        print("Configuring....")
        output = net_connect.send_config_set(commands_list_cisco_xr, exit_config_mode=False, delay_factor=4)
        word_list.append('===================================================\n')
        word_list.append(str("Device_type is: ") + (device_type) + str(" >> IP: ") + (devices) + str(" \n")
        word_list.append('---------------------------------------------------\n')
        word_list.append((output) + str('\n'))
        word_list.append('---------------------------------------------------\n')
        text_file.writelines(word_list)
        text_file.close()
        print(output)
        
    elif device_type  == 'juniper':
        print("Configuring....")
        output = net_connect.send_config_set(commands_list_juniper, exit_config_mode=False, delay_factor=4)
        word_list.append('===================================================\n')
        word_list.append(str("Device_type is: ") + (device_type) + str(" >> IP: ") + (devices) + str(" \n")
        word_list.append('---------------------------------------------------\n')
        word_list.append((output) + str('\n'))
        word_list.append('---------------------------------------------------\n')
        text_file.writelines(word_list)
        text_file.close()
        print(output)
        
    elif device_type  == 'arista_eos':
        print("Configuring....")
        output = net_connect.send_config_set(commands_list_arista_eos, exit_config_mode=False, delay_factor=4)
        word_list.append('===================================================\n')
        word_list.append(str("Device_type is: ") + (device_type) + str(" >> IP: ") + (devices) + str(" \n")
        word_list.append('---------------------------------------------------\n')
        word_list.append((output) + str('\n'))
        word_list.append('---------------------------------------------------\n')
        text_file.writelines(word_list)
        text_file.close()
        print(output)
        
    elif device_type  == 'hp_procurve':
        print("Configuring....")
        output = net_connect.send_config_set(commands_list_hp_procurve, exit_config_mode=False, delay_factor=4)
        word_list.append('===================================================\n')
        word_list.append(str("Device_type is: ") + (device_type) + str(" >> IP: ") + (devices) + str(" \n")
        word_list.append('---------------------------------------------------\n')
        word_list.append((output) + str('\n'))
        word_list.append('---------------------------------------------------\n')
        text_file.writelines(word_list)
        text_file.close()
        print(output)

   # Used to determine how long it takes for the script to run/complete 
    print('\n---- Elapsed time=', time()-starting_time, '-----\n\n')


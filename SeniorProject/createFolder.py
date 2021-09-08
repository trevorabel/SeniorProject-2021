#
#
# Sources
# Custom validation loop with exception handling for python: www.stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
#

import os

def get_drive_name():
    real_drive = False
    windows_drive = "C:"
    mac_drive = "X:"
    linux_drive = ""
    drive = ""
    
    while real_drive == False:
        try:
            drive_name = int(input("Please enter the number that corresponds to you operating system: 1 for Windows, 2 for MacOS, 3 for Linux:"))
        except ValueError:
            print("Sorry, that input was not understood.")
            continue
        
        if drive_name < 0 and drive_name > 3:
            print("Sorry, please enter a valid number between 1 and 3 for your OS for encryption and decryption.")
            continue
        else:
            # in this condition the drive name is a value between 1 and 3
            if drive_name == 1:
                real_drive = True
                drive = windows_drive
            elif drive_name == 2:
                real_drive = True
                drive = mac_drive
            elif drive_name == 3:
                real_drive = True
                drive = linux_drive
                
    return drive
                
def des_Encryption_Directory():
    pathp2 = "/SPTests/DESEncryption"
    desktop = os.path.join(os.path.join(os.environ['HOME']), 'Desktop')
    drive_name = get_drive_name()
    creates_file = False
    newFolder = ""
    
    # join the drive name to the desktop path
    pathp1 = drive_name + desktop + pathp2
    while creates_file == False:
        for x in range(50):
            file_iter = x
            full_path = pathp1 + str(file_iter)
            


print(des_Encryption_Directory())
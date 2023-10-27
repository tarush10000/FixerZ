data=[['HI1','No bootable device found.','1. Switch off the system. \n2. Disconnect all power cables to the servers power supply units.\n3. Remove the system cover.\n4. Reseat all the cables of hard drive backplane at both ends.\n5. Reseat all the drives.\n6. Replace the system cover.\n7. Connect the power cables to the servers power supply units.\n8. Power on the system.\n9. To enter UEFI, Press F2.\n10. Verify that all installed drives are detected in controller BIOS, if not detected refer to the Troubleshooting Hard drive issues section.\n11. Ensure that in BIOS the RAID setting is set to RAID mode for SATA drives.\n12. Save the setting, and reboot the server.\n13. If the issue persists, contact Dell Technical Support for assistance.'],
      ['HI2','USB device not connected','1. Disconnect the device and reconnect them.\n2. If the problem persists, connect the keyboard and/or mouse to another USB port on the system.\n3. Turn off all attached USB devices, and disconnect them from the system and restart the system.\n5. Reconnect and turn on each USB device one at a time.\n6.If the problem persists, get help from the support center.'],
      ['HI3','Battery status not available','1.Check Battery Connections.\n2. Update battery drivers.\n3. Perform power reset.\n4. Check for a newer version of Windows.'],
      ['HI4','High CPU usage','1. Close unnecessary programs.\n2.Restart the PC.\n3. Update the software.\n4. Malware scan.'],
      ['HI5','High RAM usage','1. Restart your computer.\n2. Browser extensions.\n3. Adjust virtual memory.\n4. Optimize Software Settings.\n5. Add more RAM.'],
      ['HI6','High disk usage','1.Close Unnecessary Programs.\n2.Restart Your Computer.\n3.Check for Windows Updates.\n4.Clear Temporary Files.\n5.Upgrade Your Storage Drive.\n6.Check for Disk Fragmentation.\n7.Consider Using a Disk Cleanup Tool'],
      ['HI7','Camera is not working.','1. Check Camera Privacy Settings.\n2. Check camera hardware.\n3. Update camera drivers and restart your computer.\n4. Reset camera application.'],
      ['HI8','Microphone not working.','1. Check microphone privacy settings.\n2. Update mirophone drivers and restart your computer.\n3. Check recording devices.'],
      ['SI1','Network Error','1.Check Your Network Connection.\n2.Restart Your Computer or Device.\n3. Reset Network Settings. \n On Windows: Running the "ipconfig /release" and "ipconfig /renew" commands in the Command Prompt.\n On macOS: Going to "System Preferences" > "Network" > selecting your network interface > clicking "Advanced" > and choosing "Renew DHCP Lease."\n4.Disable VPN or Proxy\n5.Update Network Drivers.']
    ]

def get_sol(issue):
    for i in range(len(data)):
        if(data[i][0]==issue):
            return(data[i][1], data[i][2])
    return("No solution found")
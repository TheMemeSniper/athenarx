# AthenaRX
An exploit to bypass Reboot Restore RX, a freeware alternative to Microsoft SteadyState.

# // Disclaimer
I am not responsible for any damages caused by running this software. It is your fault if your personal computer is clogged up with a garbage 87GB .exe file.


# // About Reboot Restore RX
Reboot Restore RX is a freeware utility that restores the computer it’s installed on to a baseline image of the OS. Some schools use this to stop students from installing software such as games by restoring the entire OS to a previous state. This is similar to Microsoft’s (much more stable) SteadyState, that does the same thing.

# // About AthenaRX
AthenaRX is an exploit for bypassing Reboot Restore RX. AthenaRX is performed by filling up the drive on which Reboot Restore RX is installed on with garbage data, stopping the machine from restoring to a previous state because it doesn’t have enough space to image the OS to the baseline.

AthenaRX was discovered (comically enough) with a Python script called “THE ONE PIECE.py”, a script that would repeatedly write “THE ONE PIECE IS REAL!!!!!” to a text file until the drive was filled and the program crashed. Once the drive is filled, Reboot Restore RX attempts to defrag the system in a desperate attempt to free up space, but fails, and continues boot without imaging the baseline.

# // Using AthenaRX
To use AthenaRX, first install the programs you wish to keep across reboots. AthenaRX works by filling the C: drive to hell and back, so you'll want to install programs first. After you've installed the programs you want, download the source ZIP file from the "Code" button at the top of this repo's page, download the ZIP, extract athena.py, and run it. The exploit's completion time will depend on how much disk space is available to the computer.



AthenaRX is FOSS. This code should never be sold or forked purely to remove the author's signature.

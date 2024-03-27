
import subprocess

# AUDIO PART
global AudioPath #Stores Audio Directory Folder Path
global R_count #Store number of R_.wav files in Audio Directory
global B_count #Store number of B_.wav files in Audio Directory
global P_count #Store number of P_.wav files in Audio Directory

#Find Audio Directory
AudioPath = "/home/aperture/Documents/PortalGunProjector/Software Development/Sounds/"

#DEVELOPER note I should hardcode these values in to save on startup time.
#Now we count how many of each type of file is in this audio directory to dynamically adjust to new sound files added.
# Get the list of files in the directory that contain a letter like 'R'
result = subprocess.run(['ls', AudioPath], stdout=subprocess.PIPE, universal_newlines=True)
R_count = len([filename for filename in result.stdout.split() if 'R' in filename])
B_count = len([filename for filename in result.stdout.split() if 'B' in filename])
P_count = len([filename for filename in result.stdout.split() if 'P' in filename])
print("Number of files with 'R' in the filename: ", R_count)
print("Number of files with 'B' in the filename: ", B_count)
print("Number of files with 'P' in the filename: ", P_count)
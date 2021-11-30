import glob
import subprocess
import sys

file_path = input('Which folder do you want to process?\n').rstrip();
types = ['.mp4', '.MP4', '.mov', '.MOV', '.jpg']
files = []
program = 'ffmpeg'

for type in types:
	for file in glob.glob(f'{file_path}/**/*{type}', recursive=True):
		#print(file);
		files.append(file);

if files:
	print(f'[INFO] {len(files)} files initialized');
else: 
	print(f'\u001b[31m[ERROR] {len(files)} files were found.')
	sys.exit()
	
	
process = subprocess. run(['which', program], capture_output=True, text=True)

if process.returncode == 0: 
	print(f'[INFO] {program} initialized');
	
else:
	print(f'Please install {program} for compressing');
	print(f'Try: brew install {program}');
	sys.exit()
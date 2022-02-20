import os
import glob
import subprocess
import sys

file_path = input('Which folder do you want to process?\n').rstrip();
output_path = input('Where do you want to save the compressed files?\n').rstrip();
types = ['.mp4', '.MP4', '.mov', '.MOV', '.JPG', '.jpg']
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
	
	
process = subprocess.run(['which', program], capture_output=True, text=True)

if process.returncode == 0: 
	print(f'[INFO] {program} initialized');
	
else:
	print(f'Please install {program} for compressing');
	print(f'Try: brew install {program}');
	sys.exit();

i = 1;

for file in files:
	outputPathName = (os.path.dirname(os.path.abspath(file))).rsplit('/',1)[1];
	output = f'{output_path}/{outputPathName}';
	# output = f'{output_path}/{(os.path.dirname(os.path.abspath(file)).rsplit('/',1)[1]}';
	# print(os.path.basename(file));
	if os.path.isdir(output):
		pass
	else: 
		os.mkdir(f'{output_path}/{outputPathName}');
	
	ffmpeg = subprocess.run([program, '-i', file, '-vcodec', 'libx264', '-crf', '25', '-preset', 'veryfast', f'{output}/{os.path.basename(file)}']);
	print(f'[INFO] {i} of {len(files)} files processed\n');
	print(ffmpeg)
	print(outputPathName);
	i+= 1;

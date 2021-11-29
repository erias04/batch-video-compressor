import glob/Volumes/erias-macos/Users/eliascerne/Documents/batchVideoConverter/main.py

file_path = input('Which folder do you want to process?\n').rstrip();
types = ['.mp4', '.MP4', '.mov', '.MOV']
files = []

for type in types:
	for file in glob.glob(f'{file_path}/**/*{type}', recursive=True):
		print(file);
		files.append(file);
	

print(len(files));
print(files);
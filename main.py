import glob

file_path = input('Which folder do you want to process? \n');
files = []

for file in glob.glob(f'{file_path}/**/*.jpg', recursive=True):
	print(file);
	files.append(file);
	
print(len(files));
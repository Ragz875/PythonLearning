import os.path

TEST_DATA_DIR='C:\\Users\\raggampa\\Desktop\\testing\\data\\'
INPUT_FILE_BASE = 'input.txt'
OUTPUT_FILE_BASE = 'output.txt'
level_name='level1'
input_file_name = os.path.join(TEST_DATA_DIR, level_name, INPUT_FILE_BASE)
#output_file_name = os.path.join(TEST_DATA_DIR, level_name, OUTPUT_FILE_BASE

print('Given file:',input_file_name)
with open(input_file_name) as input_file:
    print(input_file.read())

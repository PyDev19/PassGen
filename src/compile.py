import py_compile

files = ["src/main.py", "src/backend.py", "src/gui.py"]
output_dir = "compiled_files"

for file in files:
    output_file = file.split('/')[1]
    py_compile.compile(file, cfile=f"{output_dir}/{output_file.split('.')[0]}.pyc")
    print(f"compiled {file} -> {file.split('.')[0]}.pyc")

print("compiled all files")

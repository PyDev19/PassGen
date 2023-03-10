import py_compile

files = ["src/main.py", "src/backend.py"]
output_dir = "compiled_files"

for file in files:
    py_compile.compile(file, cfile=f"{output_dir}/{file.split('.')[0]}.pyc")
    print(f"compiled {file} -> {file.split('.')[0]}.pyc")

print("compiled all files")

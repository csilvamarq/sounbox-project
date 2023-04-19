import os

# Limpiar carpeta ./spanish
os.chdir("spanish")
for file_name in os.listdir("."):
    if not file_name.startswith(".gitignore"):
        os.remove(file_name)
os.chdir("..")

# Limpiar carpeta ./japanese
os.chdir("japanese")
for file_name in os.listdir("."):
    if not file_name.startswith(".gitignore"):
        os.remove(file_name)
os.chdir("..")

# Limpiar carpeta ./output
os.chdir("output")
for file_name in os.listdir("."):
    if not file_name.startswith(".gitignore"):
        os.remove(file_name)
os.chdir("..")
# to rename many file at a time 


import os

files = os.listdir("<folder_name>")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"<folder_name>/{file}", f"<folder_name>/{i}.png")
    i = i + 1
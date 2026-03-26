import os
folder_path = r"C:\Users\prana\Downloads"
file_type_sizes = {"DOCX": 0,"PNG": 0,"PDF": 0,"Others": 0}
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        size = os.path.getsize(file_path)
        ext = os.path.splitext(file)[1].lower()
        if ext == ".docx":
            file_type_sizes["DOCX"] += size
        elif ext == ".png":
            file_type_sizes["PNG"] += size
        elif ext == ".pdf":
            file_type_sizes["PDF"] += size
        else:
            file_type_sizes["Others"] += size
print("***** Disc Health Report *****\n")
print("File Type        Size")
for key, value in file_type_sizes.items():
    print(f"{key:<15}{value}")
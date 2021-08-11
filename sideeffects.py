import os
def list_files_by_formats(formats):
    if "jpg" in formats:
        formats = formats.copy()
        formats.append("jpeg")
    files = []
""" #    for file in os.listdir(path):
        for format in formats:
            if file.endswith("." + format):
                files.append(file)
                break
    return files """

formats = ["jpg", "png"]

print(list_files_by_formats(formats))

print(formats)

# will print: ["jpg", "png", "jpeg"]


# uses' input
file_extentions = input("File name: ").rsplit(sep = ".")


# check conditionals
if file_extentions[1] == "gif":
    print("image/git")
elif file_extentions[1] == "jpg":
    print("image/jpeg")
elif file_extentions[1] == "jpeg":
    print("image/jpeg")
elif file_extentions[1] == "png":
    print("image/png")
elif file_extentions[1] == "pdf":
    print("application/pdf")
elif file_extentions[1] == "txt":
    print("txt/plain")
elif file_extentions[1] == "zip":
    print("application/zip")
else :
    print("application/octet-stream")
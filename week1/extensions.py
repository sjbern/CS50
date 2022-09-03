main = input("File Name: ").lower()
newname = main.lower()

if '.gif' in main:
    print("image/gif")

elif '.jpg' in main:
    print("image/jpeg")

elif '.jpeg' in main:
    print("image/jpeg")

elif '.png' in main:
    print("image/png")

elif '.pdf' in main:
    print("application/pdf")

elif '.txt' in main:
    print("text/plain")

elif '.zip' in main:
    print("application/zip")

else:
    print("application/octet-stream")

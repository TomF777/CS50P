"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and
then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

Common media types:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

"""

file_name = input("File name: ").lower().strip()

if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

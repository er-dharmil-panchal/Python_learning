# NOTE:
# This script requires the following helper files in the `file_io` folder:
#   - Random.png
#   - Random2.jpg
#   - Sound.mp3
# Make sure these files exist before running the program.

# ----------------------------------------
# Simplest approach (read all at once)
# ----------------------------------------
try:
    with open("file_io/Random.png", "rb") as randomIMG, open("file_io/image.jpg", "wb") as photo:
        photo.write(randomIMG.read())
    print("Image copied successfully!")
except FileNotFoundError:
    print("Error: Required file not found. Please check the file_io folder.")

# OR
photo = open("file_io/image.jpg", "wb")
randomIMG = open("file_io/Random.png", "rb")
photo.write(randomIMG.read())

# NOTE:
# - readline() is for text files, not binary images.
# - Images should be handled in binary mode with read() or chunked reads.
# - photo.write() expects bytes, not strings or lists.


# ----------------------------------------
# Chunked approach (for large files)
# ----------------------------------------
# Explanation:
# chunk := randomIMG.read(1024) assigns the 1KB of data to chunk
# while checks if chunk is not empty (truthy)
# If chunk is empty (b''), loop ends
# NOTE: '=' assignment in while gives syntax error, use ':='

try:
    with open("file_io/Random2.jpg", "rb") as randomIMG, open("file_io/image.jpg", "wb") as photo:
        while chunk := randomIMG.read(1024):  # read 1KB chunks at a time
            photo.write(chunk)
            print("Image copied successfully!")
except FileNotFoundError:
    print("Error: Required file not found. Please check the file_io folder.")

    # OR (older Python versions without ':=')
    # chunk = randomIMG.read(1024)
    # while chunk:
    #     photo.write(chunk)
    #     chunk = randomIMG.read(1024)


# ----------------------------------------
# MP3 file example
# ----------------------------------------
try:
    with open("file_io/Sound.mp3", 'rb') as sound, open("file_io/SoundOP.mp3", 'wb') as op:
        while chunk := sound.read(1024):
            op.write(chunk)
            print("Sound copied successfully!")
except FileNotFoundError:
    print("Error: Required file not found. Please check the file_io folder.")

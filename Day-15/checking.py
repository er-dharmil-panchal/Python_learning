"""
=========================================================
 File Integrity Checker (using MD5 Hash)
=========================================================
This script verifies if two files are identical by
calculating their MD5 hash — also known as a digital
fingerprint of the file.

Why MD5?
---------
- MD5 generates a unique string (hash) for any file.
- If even a single byte changes, the hash will be different.
- Commonly used for integrity checks, though not for security.
"""

# -----------------------------------------
# Import hashlib
# -----------------------------------------
# hashlib is a built-in Python library for hashing algorithms.
# We use it here to generate an MD5 hash (digital fingerprint).
import hashlib


def file_hash(path):
    """
    Generate the MD5 hash of a file (digital fingerprint).
    Returns:
        str: 32-character MD5 hash of the file.
    """
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()
# NOTE .hexdigest() -> Return the digest value as a string of hexadecimal digits.

def compare_files(file1, file2):

    hash1 = file_hash(file1)
    hash2 = file_hash(file2)

    print(f"{file1} -> {hash1}")
    print(f"{file2} -> {hash2}")

    if hash1 == hash2:
        print("✅ Files are IDENTICAL (same hash)\n")
    else:
        print("❌ Files are DIFFERENT (hash mismatch)\n")

print("=== File Integrity Checker ===")

# Change these paths to your actual files

# file1 = input("Enter path of first file: ").strip()
# file2 = input("Enter path of second file: ").strip()

file1 = "file_io/Random.png"
file2 = "file_io/image.jpg"
file3 = "file_io/Random2.jpg"

compare_files(file1, file2)
compare_files(file3, file2)

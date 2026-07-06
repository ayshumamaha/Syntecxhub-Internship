import os
import logging

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Simulated folder contents
files = [
    "report.pdf",
    "photo.jpg",
    "notes.txt",
    "song.mp3",
    "resume.pdf",
    "presentation.pptx",
    "photo.jpg",      # Duplicate
    "movie.mp4",
    "archive.zip",
    "python.py"
]

organized = {}

print("===== FILE ORGANIZER SCRIPT =====\n")

choice = input("Run in Dry Run Mode? (y/n): ").lower()

dry_run = (choice == "y")


def unique_name(folder, filename):

    if folder not in organized:
        organized[folder] = []

    if filename not in organized[folder]:
        return filename

    name, ext = os.path.splitext(filename)

    count = 1

    while True:

        new_name = f"{name}_{count}{ext}"

        if new_name not in organized[folder]:
            return new_name

        count += 1


for file in files:

    extension = os.path.splitext(file)[1]

    if extension == "":
        folder = "Others"

    else:
        folder = extension[1:].upper() + " Files"

    filename = unique_name(folder, file)

    organized.setdefault(folder, []).append(filename)

    if dry_run:

        print(f"[DRY RUN] {file}  -->  {folder}/{filename}")

    else:

        print(f"Moved: {file}  -->  {folder}/{filename}")

        logging.info("%s moved to %s/%s", file, folder, filename)

print("\n========== ORGANIZED FILES ==========\n")

for folder in organized:

    print(folder)

    for file in organized[folder]:
        print("   -", file)

    print()

print("Organization Completed Successfully.")

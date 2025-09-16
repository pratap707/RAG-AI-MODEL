import os
import subprocess
import re

# make sure output folder exists
os.makedirs("audios", exist_ok=True)

files = os.listdir("videos")
for file in files:
    # ignore non-video files
    if not file.lower().endswith((".mp4", ".mkv", ".avi", ".mov")):
        continue  

    # remove extension for processing
    base_name = os.path.splitext(file)[0]

    # extract tutorial number using regex
    match = re.search(r"Tutorial #(\d+)", base_name)
    tutorial_number = match.group(1) if match else "unknown"

    # use cleaned filename (without extension)
    file_name = base_name

    print("Converting:", file, "→", f"{tutorial_number}_{file_name}.mp3")

    subprocess.run([
        "ffmpeg", "-i", f"videos/{file}",
        f"audios/{tutorial_number}_{file_name}.mp3"
    ])

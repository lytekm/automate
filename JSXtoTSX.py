import os
import subprocess

# Define the path to the src folder
src_path = r'C:\Users\kevin\Documents\Projects\membrant2.0\membrant\membrant\front\src'


def convert_jsx_to_tsx(directory):
    # Walk through all directories and files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jsx"):
                # Construct the full path to the file
                full_file_path = os.path.join(root, file)
                # Construct the command to run
                command = f"react-js-to-ts {full_file_path}"
                print(f"Running command: {command}")
                # Execute the command
                try:
                    subprocess.run(command, check=True, shell=True)
                    print(f"Converted: {full_file_path}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to convert {full_file_path}: {str(e)}")


if __name__ == "__main__":
    convert_jsx_to_tsx(src_path)

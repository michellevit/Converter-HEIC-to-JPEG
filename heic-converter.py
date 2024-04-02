import os
from PIL import Image

def convert_and_move_heic_to_jpeg(unconverted_dir, converted_dir):
    # Ensure the converted directory exists
    os.makedirs(converted_dir, exist_ok=True)
    
    # Loop through all files in the unconverted directory
    for filename in os.listdir(unconverted_dir):
        # Skip macOS metadata files that start with ._ and only attempt to convert .heic files
        if filename.startswith("._") or not filename.lower().endswith(".heic"):
            print(f"{filename} - SKIP (Metadata file or unsupported file type)")
            continue

        # Construct the full file path
        file_path = os.path.join(unconverted_dir, filename)
        try:
            # Open the .heic file
            with Image.open(file_path) as img:
                # Define the new filename with .jpeg extension
                base_name = os.path.splitext(filename)[0] + ".jpeg"
                new_file_path = os.path.join(converted_dir, base_name)
                # Convert and save the image as .jpeg in the converted directory
                img.save(new_file_path, format="JPEG")
                print(f"{filename} - SUCCESS")
        except Exception as e:
            # If an error occurred during conversion, print FAIL
            print(f"{filename} - FAIL (Error: {e})")

# Adjust these paths as necessary
unconverted_dir = 'files-unconverted'
converted_dir = 'files-converted'
convert_and_move_heic_to_jpeg(unconverted_dir, converted_dir)

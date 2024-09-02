from PIL import Image
import os

# Define the directory containing JPEG images
directory = 'C:/Users/nickb/Desktop/projects/formRest/Images'  # Replace with your directory path

# Loop through each file in the directory
for filename in os.listdir(directory):
    # Construct full file path
    file_path = os.path.join(directory, filename)
    
    # Check if it's a file and has a .jpg or .jpeg extension
    if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.jpeg')):
        try:
            # Open the JPEG image
            with Image.open(file_path) as img:
                # Create a new file name with .png extension
                png_filename = os.path.splitext(filename)[0] + '.png'
                png_file_path = os.path.join(directory, png_filename)
                
                # Save the image in PNG format
                img.save(png_file_path, 'PNG')
                
                print(f"Converted {filename} to {png_filename}")
        
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

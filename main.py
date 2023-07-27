# Importing DoodStream Module
from doodstream import DoodStream
# Importing DoodStream API Key From config.py
from config import API_KEY
import os

# Using API Key To Access DoodStream Account
api_key = API_KEY
d = DoodStream(api_key)

#Print a message to indicate the start of the upload process
print("Uploading Please Wait...")

# Uploading File From Local Storage
# Get the current directory
current_directory = os.path.dirname(os.path.realpath(__file__))
# Define the upload directory
upload_directory = os.path.join(current_directory, 'upload')
# Get the list of files in the upload directory
files = os.listdir(upload_directory)

# Open the log file in append mode
with open('Uploaded.txt', 'a') as log_file:
    # Loop through each file in the upload directory
    for file in files:
        # Construct the full file path
        file_path = os.path.join(upload_directory, file)
        # Upload the file
        response = d.local_upload(file_path)

        # Check if the upload was successful (status code 200) before proceeding
        if response['status'] == 200:
            data = response['result']
            for item in data:
                thumb = item['splash_img']
                status = item['status']
                size = item['size']
                title = item['title']
                date = item['uploaded']
                dow_url = item['download_url']

            # Write the results to the log file
            log_file.write("====== Upload Results ======\n")
            log_file.write("Title: {}\n".format(title))
            log_file.write("Size: {} Bytes\n".format(size))
            log_file.write("Date: {} UTC\n".format(date))
            log_file.write("Thumbnail: {}\n".format(thumb))
            log_file.write("Download URL: {}\n".format(dow_url))
            log_file.write("----------------------------\n")

        # Print a message to indicate if there any errors
        else:
            log_file.write("Error: Upload request failed with status {}\n".format(response['status']))

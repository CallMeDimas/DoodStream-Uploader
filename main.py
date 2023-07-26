# Importing DoodStream Module
from doodstream import DoodStream
# Importing DoodStream API Key From config.py
from config import API_KEY
import os

# Using API Key To Access DoodStream Account
api_key = API_KEY
d = DoodStream(api_key)

# Uploading File From Local Storage
# Get the current directory
current_directory = os.path.dirname(os.path.realpath(__file__))
# Define the upload directory
upload_directory = os.path.join(current_directory, 'upload')
# Get the list of files in the upload directory
files = os.listdir(upload_directory)

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

        # Print the results
        print("====== Upload Results ======")
        print("Title:", title)
        print("Size: {} Bytes".format(size))
        print("Date: {} UTC".format(date))
        print("Thumbnail:", thumb)
        print("Download URL:", dow_url)
        print("Credit https://github.com/callmedimas/") #Please don't remove the credit :)
        print("============================")

    else:
        print("Error: Upload request failed with status", response['status'])
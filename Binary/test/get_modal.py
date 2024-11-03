import gdown

# URL of the Google Drive folder
folder_url = "https://drive.google.com/drive/folders/1-25ZOZoaFhowqi_3VpYUwmbvO7GLrnfl?usp=drive_link"

# Download the entire folder
gdown.download_folder(folder_url, output="./new modal", quiet=False)

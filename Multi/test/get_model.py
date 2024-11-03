import gdown

# URL of the Google Drive folder
folder_url = "https://drive.google.com/drive/folders/1-6HwCm8kGtVcBW-MliDQh_epWAghT8Fk?usp=sharing"

# Download the entire folder
gdown.download_folder(folder_url, output="./new modal", quiet=False)

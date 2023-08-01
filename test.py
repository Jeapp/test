import requests
import zipfile
import os
import sys
import time

def get_latest_version_from_repository():
    # Replace this URL with the URL to your repository and the file containing the latest version
    repository_url = "https://github.com/Jeapp/test/raw/main/version.txt"
    response = requests.get(repository_url)
    if response.status_code == 200:
        return response.text.strip()
    return None

def download_and_apply_update(latest_version):
    # Replace this URL with the URL to your update package
    update_url = "https://github.com/Jeapp/test/raw/main/update.zip"
    response = requests.get(update_url)

    if response.status_code == 200:
        with open("update.zip", "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile("update.zip", "r") as zip_ref:
            zip_ref.extractall(".")

 #    os.remove("update.zip")

        # Restart the updated version
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        print("Error downloading the update.")

def check_for_updates():
    current_version = "1.0.0"  # Current version of your program
    latest_version = get_latest_version_from_repository()

    if latest_version and latest_version != current_version:
        print("A new version ({}) is available!".format(latest_version))
        response = input("Would you like to download the update? (Yes/No): ")
        if response.lower() == "yes":
            download_and_apply_update(latest_version)
    else:
        print("Your program is up to date.")
        time.sleep(2)
        print("Im black")
        time.sleep(100)

        
def main():
    print("Welcome to your application!")
    check_for_updates()

if __name__ == "__main__":
    main()

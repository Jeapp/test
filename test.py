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
            print("Tool was successfully downloaded check your folder and extract the ZIP folder!")
            time.sleep(20)
            exit()

        with zipfile.ZipFile("update.zip", "r") as zip_ref:
            zip_ref.extractall(".")

        #os.remove("update.zip")

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
            time.sleep(1)
            print("Tool was successfully downloaded check your folder and extract the ZIP folder!")
            time.sleep(20)
            exit()
        if not response.lower() == "yes":
            print("BRO HOW YOU GONNA USE THE TOOL IF ITS NOT UPDATED DUMBASS?")
            time.sleep(10)
            exit()
    else:
        print("Your program is up to date.")
        time.sleep(10)

def main():
    print("Welcome to Jpxq All In One Tool")
    check_for_updates()

if __name__ == "__main__":
    main()

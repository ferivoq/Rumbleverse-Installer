import requests
import zipfile
import os
import time

def get_builds(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('versions', [])
    else:
        print("Failed to fetch builds from the API.")
        return []

def display_builds(builds):
    print("Available versions:")
    for idx, build in enumerate(builds):
        print(f" * [{idx}] {build['name']}")
    print(f"\nTotal: {len(builds)}")
    print("Please enter the number before the Build Version to select it:")

def download_build(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    downloaded_size = 0
    start_time = time.time()

    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
            downloaded_size += len(chunk)
            elapsed_time = time.time() - start_time

            if elapsed_time % 5 < 0.1:
                percent_complete = (downloaded_size / total_size) * 100
                print(f"INFO: Progress: {percent_complete:.2f}%, Running for {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}")

def unzip_file(filename, install_dir):
    if not os.path.exists(install_dir):
        os.makedirs(install_dir)

    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(install_dir)

    print(f"Build unzipped in {install_dir}")

def install_build(filename, install_dir):
    user_choice = input("Do you want to unzip it? (Y)es or (N)o: ").lower()
    if user_choice == 'y':
        unzip_file(filename, install_dir)
    else:
        print("Skipping unzip.")

def main(api_url):
    builds = get_builds(api_url)
    if not builds:
        return

    display_builds(builds)

    choice = int(input("Your choice: "))
    selected_build = builds[choice]

    install_dir = input("Please enter a game folder location: ")
    download_filename = os.path.join(install_dir, selected_build['name'] + ".zip")

    download_build(selected_build['link'], download_filename)
    install_build(download_filename, install_dir)

if __name__ == "__main__":
    API_URL = "https://rvapi.ferivoq.me/api/"
    main(API_URL)

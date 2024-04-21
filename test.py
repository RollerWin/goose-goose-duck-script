from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
import time
import os
import subprocess

def download_file(url, path):
    chrome_options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": path
    }

    chrome_options.add_experimental_option("prefs", prefs)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    time.sleep(3)
    driver.find_elements(By.ID, "uc-download-link")[0].click()
    time.sleep(3)

    for file in os.listdir(path):
        if file.endswith('.crdownload'):
            new_name = 'settings.reg'
            os.rename(os.path.join(path, file), os.path.join(path, new_name))

def import_settings_to_registry(reg_file_path):
    try:
        subprocess.call(['reg', 'import', reg_file_path])
        print("Значения из файла успешно импортированы в реестр Windows.")
    except Exception as e:
        print(f"Ошибка при импорте значений из файла в реестр Windows: {e}")

def launch_game(game_path):
    if os.path.isfile(game_path):
        subprocess.Popen([game_path])
    else:
        print("Исполняемый файл игры не найден")

if __name__ == "__main__":
    url = "https://drive.usercontent.google.com/download?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export=download&authuser=0"
    path = "D:\Mesto dlya Igor' Steam\steamapps\common\Goose Goose Duck"
    file_path = "D:\Mesto dlya Igor' Steam\steamapps\common\Goose Goose Duck\settings.reg"
    game_path = "D:\Mesto dlya Igor' Steam\steamapps\common\Goose Goose Duck\Goose Goose Duck.exe"
    
    download_file(url, path)
    import_settings_to_registry(file_path)
    launch_game(game_path)
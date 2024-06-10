import zipfile
import os


zip_path = 'static/meteo/icons.zip'
extract_path = 'static/meteo/icons/'


os.makedirs(extract_path, exist_ok=True)


with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Ícones descompactados com sucesso.")

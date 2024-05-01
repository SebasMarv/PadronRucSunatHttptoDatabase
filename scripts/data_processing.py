import os
import requests
import zipfile
import pandas as pd

class DataProcessor:
    """
    Clase para procesar datos.

    Args:
        data_folder (str): Ruta de la carpeta de datos.
        input_folder (str): Ruta de la carpeta de entrada.

    Attributes:
        data_folder (str): Ruta de la carpeta de datos.
        input_folder (str): Ruta de la carpeta de entrada.
    """

    def __init__(self, data_folder, input_folder):
        self.data_folder = data_folder
        self.input_folder = input_folder

    def remove_files(self, folder):
        """
        Elimina todos los archivos en la carpeta especificada.

        Args:
            folder (str): Ruta de la carpeta.

        Returns:
            None
        """
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            os.remove(file_path)

    def download_file(self, url, download_path):
        """
        Descarga un archivo desde la URL especificada y lo guarda en la ruta de descarga.

        Args:
            url (str): URL del archivo a descargar.
            download_path (str): Ruta donde se guardará el archivo descargado.

        Returns:
            None
        """
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(download_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

    def extract_file(self, download_path, extract_path):
        """
        Extrae un archivo comprimido en la ruta de descarga y lo guarda en la ruta de extracción.

        Args:
            download_path (str): Ruta del archivo comprimido.
            extract_path (str): Ruta donde se guardará el archivo extraído.

        Returns:
            None
        """
        with zipfile.ZipFile(download_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)

    def process_data(self, file_path):
        """
        Procesa los datos de un archivo y devuelve un DataFrame.

        Args:
            file_path (str): Ruta del archivo a procesar.

        Returns:
            pandas.DataFrame: DataFrame con los datos procesados.
        """
        df = pd.read_csv(file_path, delimiter="|", encoding='latin1', on_bad_lines='skip')
        return df

    def run(self):
        """
        Ejecuta el proceso de descarga, extracción y procesamiento de datos.

        Returns:
            None
        """
        self.remove_files(self.data_folder)

        self.remove_files(self.input_folder)

        url = "http://www2.sunat.gob.pe/padron_reducido_ruc.zip"
        download_path = os.path.join(self.input_folder, "padron_reducido_ruc.zip")
        extract_path = self.data_folder

        self.download_file(url, download_path)

        self.extract_file(download_path, extract_path)

        file_path = os.path.join(self.data_folder, "padron_reducido_ruc.txt")

        df = self.process_data(file_path)

        file_size = os.path.getsize(file_path)
        file_size_gb = file_size / 1073741824
        print(f"\nEl tamaño del archivo es {round(file_size_gb,2)} GB.")

data_folder = "../data"
input_folder = "../input"

data_processor = DataProcessor(data_folder, input_folder)
data_processor.run()

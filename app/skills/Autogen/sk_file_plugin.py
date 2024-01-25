import csv
import requests
from io import BytesIO

from app.env.connect import Connector
connector = Connector()
ocr = connector.connect_azure_ocr()

from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter
from semantic_kernel.orchestration.sk_context import SKContext


class FilePlugin:
    @sk_function(
        description="Load JPG",
        name="load_jpg",
    )

    @sk_function_context_parameter(
        name="file_path_jpg",
        description="The file path",
    )

    def load_jpg(self, context: SKContext) -> str:
        content = ""
        file_path_jpg = str(context["file_path_jpg"])

        if file_path_jpg.startswith('http://') or file_path_jpg.startswith('https://'):
            response = requests.get(file_path_jpg)
            raw_file = BytesIO(response.content)
        else:
            with open(file_path_jpg, "rb") as f:
                raw_file = f.read()
        
        ocr_reader = ocr.begin_analyze_document("prebuilt-document", raw_file)
        for idx, page in enumerate(ocr_reader.result().pages):
            for line in page.lines:
                content = content + " " + line.content
        return content
    
    @sk_function(
        description="Load PDF",
        name="load_pdf",
    )

    @sk_function_context_parameter(
        name="file_path_pdf",
        description="The file path",
    )
    
    def load_pdf(self, context: SKContext) -> str:
        content = ""
        file_path_pdf = str(context["file_path_pdf"])

        if file_path_pdf.startswith('http://') or file_path_pdf.startswith('https://'):
            response = requests.get(file_path_pdf)
            raw_file = BytesIO(response.content)
        else:
            with open(file_path_pdf, "rb") as f:
                raw_file = f.read()

        ocr_reader = ocr.begin_analyze_document("prebuilt-document", raw_file)
        for idx, page in enumerate(ocr_reader.result().pages):
            for line in page.lines:
                content = content + " " + line.content
        return content
    
    @sk_function(
        description="Load CSV",
        name="load_csv",
    )

    @sk_function_context_parameter(
        name="file_path_csv",
        description="The file path",
    )
    
    def load_csv(self, context: SKContext) -> str:
        content = ""

        file_path_csv = str(context["file_path_csv"])

        if file_path_csv.startswith('http://') or file_path_csv.startswith('https://'):
            response = requests.get(file_path_csv)
            raw_file = BytesIO(response.content)
        else:
            with open(file_path_csv, mode='r', encoding='utf-8') as f:
               for line in f:
                reader = csv.reader([line])
                for row in reader:
                    combined_line = ' '.join(row)
                    content = content + " " + combined_line

        return content
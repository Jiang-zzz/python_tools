from PyPDF2 import PdfFileMerger
from pathlib import Path
from io import FileIO
import sys


def merge_pdf(folder_path, output_name="document-output.pdf"):
    mypath = Path(folder_path)
    pdfs = [Path.joinpath(mypath, f) for f in mypath.iterdir()]
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(FileIO(pdf, "rb"))
        # use FileIO wrapping to avoid error
    merger.write(output_name)


if __name__ == "__main__":
    path_name = sys.argv[1]
    if len(sys.argv) == 2:
        merge_pdf(path_name)
    elif len(sys.argv) == 3:
        output_name = sys.argv[2]
        merge_pdf(path_name, output_name)

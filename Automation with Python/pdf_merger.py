import os
from PyPDF2 import PdfMerger

def merge_pdfs(directory, output_filename):
    merger = PdfMerger()
    
    # Get all PDF files in the directory
    pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf")]
    
    # Sort the files to ensure consistent ordering
    pdf_files.sort()
    
    # Merge the PDFs
    for filename in pdf_files:
        filepath = os.path.join(directory, filename)
        merger.append(filepath)
    
    # Write the merged PDF to a file
    with open(output_filename, "wb") as output_file:
        merger.write(output_file)
    
    print(f"Merged {len(pdf_files)} PDFs into {output_filename}")

# Example usage
merge_pdfs("/path/to/pdf/directory", "merged_output.pdf")

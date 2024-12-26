import os
from docx import Document
from docxcompose.composer import Composer

def advanced_merge_word_documents(directory, output_filename):
    # Get all .docx files in the directory
    docx_files = [f for f in os.listdir(directory) if f.endswith(".docx")]
    
    # Sort the files to ensure consistent ordering
    docx_files.sort()
    
    # Create a composer with the first document
    first_doc_path = os.path.join(directory, docx_files[0])
    composer = Composer(Document(first_doc_path))
    
    # Add the rest of the documents
    for filename in docx_files[1:]:
        filepath = os.path.join(directory, filename)
        doc = Document(filepath)
        composer.append(doc)
    
    # Save the merged document
    output_path = os.path.join(directory, output_filename)
    composer.save(output_path)
    
    print(f"Merged {len(docx_files)} Word documents into {output_filename}")

# Example usage
directory = "/path/to/word/documents"
output_filename = "advanced_merged_output.docx"

advanced_merge_word_documents(directory, output_filename)

print("Advanced Word document merging completed.")

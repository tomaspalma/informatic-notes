from pathlib import Path
import re
import subprocess

def convert_to_pdf(element):
    element_to_str = f"{element}";
    conversion_process = subprocess.Popen(['pandoc', element_to_str, "-o", f"{element_to_str[:len(element_to_str) - 3]}.pdf"])

def transform_md_into_pdf(curr_path):
    for child in curr_path.iterdir():
        if child.is_dir():
            transform_md_into_pdf(child);
        elif (child.suffix == ".md"):
                convert_to_pdf(child);
    
start_path = Path('.');

transform_md_into_pdf(start_path);


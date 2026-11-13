import zipfile
import os

manuscript_dir = r"C:\Users\alkaw\.gemini\antigravity\scratch\clei-extended-paper\manuscript"
zip_path = r"C:\Users\alkaw\Downloads\CLEI_EJ_Manuscript_Overleaf.zip"

files_to_pack = [
    "main.tex",
    "references.bib",
    "cleiej.cls",
    "cleiejbanner.jpg",
    "IEEEtran.bst",
    "IEEEabrv.bib",
    "figures/figure_interfaces_comparison.png"
]

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for rel_path in files_to_pack:
        abs_path = os.path.join(manuscript_dir, rel_path)
        if os.path.exists(abs_path):
            zipf.write(abs_path, arcname=rel_path)
            print(f"Added to zip: {rel_path} ({os.path.getsize(abs_path)} bytes)")
        else:
            print(f"WARNING: File not found: {abs_path}")

print(f"Successfully generated Overleaf package: {zip_path} ({os.path.getsize(zip_path)} bytes)")

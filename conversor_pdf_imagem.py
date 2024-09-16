from pdf2image import convert_from_path
import os

def extract_pages_as_images(pdf_path, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    pages = convert_from_path(pdf_path) # Converte todas as páginas do PDF em imagens

    # Salva cada página localmente como uma imagem, caso não precise salvar localmente pode remover essa parte do FOR
    # Pois é possível usar as imagens que estão salvas temporariamente na variavel pages.
    for i, img in enumerate(pages):
        img_path = os.path.join(destination_folder, f'pagina_{i + 1}.png')
        img.save(img_path, 'PNG')  # Salva a imagem no formato PNG
        print(f'Imagem Salva em: {img_path}')

    return pages

pdf_path = 'Documento.pdf'  # Local do arquivo PDF
destination_folder = 'imagens' # Local onde as imagens serão salvas
page_images = extract_pages_as_images(pdf_path, destination_folder)

# Mostrar as páginas extraídas
for img in page_images:
    img.show()
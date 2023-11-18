from PIL import Image
import pytesseract

def ocr_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    image_path = input("Digite o caminho da imagem: ")
    result = ocr_image(image_path)
    print("Texto extraído: \n", result)

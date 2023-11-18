import tkinter as tk
from tkinter import filedialog
from ocr_script import ocr_image


def browse_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)


def perform_ocr():
    image_path = entry_path.get()
    result = ocr_image(image_path)
    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, result)
    text_result.config(state=tk.DISABLED)


window = tk.Tk()
window.title("OCR App")

label_path = tk.Label(window, text="Caminho da Imagem:")
entry_path = tk.Entry(window, width=40)
button_browse = tk.Button(window, text="Buscar Imagem", command=browse_image)
button_ocr = tk.Button(window, text="Executar OCR", command=perform_ocr)
text_result = tk.Text(window, height=10, width=50, state=tk.DISABLED)

label_path.grid(row=0, column=0, padx=10, pady=10)
entry_path.grid(row=0, column=1, padx=10, pady=10)
button_browse.grid(row=0, column=2, padx=10, pady=10)
button_ocr.grid(row=1, column=0, columnspan=3, pady=10)
text_result.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()

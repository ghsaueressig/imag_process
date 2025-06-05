
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance
import cv2
import numpy as np

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Imagens - Grupo 1")

        self.images = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg']
        self.original_image = None
        self.modified_image = None

        self.setup_ui()

    def setup_ui(self):
        frame = tk.Frame(self.root)
        frame.pack()

        # Botões para carregar imagens predefinidas
        for idx, img in enumerate(self.images):
            btn = tk.Button(frame, text=f"Imagem {idx + 1}", command=lambda i=img: self.load_image(i))
            btn.pack(side='left')

        # Canvas para mostrar imagens
        self.original_canvas = tk.Label(self.root)
        self.original_canvas.pack(side='left')

        self.modified_canvas = tk.Label(self.root)
        self.modified_canvas.pack(side='right')

        # Filtros
        self.var_gaussian = tk.BooleanVar()
        self.var_median = tk.BooleanVar()
        self.var_laplacian = tk.BooleanVar()
        self.var_sobel = tk.BooleanVar()

        tk.Checkbutton(self.root, text="Gaussiano", variable=self.var_gaussian).pack()
        tk.Checkbutton(self.root, text="Mediana", variable=self.var_median).pack()
        tk.Checkbutton(self.root, text="Laplaciano", variable=self.var_laplacian).pack()
        tk.Checkbutton(self.root, text="Sobel", variable=self.var_sobel).pack()

        # Sliders para transformações
        self.brightness = tk.DoubleVar()
        self.contrast = tk.DoubleVar()
        self.threshold = tk.DoubleVar()

        ttk.Label(self.root, text="Brilho").pack()
        ttk.Scale(self.root, from_=0, to=2, orient='horizontal', variable=self.brightness).pack()

        ttk.Label(self.root, text="Contraste").pack()
        ttk.Scale(self.root, from_=0, to=2, orient='horizontal', variable=self.contrast).pack()

        ttk.Label(self.root, text="Binarização").pack()
        ttk.Scale(self.root, from_=0, to=255, orient='horizontal', variable=self.threshold).pack()

        # Botões de ação
        tk.Button(self.root, text="Aplicar", command=self.apply_filters).pack()
        tk.Button(self.root, text="Salvar", command=self.save_image).pack()

    def load_image(self, path):
        self.original_image = cv2.imread(path)
        self.modified_image = self.original_image.copy()
        self.display_image(self.original_image, self.original_canvas)

    def display_image(self, img, canvas):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil.resize((250, 250)))
        canvas.config(image=img_tk)
        canvas.image = img_tk

    def apply_filters(self):
        img = self.original_image.copy()

        if self.var_gaussian.get():
            img = cv2.GaussianBlur(img, (5, 5), 0)

        if self.var_median.get():
            img = cv2.medianBlur(img, 5)

        if self.var_laplacian.get():
            img = cv2.Laplacian(img, cv2.CV_64F)
            img = cv2.convertScaleAbs(img)

        if self.var_sobel.get():
            sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
            img = cv2.convertScaleAbs(cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0))

        # Ajuste de brilho e contraste
        pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        enhancer = ImageEnhance.Brightness(pil_img)
        pil_img = enhancer.enhance(self.brightness.get() or 1)

        enhancer = ImageEnhance.Contrast(pil_img)
        pil_img = enhancer.enhance(self.contrast.get() or 1)

        img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

        # Binarização
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(gray, self.threshold.get(), 255, cv2.THRESH_BINARY)

        self.modified_image = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        self.display_image(self.modified_image, self.modified_canvas)

    def save_image(self):
        if self.modified_image is not None:
            filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                                    filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("BMP files", "*.bmp")])
            if filepath:
                cv2.imwrite(filepath, self.modified_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()

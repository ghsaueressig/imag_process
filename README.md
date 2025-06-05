
# **Editor de Imagens - Grupo 1**

Este é um programa de **processamento digital de imagens** com **interface gráfica interativa**.  
Permite aplicar filtros e transformações em imagens predefinidas, ideal para aprendizado e demonstração de técnicas clássicas de processamento.

---

## ✅ **Funcionalidades**

- **Carregamento de imagens predefinidas** (4 imagens).
- **Visualização lado a lado**: imagem original e modificada.
- **Filtros**:  
  - Gaussiano  
  - Mediana  
  - Laplaciano  
  - Sobel  
- **Transformações com controle de intensidade**:  
  - Binarização (com ajuste via slider)  
  - Brilho  
  - Contraste  
  - Inverter cores  
  - Isolar cor específica  
  - Tons de cinza  
- **Salvar imagem modificada** em múltiplos formatos: `.png`, `.jpg`, `.bmp`.

---

## 🛠️ **Tecnologias utilizadas**

- Python 3.x  
- OpenCV  
- Pillow (PIL)  
- NumPy  
- Tkinter (interface gráfica)

---

## 📦 **Instalação**

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/editor-imagens-grupo1.git
cd editor-imagens-grupo1
```

2. Instale as dependências:

```bash
pip install opencv-python pillow numpy
```

3. Coloque **quatro imagens** no diretório principal com os nomes:  

- img1.jpg  
- img2.jpg  
- img3.jpg  
- img4.jpg  

*(podem ser em formatos `.png` ou `.bmp` também)*

---

## ▶️ **Como executar**

Execute o arquivo principal:  

```bash
python editor_imagens.py
```

A interface gráfica será aberta automaticamente.

---

## 🖱️ **Como usar**

1. Clique em um dos botões `Imagem 1`, `Imagem 2`, etc., para carregar a imagem.  
2. Use as **checkboxes** para ativar os filtros desejados.  
3. Ajuste as **transformações** com os sliders (binarização, brilho, contraste, etc.).  
4. Clique em `Aplicar` para ver o resultado.  
5. Clique em `Salvar` para exportar a imagem modificada.

---

## 💡 **Observações**

- O programa é focado em **didática** e **facilidade de uso**.  
- Extensível para novos filtros e transformações.  
- Compatível com Windows, Linux e macOS.

---

## 📄 **Licença**

Este projeto está sob a licença MIT — veja o arquivo **LICENSE** para detalhes.

---

## 👥 **Autores**

- [Guilherme Henke Saueressig]  

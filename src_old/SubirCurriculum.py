from pdfminer.high_level import extract_text


ruta = "C:\\Users\\agell\\Downloads\\CV_HUGO GÓMEZ VILLAREAL _SUPPLY CHAIN.pdf"



def extraerTexto(ruta):
    text = extract_text(ruta)
    print(text.upper())


extraerTexto(ruta)
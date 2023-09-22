import win32print

# Nombre de la impresora a la que deseas conectarte
printer_name = "POS"

# Texto que deseas imprimir
texto_a_imprimir = "Hola, esto es una prueba de impresión térmica."

# Intenta abrir la impresora
try:
    hprinter = win32print.OpenPrinter(printer_name)
    print(f"Conectado a la impresora '{printer_name}'")
    
    # Configura la impresora para imprimir en texto plano (RAW)
    printer_info = win32print.GetPrinter(hprinter, 2)
    printer_info['pDatatype'] = 'RAW'
    win32print.SetPrinter(hprinter, 2, printer_info, 0)
    
    # Inicia un documento de impresión
    win32print.StartDocPrinter(hprinter, 1, ("My Document", None, "RAW"))
    win32print.StartPagePrinter(hprinter)
    
    # Envía el texto a la impresora
    win32print.WritePrinter(hprinter, texto_a_imprimir.encode('utf-8'))
    
    # Finaliza el documento de impresión
    win32print.EndPagePrinter(hprinter)
    win32print.EndDocPrinter(hprinter)
    
    # Cierra la impresora
    win32print.ClosePrinter(hprinter)
    
    print("Texto impreso con éxito.")
except Exception as e:
    print(f"No se pudo imprimir en la impresora '{printer_name}': {e}")

# OCRizador de imágenes, ¡dale! 📷🔎✨
¿Tenés un montón de imágenes con texto y necesitás convertir ese quilombo a texto plano? ¡Este script de Python es tu salvación, pibe! Usamos Tesseract, una herramienta potente de OCR, para transformar todas las imágenes .png de un directorio que elijas en un archivo de texto plano.

## ¿Cómo lo uso, ché?
Es más fácil que hacer un asado. Primero necesitás tener Tesseract en tu compu. Si no lo tenés, seguí estos pasos:

- Visitá la página de lanzamientos de Tesseract en GitHub.
- Descargá el instalador para Windows.
- Ejecutá el instalador y seguí los pasos. Cuando llegues a la pantalla "Choose Components", asegurate de marcar la casilla "Tesseract development files".
- ¡Listo, ya tenés Tesseract!

- Ahora, abrí tu terminal y escribí lo siguiente:

python ocr_script.py <directorio> <archivo_salida> --lang <idioma> --rotation <rotación>
  
Solo reemplazá:

- <directorio> por el directorio donde tenés tus imágenes.
- <archivo_salida> por el nombre del archivo donde querés guardar el texto.
- <idioma> por el idioma del texto en tus imágenes (por defecto es 'spa').
- <rotación> por el ángulo de rotación de tus imágenes (por defecto es 0).

¡Y ya está, ché! 🎉 Ahora podés disfrutar de tu texto sin imágenes.

Asegurate de que el camino a tesseract.exe esté bien configurado en el script. El script y estas instrucciones suponen que estás en Windows y que Tesseract está instalado en la carpeta Program Files. Eso puede cambiar si estás usando otro sistema operativo.

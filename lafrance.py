import qrcode

# Enlace correcto al archivo HTML que redirige a tu Excel
url = "https://1drv.ms/x/c/4EFE38FC60FFCAEB/EdSNCXK-r7pCo7k0TmLkWtYBL37V32Ou3b1eR8gnb-DR0Q?e=ItbPio"

# Generar el código QR
img = qrcode.make(url)
img.save("qr_Lafrance.png")

print("✅ QR generado correctamente y apunta al archivo correcto.")

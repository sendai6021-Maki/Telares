import os
import qrcode

# Reemplaza con el enlace real de tu app cuando la subas (o la URL de tu servidor)
BASE_URL = "https://tu-app-produccion.onrender.com/registro"

os.makedirs("qrs_telares", exist_ok=True)

# Listas de telares: Fx001 a Fx030 y Rx 001 a Rx 006
telares_fx = [f"Fx{i:03d}" for i in range(1, 31)]
telares_rx = [f"Rx {i:03d}" for i in range(1, 7)]
todos = telares_fx + telares_rx

for telar in todos:
    url_destino = f"{BASE_URL}?telar={telar.replace(' ', '%20')}"
    
    qr = qrcode.QRCode(box_size=10, border=3)
    qr.add_data(url_destino)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qrs_telares/QR_{telar.replace(' ', '_')}.png")

print("Listo: 36 QRs creados en la carpeta qrs_telares")

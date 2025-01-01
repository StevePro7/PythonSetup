# 22. Automate QR Code Generation
import qrcode


def generate_qr(data, filename):
    qr = qrcode.make(data)
    qr.save(filename)

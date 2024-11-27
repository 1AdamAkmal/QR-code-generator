import qrcode
from PIL import Image

class QRCodeGenerator:
    def __init__(self):
        self.qr_image = None

    def generate(self, data):
        """
        Generate a QR code from the provided data.
        
        :param data: The text or URL to encode in the QR code.
        :return: A PIL Image object of the QR code.
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        self.qr_image = qr.make_image(fill_color="black", back_color="white")
        return self.qr_image

    def save(self, file_path):
        """
        Save the QR code image to the specified file path.
        """
        if self.qr_image:
            self.qr_image.save(file_path)
            return True
        return False
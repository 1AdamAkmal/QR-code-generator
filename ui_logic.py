from PIL import ImageTk, Image
from tkinter import filedialog
from qr_generator import QRCodeGenerator

class QRCodeAppLogic:
    def __init__(self):
        self.qr_generator = QRCodeGenerator()
        self.preview_image = None

    def preview_qr(self, data, qr_preview_label, result_label):
        """
        Generate and display the QR code preview.
        """
        if not data.strip():
            result_label.config(text="Please enter text or a URL!", bootstyle="danger")
            return

        qr_image = self.qr_generator.generate(data)

        # Resize for preview
        self.preview_image = qr_image.resize((250, 250), Image.Resampling.LANCZOS)
        qr_tk_image = ImageTk.PhotoImage(self.preview_image)

        qr_preview_label.config(image=qr_tk_image, text="")
        qr_preview_label.image = qr_tk_image
        result_label.config(text="QR Code previewed successfully!", bootstyle="success")

    def save_qr(self, result_label):
        """
        Save the generated QR code to a file.
        """
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        )
        if not file_path:
            return

        if self.qr_generator.save(file_path):
            result_label.config(text="QR Code saved successfully!", bootstyle="success")
        else:
            result_label.config(text="Generate a QR Code first!", bootstyle="danger")
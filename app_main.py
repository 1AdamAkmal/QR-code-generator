import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar
from ui_logic import QRCodeAppLogic

class QRCodeApp:
    def __init__(self):
        self.logic = QRCodeAppLogic()
        self.app = ttk.Window(themename="cosmo")
        self.app.title("QR Code Maker with Preview")
        self.app.geometry("580x600")
        self.app.resizable(False, False)
        self.data_var = StringVar()
        self._build_ui()

    def _build_ui(self):
        # Header
        header_frame = ttk.Frame(self.app)
        header_frame.pack(pady=20, fill="x")
        ttk.Label(
            header_frame, text="QR Code Generator", font=("Helvetica", 18, "bold"), bootstyle="info"
        ).pack()

        # Input Frame
        input_frame = ttk.Frame(self.app)
        input_frame.pack(pady=10)

        data_entry = ttk.Entry(
            input_frame, textvariable=self.data_var, font=("Helvetica", 12), width=25, bootstyle="cosmo"
        )
        data_entry.insert(ttk.END, "Enter Text or URL")
        data_entry.grid(row=0, column=0, padx=10, pady=8)

        preview_button = ttk.Button(
            input_frame,
            text="Preview QR Code",
            bootstyle="primary-outline",
            command=lambda: self.logic.preview_qr(
                self.data_var.get(), self.qr_preview_label, self.result_label
            ),
        )
        preview_button.grid(row=0, column=1, padx=5)

        # Preview Frame
        qr_preview_frame = ttk.Frame(self.app)
        qr_preview_frame.pack(pady=20)

        self.qr_preview_label = ttk.Label(
            qr_preview_frame, text="QR Code Preview", width=25, anchor="center", padding=10
        )
        self.qr_preview_label.pack(pady=10)

        # Save Button
        save_button = ttk.Button(
            self.app,
            text="Save QR Code",
            bootstyle="success-outline",
            command=lambda: self.logic.save_qr(self.result_label),
        )
        save_button.pack(pady=10)

        # Result Message
        self.result_label = ttk.Label(self.app, text="", font=("Helvetica", 10, "italic"))
        self.result_label.pack(pady=10)

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    app = QRCodeApp()
    app.run()
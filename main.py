"""
Ujian Tengah Semester
Kelompok 5
Anggota: Andre Alfaridzi (2408107010011)
        Muhammad Riyadh (2408107010015)
        Hani Huriyah Ahmad (2408107010020)
        Meurahmah Nushsharie (2408107010035)
        Urfan (2408107010038)
"""
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFormLayout, QLabel, 
                             QLineEdit, QPushButton, QTableWidget, 
                             QTableWidgetItem, QDesktopWidget, QMessageBox,
                             QHeaderView)
from sympy import symbols, sympify, SympifyError

class BisectionCalculator(QWidget):
    """
    Kelas utama untuk aplikasi Kalkulator Metode Biseksi.
    Mengelola semua elemen UI dan logika aplikasi.
    """
    def __init__(self):
        super().__init__()
        self._initialize_ui()

    def _initialize_ui(self):
        """Menginisialisasi seluruh antarmuka pengguna (UI)."""
        self._setup_window()
        self._create_widgets()
        self._setup_layout()
        self._apply_styles()
        self._connect_signals()
        self.center_window()

    def _setup_window(self):
        """Mengatur properti dasar jendela aplikasi."""
        self.setGeometry(0, 0, 900, 550)
        self.setWindowTitle('Kalkulator Metode Biseksi ')

    def center_window(self):
        """Memposisikan jendela aplikasi di tengah layar."""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def _create_widgets(self):

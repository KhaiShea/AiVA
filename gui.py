# gui.py

import sys
import threading
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QHBoxLayout
)
from PyQt6.QtGui import QPixmap, QIcon, QFontDatabase
from PyQt6.QtCore import Qt

from main import run_conversation_loop, stop_conversation

class AiVAWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AiVA - Gremlin Assistant")
        self.setWindowIcon(QIcon("assets/Ai.svg"))
        self.setMinimumSize(500, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2e;
                color: #f8f8f2;
                font-family: "SourGummy";
                font-size: 14px;
            }
            QPushButton {
                background-color: #ff79c6;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #ff92df;
            }
            QTextEdit {
                background-color: #282a36;
                border: 1px solid #44475a;
                border-radius: 6px;
                padding: 4px;
            }
        """)

        # Load font
        QFontDatabase.addApplicationFont("assets/fonts/SourGummy-Italic-VariableFont_wdth,wght.ttf")

        # Layouts
        layout = QVBoxLayout()
        titlebar = QHBoxLayout()

        avatar = QLabel()
        avatar.setPixmap(QPixmap("assets/Ai.svg").scaled(48, 48, Qt.AspectRatioMode.KeepAspectRatio))

        title = QLabel("Your Cute Sidekick")
        title.setStyleSheet("font-weight: bold; font-size: 16pt; margin-left: 12px;")

        titlebar.addWidget(avatar)
        titlebar.addWidget(title)
        titlebar.addStretch()

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.append("🤖 Hi! I'm AiVA! Ask me anything~")

        self.listen_button = QPushButton("🎤 Start Listening")
        self.listen_button.clicked.connect(self.start_listening)

        self.stop_button = QPushButton("🛑 End Conversation")
        self.stop_button.clicked.connect(stop_conversation)

        layout.addLayout(titlebar)
        layout.addWidget(self.log)
        layout.addWidget(self.listen_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

        self.thread = None

    def start_listening(self):
        if self.thread and self.thread.is_alive():
            self.log.append("⚠️ Already listening!")
            return

        self.thread = threading.Thread(
            target=run_conversation_loop,
            kwargs={"callback": self.append_to_log},
            daemon=True
        )
        self.thread.start()

    def append_to_log(self, user, ai):
        self.log.append(f"🧍 You: {user}")
        self.log.append(f"🤖 AiVA: {ai}")
        self.log.verticalScrollBar().setValue(self.log.verticalScrollBar().maximum())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AiVAWindow()
    window.show()
    sys.exit(app.exec())

# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
from textblob import TextBlob
import emoji

class MoodojiApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moodoji - Text to Emoji + Meaning")
        self.setGeometry(100, 100, 420, 550)   # Increased window size
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Instruction label
        self.label = QLabel("Type something to see the result:")
        self.label.setFont(QFont("Arial", 14,QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        # Text box
        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("Arial", 12))
        layout.addWidget(self.text_edit)

        # Button
        self.button = QPushButton("Show Emoji and the Meaning")
        self.button.setFont(QFont("Arial",12,QFont.Bold))
        self.button.clicked.connect(self.show_emoji)
        layout.addWidget(self.button)

        # Emoji label (output)
        self.emoji_label = QLabel("")
        self.emoji_label.setFont(QFont("Segoe UI Emoji", 150))
        self.emoji_label.setFixedHeight(300)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.emoji_label)

        # Meaning label (text below emoji)
        self.meaning_label = QLabel("")
        self.meaning_label.setFont(QFont("Arial", 16))
        self.meaning_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.meaning_label)

        self.setLayout(layout)

    def show_emoji(self):
        text = self.text_edit.toPlainText().strip()
        if not text:
            self.emoji_label.setText("❓")
            self.meaning_label.setText("Please enter some text!")
            return

        sentiment = TextBlob(text).sentiment.polarity

        # Emotion mapping
        if sentiment > 0.6:
            emotion_word = "star-struck"
            meaning = "Very Happy / Excited"
        elif sentiment > 0.2:
            emotion_word = "smile"
            meaning = "Happy / Positive"
        elif sentiment > -0.2:
            emotion_word = "neutral_face"
            meaning = "Neutral / Calm"
        elif sentiment > -0.6:
            emotion_word = "pensive"
            meaning = "Sad / Thoughtful"
        else:
            emotion_word = "loudly_crying_face"
            meaning = "Very Sad / Upset"

        # Convert to emoji
        emoji_output = emoji.emojize(f":{emotion_word}:", language="alias")

        # Display emoji + meaning
        self.emoji_label.setText(emoji_output)
        self.meaning_label.setText(f"Emotion: {meaning}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoodojiApp()
    window.show()
    sys.exit(app.exec_())
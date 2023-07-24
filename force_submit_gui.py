from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QFileDialog
from force_submit import ForceSubmitScraper

class ForceSubmitGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()

        self.webdriver_label = QLabel("Webdriver Path:")
        self.layout.addWidget(self.webdriver_label, 0, 0)

        self.webdriver_path = QLineEdit()
        self.webdriver_path.setFixedWidth(300)  # Set width
        self.layout.addWidget(self.webdriver_path, 0, 1)

        self.webdriver_browse_button = QPushButton("Browse")
        self.webdriver_browse_button.clicked.connect(self.browse_webdriver)
        self.layout.addWidget(self.webdriver_browse_button, 0, 2)

        self.csv_label = QLabel("Links CSV File Path:")
        self.layout.addWidget(self.csv_label, 1, 0)

        self.csv_path = QLineEdit()
        self.csv_path.setFixedWidth(300)  # Set width
        self.layout.addWidget(self.csv_path, 1, 1)

        self.csv_browse_button = QPushButton("Browse")
        self.csv_browse_button.clicked.connect(self.browse_csv)
        self.layout.addWidget(self.csv_browse_button, 1, 2)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_scraper)
        self.layout.addWidget(self.start_button, 2, 1)

        self.setLayout(self.layout)

    def browse_webdriver(self):
        filepath, _ = QFileDialog.getOpenFileName()
        self.webdriver_path.setText(filepath)

    def browse_csv(self):
        filepath, _ = QFileDialog.getOpenFileName()
        self.csv_path.setText(filepath)

    def start_scraper(self):
        driver_path = self.webdriver_path.text()
        postlab_links_dir = self.csv_path.text()

        scraper = ForceSubmitScraper(driver_path=driver_path, links_path=postlab_links_dir)
        scraper.force_submit()

app = QApplication([])
window = ForceSubmitGUI()
window.show()
app.exec_()

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
# from force_submit import ForceSubmitScraper

class ForceSubmitGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Force Submit Scraper")
        self.window.geometry("525x150")

        # set the background color of the window
        self.window.configure(bg="black")

        # center the window
        self.window.eval('tk::PlaceWindow %s center' % self.window.winfo_toplevel())

        # style the widgets to look more modern
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica Neue', 10), background="black", foreground="white")
        style.configure('TButton', font=('Helvetica Neue', 10), padding=1, background="black")
        style.configure('TEntry', font=('Helvetica Neue', 10), background="gray", foreground="black")
        style.configure('TCombobox', font=('Helvetica Neue', 10), padding=4, background="white", foreground="black")

        # webdriver path
        webdriver_label = ttk.Label(self.window, text="Webdriver Path:")
        webdriver_label.grid(column=0, row=0, padx=5, pady=5)

        self.webdriver_path = tk.StringVar()
        webdriver_entry = ttk.Entry(self.window, width=40, textvariable=self.webdriver_path)
        webdriver_entry.grid(column=1, row=0, padx=5, pady=5)

        webdriver_browse_button = ttk.Button(self.window, text="Browse", command=self.browse_webdriver)
        webdriver_browse_button.grid(column=2, row=0, padx=5, pady=5)

        # csv file path
        csv_label = ttk.Label(self.window, text="Links CSV File Path:")
        csv_label.grid(column=0, row=1, padx=5, pady=5)

        self.csv_path = tk.StringVar()
        csv_entry = ttk.Entry(self.window, width=40, textvariable=self.csv_path)
        csv_entry.grid(column=1, row=1, padx=5, pady=5)

        csv_browse_button = ttk.Button(self.window, text="Browse", command=self.browse_csv)
        csv_browse_button.grid(column=2, row=1, padx=5, pady=5)

        # start button
        start_button = ttk.Button(self.window, text="Start", command=self.start_scraper)
        start_button.grid(column=1, row=4, padx=5, pady=5)

        # center the widgets in the window
        for child in self.window.winfo_children():
            child.grid_configure(padx=10, pady=5)

        self.window.mainloop()

    def browse_webdriver(self):
        filepath = filedialog.askopenfilename()
        self.webdriver_path.set(filepath)

    def browse_csv(self):
        filepath = filedialog.askopenfilename()
        self.csv_path.set(filepath)

    def browse_download(self):
        filepath = filedialog.askdirectory()
        self.download_path.set(filepath)

    def start_scraper(self):
        driver_path = self.webdriver_path.get()
        download_path = self.download_path.get()
        postlab_links_dir = self.csv_path.get()
        lab_num = self.selected_lab.get()
        scraper = ForceSubmitScraper(driver_path=driver_path, links_path=postlab_links_dir)
        scraper.force_submit()
        # canvas_scraper(driver_path, download_path, postlab_links_dir, lab_num)

ForceSubmitGUI()
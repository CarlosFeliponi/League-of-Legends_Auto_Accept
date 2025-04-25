import os
import threading
import time
import tkinter as tk
from tkinter import ttk, messagebox
import cv2
import numpy as np
import pyautogui

LANGUAGES_DIR = "Languages"
OPTION_FILE = os.path.join(LANGUAGES_DIR, "Option.txt")

def get_available_languages():
    return [name for name in os.listdir(LANGUAGES_DIR)
            if os.path.isdir(os.path.join(LANGUAGES_DIR, name))]

def read_selected_language():
    if not os.path.exists(OPTION_FILE):
        return "English"
    with open(OPTION_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("Language"):
                return line.split("=")[1].strip()
    return "English"

def write_selected_language(lang):
    with open(OPTION_FILE, "w", encoding="utf-8") as f:
        f.write(f"Language = {lang}\n")

def load_images(language):
    lang_path = os.path.join(LANGUAGES_DIR, language)
    accept_img = cv2.imread(os.path.join(lang_path, "accept.png"))
    notaccept_img = cv2.imread(os.path.join(lang_path, "notaccept.png"))
    return accept_img, notaccept_img

def find_on_screen(template, threshold=0.8):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        return pt  # Return first match
    return None

class AutoAcceptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lol Auto Accept")
        self.running = False
        self.thread = None

        # Language selection
        self.languages = get_available_languages()
        self.selected_language = tk.StringVar(value=read_selected_language())
        ttk.Label(root, text="Idioma / Language:").pack(pady=5)
        self.lang_combo = ttk.Combobox(root, values=self.languages, textvariable=self.selected_language, state="readonly")
        self.lang_combo.pack(pady=5)
        self.lang_combo.bind("<<ComboboxSelected>>", self.change_language)

        # On/Off button
        self.toggle_btn = ttk.Button(root, text="ON", command=self.toggle)
        self.toggle_btn.pack(pady=10)

        self.status_label = ttk.Label(root, text="Status: OFF")
        self.status_label.pack(pady=5)

    def change_language(self, event=None):
        lang = self.selected_language.get()
        write_selected_language(lang)

    def toggle(self):
        if not self.running:
            self.running = True
            self.toggle_btn.config(text="OFF")
            self.status_label.config(text="Status: ON")
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()
        else:
            self.running = False
            self.toggle_btn.config(text="ON")
            self.status_label.config(text="Status: OFF")

    def run(self):
        lang = self.selected_language.get()
        accept_img, notaccept_img = load_images(lang)
        while self.running:
            pt = find_on_screen(accept_img)
            if pt:
                pyautogui.click(pt[0] + accept_img.shape[1]//2, pt[1] + accept_img.shape[0]//2)
                self.running = False
                self.root.after(0, lambda: self.toggle_btn.config(text="ON"))
                self.root.after(0, lambda: self.status_label.config(text="Status: OFF"))
                break
            pt_not = find_on_screen(notaccept_img)
            if pt_not:
                # Someone didn't accept, keep running
                pass
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoAcceptApp(root)
    root.mainloop()
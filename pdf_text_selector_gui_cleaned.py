import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pdfplumber
import pandas as pd
import os

class PDFTextSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Text Selector")

        self.pdf = None
        self.pdf_path = ""
        self.current_page = 0
        self.selections = []

        # Text area for PDF content with scrollbar
        text_frame = tk.Frame(root)
        text_frame.pack(pady=10)
        self.text_area = tk.Text(text_frame, wrap=tk.WORD, height=30, width=100, font=("Courier", 10))
        scrollbar = tk.Scrollbar(text_frame, command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=scrollbar.set)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Note entry
        self.note_frame = tk.Frame(root)
        self.note_frame.pack(pady=5)
        tk.Label(self.note_frame, text="Note:").pack(side=tk.LEFT)
        self.note_entry = tk.Entry(self.note_frame, width=80)
        self.note_entry.pack(side=tk.LEFT, padx=5)

        # Table for selections
        self.table_frame = tk.Frame(root)
        self.table_frame.pack(pady=10)
        self.tree = ttk.Treeview(self.table_frame, columns=("Page", "Text", "Note"), show="headings")
        self.tree.heading("Page", text="Page")
        self.tree.heading("Text", text="Selected Text")
        self.tree.heading("Note", text="Note")
        self.tree.pack()

        # Navigation and action buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)
        tk.Button(self.button_frame, text="Previous Page", command=self.prev_page).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Next Page", command=self.next_page).grid(row=0, column=1, padx=5)
        tk.Button(self.button_frame, text="Go to Page", command=self.goto_page).grid(row=0, column=2, padx=5)
        self.page_entry = tk.Entry(self.button_frame, width=5)
        self.page_entry.grid(row=0, column=3, padx=5)
        tk.Button(self.button_frame, text="Select Highlighted Text", command=self.select_text).grid(row=0, column=4, padx=5)
        tk.Button(self.button_frame, text="Open PDF", command=self.load_pdf).grid(row=0, column=5, padx=5)
        tk.Button(self.button_frame, text="Save to Excel", command=self.save_to_excel).grid(row=0, column=6, padx=5)

        # Keyboard shortcuts
        self.root.bind("<Control-o>", lambda event: self.load_pdf())
        self.root.bind("<Control-s>", lambda event: self.select_text())
        self.root.bind("<Control-e>", lambda event: self.save_to_excel())
        self.root.bind("<Control-n>", lambda event: self.next_page())
        self.root.bind("<Control-p>", lambda event: self.prev_page())
        self.root.bind("<Control-g>", lambda event: self.goto_page())

    def load_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.pdf_path = file_path
            self.pdf = pdfplumber.open(file_path)
            self.current_page = 0
            self.display_page()

    def display_page(self):
        if self.pdf:
            self.text_area.delete(1.0, tk.END)
            page = self.pdf.pages[self.current_page]
            text = page.extract_text()
            self.text_area.insert(tk.END, text if text else "[No text on this page]")

    def next_page(self):
        if self.pdf and self.current_page < len(self.pdf.pages) - 1:
            self.current_page += 1
            self.display_page()

    def prev_page(self):
        if self.pdf and self.current_page > 0:
            self.current_page -= 1
            self.display_page()

    def goto_page(self):
        try:
            page_num = int(self.page_entry.get()) - 1
            if 0 <= page_num < len(self.pdf.pages):
                self.current_page = page_num
                self.display_page()
            else:
                messagebox.showerror("Invalid Page", "Page number out of range.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid page number.")

    def select_text(self):
        try:
            selected = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
            note = self.note_entry.get().strip()
            if selected:
                self.selections.append((self.current_page + 1, selected, note))
                self.tree.insert("", tk.END, values=(self.current_page + 1, selected, note))
                self.note_entry.delete(0, tk.END)
        except tk.TclError:
            pass

    def save_to_excel(self):
        if not self.selections:
            messagebox.showinfo("No Data", "No selections to save.")
            return
        df = pd.DataFrame(self.selections, columns=["Page", "Selected Text", "Note"])
        output_path = os.path.splitext(self.pdf_path)[0] + "_selections.xlsx"
        df.to_excel(output_path, index=False, engine="openpyxl")
        messagebox.showinfo("Saved", f"Selections saved to {output_path}")
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFTextSelectorApp(root)
    root.mainloop()

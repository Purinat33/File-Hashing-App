import os
import tkinter as tk
from tkinter import filedialog
import hashlib
import zlib


# https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/
def openFile():

    file = filedialog.askopenfilename(initialdir='.',
                                      title="Select File",
                                      filetypes=(("all files",
                                                  "*.*"),
                                                 ("bin files",
                                                  "*.exe*")
                                                 ))

    # https://stackoverflow.com/questions/35483700/python-how-to-get-the-filename-in-tkinter-file-dialog
    file_name = os.path.split(file)[1]
    label_file.configure(text=f"File: {file_name}")

    # Check stuff
    if file:
        # https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only
        # MD5
        # https://stackoverflow.com/questions/16874598/how-to-calculate-the-md5-checksum-of-a-file-in-python
        md5_val = hashlib.md5(open(file, 'rb').read()).hexdigest()
        label_md5.config(state=tk.NORMAL)
        label_md5.delete('1.0', tk.END)
        # https://discuss.python.org/t/tkinter-text-insert/44527
        label_md5.insert('1.0', md5_val)
        label_md5.config(state=tk.DISABLED)
        # CRC
        crc_val = zlib.crc32(open(file, 'rb').read())
        label_crc.config(state=tk.NORMAL)
        label_crc.delete('1.0', tk.END)
        label_crc.insert('1.0', crc_val)
        label_crc.config(state=tk.DISABLED)

        # SHA256
        sha_val = hashlib.sha256(open(file, 'rb').read()).hexdigest()
        label_sha.config(state=tk.NORMAL)
        label_sha.delete('1.0', tk.END)
        label_sha.insert('1.0', sha_val)
        label_sha.config(state=tk.DISABLED)

        # TODO:
        # Add to history
        # Checking against history?


# Window
app = tk.Tk()
app.title("File Hashing Checker")
app.geometry("470x1200")


label = tk.Label(app, text='File Hash Checking', font=("Ariel", 14))
label.pack(pady=20)

author = tk.Label(app, text="By Purinat33", font=('Ariel', 10))
author.pack(pady=10)

label_file = tk.Button(app,
                       text="Open File",
                       font=("Ariel", 14),
                       command=openFile)

label_file.pack(pady=10)


label_md5_1 = tk.Label(app, text="MD5", font=("Ariel", 14))
label_md5_1.pack(pady=10)

# https://www.geeksforgeeks.org/python-tkinter-text-widget/
label_md5 = tk.Text(app, height=1, width=32, font=("Ariel", 14))
label_md5.pack()

label_crc_1 = tk.Label(app, text="CRC32", font=("Ariel", 14))
label_crc_1.pack(pady=10)

label_crc = tk.Text(app, height=1, width=10, font=("Ariel", 14))
label_crc.pack()

label_sha_1 = tk.Label(app, text="SHA256", font=("Ariel", 14))
label_sha_1.pack(pady=10)

label_sha = tk.Text(app, height=2, width=32, font=("Ariel", 14))
label_sha.pack()


def openSHA():
    file = filedialog.askopenfilename(initialdir='.',
                                      title="Select File",
                                      filetypes=(("SHA256 Files",
                                                  "*.sha256*"),
                                                 ("all files",
                                                  "*.*")
                                                 ))
    if file:
        file_name = os.path.split(file)[1]
        label_shafile.configure(text=f"File: {file_name}")
        sha_val = hashlib.sha256(open(file, 'rb').read()).hexdigest()
        label_sha_check.delete('1.0', tk.END)
        label_sha_check.insert('1.0', sha_val)


label_compare = tk.Label(
    app, text="Compare with SHA256 Hash from the original website", font=("Ariel", 14))
label_compare.pack(pady=10)


label_shafile = tk.Button(app,
                          text="Open SHA256 File",
                          font=("Ariel", 14),
                          command=openSHA)

label_shafile.pack(pady=10)

ortext = tk.Label(app, text="Or Paste it here: ", font=("Ariel", 12))
ortext.pack(pady=5)

label_sha_check = tk.Text(app, height=2, width=32, font=("Ariel", 14))
label_sha_check.pack()


def checkSHAMatch():
    if label_sha_check.get('1.0', tk.END).strip().lower() == label_sha.get('1.0', tk.END).strip().lower() and label_sha_check.get('1.0', tk.END) and label_sha.get('1.0', tk.END):
        label_status.configure(text="SHA256 Match!", fg='#006400')
    else:
        label_status.configure(text="Not MATCH", fg='#8B0000')


label_ok = tk.Button(app, text="Check Match", font=(
    'Ariel', 12), command=checkSHAMatch)
label_ok.pack(pady=10)

label_status = tk.Label(app, font=("Ariel", 16))
label_status.pack(pady=10)

##########################


def openMD5():
    file = filedialog.askopenfilename(initialdir='.',
                                      title="Select File",
                                      filetypes=(("MD5 Files",
                                                  "*.md5*"),
                                                 ("all files",
                                                  "*.*")
                                                 ))
    if file:
        file_name = os.path.split(file)[1]
        label_md5file.configure(text=f"File: {file_name}")
        md5_val = hashlib.md5(open(file, 'rb').read()).hexdigest()
        label_md5_check.delete("1.0", tk.END)
        label_md5_check.insert('1.0', md5_val)


label_compare_1 = tk.Label(
    app, text="Compare with MD5 Hash from the original website", font=("Ariel", 14))
label_compare_1.pack(pady=10)


label_md5file = tk.Button(app,
                          text="Open MD5 File",
                          font=("Ariel", 14),
                          command=openMD5)

label_md5file.pack(pady=10)

ortext1 = tk.Label(app, text="Or Paste it here: ", font=("Ariel", 12))
ortext1.pack(pady=5)

label_md5_check = tk.Text(app, height=2, width=32, font=("Ariel", 14))
label_md5_check.pack()


def checkMD5Match():
    if label_md5_check.get('1.0', tk.END).strip().lower() == label_md5.get('1.0', tk.END).strip().lower() and label_md5_check.get('1.0', tk.END) and label_md5.get('1.0', tk.END):
        label_status_md5.configure(text="MD5 Match!", fg='#006400')
    else:
        label_status_md5.configure(text="Not MATCH", fg='#8B0000')


label_ok_1 = tk.Button(app, text="Check Match", font=(
    'Ariel', 12), command=checkMD5Match)
label_ok_1.pack(pady=10)

label_status_md5 = tk.Label(app, font=("Ariel", 16))
label_status_md5.pack(pady=10)

app.mainloop()

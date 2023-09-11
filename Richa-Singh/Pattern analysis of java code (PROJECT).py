#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import csv
import os
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, scrolledtext

def extract_comments_and_blank_spaces(java_code):
    lines = java_code.split('\n')
    single_line_comments = []
    multi_line_comments = []
    blank_space_lines = []

    for i, line in enumerate(lines, start=1):
        if re.match(r'\s*\/\/', line):
            single_line_comments.append((i, line, len(line.strip())))
        elif re.match(r'\s*\/\*', line):
            multi_line = line
            for j in range(i, len(lines)):
                multi_line += '\n' + lines[j]
                if re.search(r'\*\/', lines[j]):
                    multi_comment_lines = [line.strip() for line in multi_line.split('\n')]
                    multi_line_comments.append((i, '\n'.join(multi_comment_lines), len(' '.join(multi_comment_lines))))
                    break
        elif re.match(r'^\s*$', line):
            blank_space_lines.append(i)

    # Count blank spaces
    blank_space_count = sum(len(re.findall(r'\s', line)) for line in lines)

    return single_line_comments, multi_line_comments, blank_space_lines, blank_space_count

def analyze_java_code(java_file_path, output_text, csv_writer):
    #java_file_path = input("Enter the path to the Java file: ")

    try:
        with open(java_file_path, 'r') as java_file:
            java_code = java_file.read()

            single_comments, multi_comments, blank_space_lines, blank_space_count = extract_comments_and_blank_spaces(java_code)

            total_single_length = sum(length for _, _, length in single_comments)
            total_multi_length = sum(length for _, _, length in multi_comments)
            total_single_comments = len(single_comments)
            total_multi_comments = len(multi_comments)

            print(f"\nAverage length of single-line comments: {total_single_length / total_single_comments:.2f}" if total_single_comments > 0 else "No single-line comments.")
            print(f"Average length of multi-line comments: {total_multi_length / total_multi_comments:.2f}" if total_multi_comments > 0 else "No multi-line comments.")



            print("Single-line comments:")
            for line_no, comment, length in single_comments:
                print(f"Line {line_no}: {comment} (Length: {length})")

            print("\nMulti-line comments:")
            for line_no, comment, length in multi_comments:
                print(f"Line {line_no}: {comment.strip()} (Length: {length})")

            print("\nBlank space lines:")
            for line_no in blank_space_lines:
                print(f"Line {line_no}")

            print(f"\nBlank spaces count: {blank_space_count}")

            print(f"\nAverage length of single-line comments: {total_single_length / total_single_comments:.2f}")
            print(f"Average length of multi-line comments: {total_multi_length / total_multi_comments:.2f}")

            # Plotting the bar graph
            categories = ['Single-Line Comments', 'Multi-Line Comments', 'Blank Spaces']
            counts = [total_single_comments, total_multi_comments, len(blank_space_lines)]

            plt.bar(categories, counts)
            plt.xlabel('Categories')
            plt.ylabel('Counts')
            plt.title('Java Code Analysis')
            plt.show()

            # Appending to CSV
            csv_filename = "Output (1).csv"
            with open(csv_filename, mode='a', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)

                csv_writer.writerow([])  # Empty row for separation
                csv_writer.writerow(["File: " + java_file_path])

                csv_writer.writerow(["Average length of single-line comments:", f"{total_single_length / total_single_comments:.2f}"])
                csv_writer.writerow(["Average length of multi-line comments:", f"{total_multi_length / total_multi_comments:.2f}"])

                csv_writer.writerow(["Single-line comments:"])
                for line_no, comment, length in single_comments:
                    csv_writer.writerow([f"Line {line_no}: {comment} (Length: {length})"])

                csv_writer.writerow(["Multi-line comments:"])
                for line_no, comment, length in multi_comments:
                    csv_writer.writerow([f"Line {line_no}: {comment.strip()} (Length: {length})"])

                csv_writer.writerow(["Blank space lines:"])
                for line_no in blank_space_lines:
                    csv_writer.writerow([f"Line {line_no}"])

                csv_writer.writerow([f"Blank spaces count: {blank_space_count}"])
                csv_writer.writerow([])  # Empty row for separation

            print(f"Analysis appended to {csv_filename}")



    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

def analyze_folder():
    folder_path = folder_entry.get()
    csv_filename = csv_entry.get()

    try:
        with open(csv_filename, mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)

            for filename in os.listdir(folder_path):
                if filename.endswith(".java"):
                    java_file_path = os.path.join(folder_path, filename)
                    analyze_java_code(java_file_path, output_text, csv_writer)

            output_text.insert(tk.END, "\nAnalysis completed for all files in the folder.")

    except Exception as e:
        output_text.insert(tk.END, f"An error occurred: {e}")

# Create the main GUI window
root = tk.Tk()
root.title("Java Code Analyzer - Folder")

# Create and place widgets on the GUI
folder_label = tk.Label(root, text="Java Folder:")
folder_label.pack()

folder_entry = tk.Entry(root, width=50)
folder_entry.pack()

browse_folder_button = tk.Button(root, text="Browse", command=browse_folder)
browse_folder_button.pack()

csv_label = tk.Label(root, text="CSV File:")
csv_label.pack()

csv_entry = tk.Entry(root, width=50)
csv_entry.pack()

analyze_folder_button = tk.Button(root, text="Analyze Folder", command=analyze_folder)
analyze_folder_button.pack()

output_text = scrolledtext.ScrolledText(root, width=80, height=20)
output_text.pack()

root.mainloop()


# In[ ]:





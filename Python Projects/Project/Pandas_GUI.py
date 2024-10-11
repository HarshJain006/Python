import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
from pandastable import Table

class PandasTkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pandas Data Analysis Tool")
        self.df = None

        # Load Data Button
        self.load_button = tk.Button(root, text="Load CSV/Excel", command=self.load_data)
        self.load_button.grid(row=0, column=0, padx=5, pady=5)

        # Data Exploration Buttons
        self.head_button = tk.Button(root, text="Show Head", command=self.show_head)
        self.head_button.grid(row=0, column=1, padx=5, pady=5)

        self.info_button = tk.Button(root, text="Show Info", command=self.show_info)
        self.info_button.grid(row=0, column=2, padx=5, pady=5)

        self.describe_button = tk.Button(root, text="Show Describe", command=self.show_describe)
        self.describe_button.grid(row=0, column=3, padx=5, pady=5)

        self.null_counts_button = tk.Button(root, text="Show Null Counts", command=self.show_null_counts)
        self.null_counts_button.grid(row=0, column=4, padx=5, pady=5)

        self.full_data_button = tk.Button(root, text="Show Full Data", command=self.show_full_data)
        self.full_data_button.grid(row=0, column=5, padx=5, pady=5)

        # Filtering Controls
        self.filter_column_label = tk.Label(root, text="Filter Column:")
        self.filter_column_label.grid(row=1, column=0, padx=5, pady=5)
        self.filter_column = tk.StringVar()
        self.filter_column_dropdown = ttk.Combobox(root, textvariable=self.filter_column)
        self.filter_column_dropdown.grid(row=1, column=1, padx=5, pady=5)

        self.filter_value_label = tk.Label(root, text="Filter Value:")
        self.filter_value_label.grid(row=1, column=2, padx=5, pady=5)
        self.filter_value_entry = tk.Entry(root)
        self.filter_value_entry.grid(row=1, column=3, padx=5, pady=5)

        self.apply_filter_button = tk.Button(root, text="Apply Filter", command=self.apply_filter)
        self.apply_filter_button.grid(row=1, column=4, padx=5, pady=5)

        # Data Manipulation Buttons
        self.sort_button = tk.Button(root, text="Sort Data", command=self.sort_data)
        self.sort_button.grid(row=2, column=0, padx=5, pady=5)

        self.drop_na_button = tk.Button(root, text="Drop NA", command=self.drop_na)
        self.drop_na_button.grid(row=2, column=1, padx=5, pady=5)

        self.fill_na_button = tk.Button(root, text="Fill NA", command=self.fill_na)
        self.fill_na_button.grid(row=2, column=2, padx=5, pady=5)

        self.remove_duplicates_button = tk.Button(root, text="Remove Duplicates", command=self.remove_duplicates)
        self.remove_duplicates_button.grid(row=2, column=3, padx=5, pady=5)

        # Grouping and Aggregation Controls
        self.group_column_label = tk.Label(root, text="Group By:")
        self.group_column_label.grid(row=3, column=0, padx=5, pady=5)
        self.group_column = tk.StringVar()
        self.group_column_dropdown = ttk.Combobox(root, textvariable=self.group_column)
        self.group_column_dropdown.grid(row=3, column=1, padx=5, pady=5)

        self.agg_function_label = tk.Label(root, text="Aggregate Function:")
        self.agg_function_label.grid(row=3, column=2, padx=5, pady=5)
        self.agg_function = tk.StringVar()
        self.agg_function_dropdown = ttk.Combobox(root, textvariable=self.agg_function)
        self.agg_function_dropdown['values'] = ['sum', 'mean', 'count', 'max', 'min']
        self.agg_function_dropdown.grid(row=3, column=3, padx=5, pady=5)

        self.apply_group_button = tk.Button(root, text="Apply Grouping", command=self.apply_grouping)
        self.apply_group_button.grid(row=3, column=4, padx=5, pady=5)

        # Data Visualization Buttons
        self.plot_type_label = tk.Label(root, text="Plot Type:")
        self.plot_type_label.grid(row=4, column=0, padx=5, pady=5)
        self.plot_type = tk.StringVar()
        self.plot_type_dropdown = ttk.Combobox(root, textvariable=self.plot_type)
        self.plot_type_dropdown['values'] = ['line', 'bar', 'hist', 'scatter']
        self.plot_type_dropdown.grid(row=4, column=1, padx=5, pady=5)

        self.x_column_label = tk.Label(root, text="X Column:")
        self.x_column_label.grid(row=4, column=2, padx=5, pady=5)
        self.x_column = tk.StringVar()
        self.x_column_dropdown = ttk.Combobox(root, textvariable=self.x_column)
        self.x_column_dropdown.grid(row=4, column=3, padx=5, pady=5)

        self.y_column_label = tk.Label(root, text="Y Column:")
        self.y_column_label.grid(row=4, column=4, padx=5, pady=5)
        self.y_column = tk.StringVar()
        self.y_column_dropdown = ttk.Combobox(root, textvariable=self.y_column)
        self.y_column_dropdown.grid(row=4, column=5, padx=5, pady=5)

        self.plot_button = tk.Button(root, text="Plot Data", command=self.plot_data)
        self.plot_button.grid(row=4, column=6, padx=5, pady=5)

        # Export Button
        self.export_button = tk.Button(root, text="Export Data", command=self.export_data)
        self.export_button.grid(row=5, column=0, padx=5, pady=5)

        # Data Display Frame
        self.frame = tk.Frame(root)
        self.frame.grid(row=6, column=0, columnspan=7, sticky="nsew")
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_columnconfigure(tuple(range(7)), weight=1)

    def load_data(self):
        file_path = filedialog.askopenfilename(title="Open CSV or Excel File", filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if file_path:
            try:
                if file_path.endswith('.csv'):
                    self.df = pd.read_csv(file_path)
                elif file_path.endswith('.xlsx'):
                    self.df = pd.read_excel(file_path)
                messagebox.showinfo("Success", "Data loaded successfully!")
                self.display_data(self.df)
                self.populate_columns()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load data: {e}")

    def populate_columns(self):
        if self.df is not None:
            columns = ['None'] + list(self.df.columns)
            self.filter_column_dropdown['values'] = columns
            self.group_column_dropdown['values'] = columns
            self.x_column_dropdown['values'] = self.df.columns
            self.y_column_dropdown['values'] = self.df.columns

    def show_head(self):
        self.display_data(self.df.head(10))

    def show_info(self):
        messagebox.showinfo("Data Info", str(self.df.info()))

    def show_describe(self):
        describe_df = self.df.describe(include='all')
        describe_text = "Data Description:\n\n" + str(describe_df) + "\n"
        describe_text += "\nStatistical Summary:\n"
        for col in describe_df.columns:
            describe_text += f"{col}:\n"
            describe_text += f"Count: {describe_df[col]['count']}\n"
            describe_text += f"Mean: {describe_df[col]['mean'] if 'mean' in describe_df[col] else 'N/A'}\n"
            describe_text += f"Std: {describe_df[col]['std'] if 'std' in describe_df[col] else 'N/A'}\n"
            describe_text += f"Min: {describe_df[col]['min'] if 'min' in describe_df[col] else 'N/A'}\n"
            describe_text += f"25%: {describe_df[col]['25%'] if '25%' in describe_df[col] else 'N/A'}\n"
            describe_text += f"50%: {describe_df[col]['50%'] if '50%' in describe_df[col] else 'N/A'}\n"
            describe_text += f"75%: {describe_df[col]['75%'] if '75%' in describe_df[col] else 'N/A'}\n"
            describe_text += f"Max: {describe_df[col]['max'] if 'max' in describe_df[col] else 'N/A'}\n\n"
        messagebox.showinfo("Data Description", describe_text.strip())

    def show_null_counts(self):
        if self.df is not None:
            null_counts = self.df.isnull().sum()
            null_counts_text = "Null Value Counts:\n\n" + str(null_counts)
            messagebox.showinfo("Null Value Counts", null_counts_text)

    def show_full_data(self):
        self.display_data(self.df)

    def apply_filter(self):
        column = self.filter_column.get()
        value = self.filter_value_entry.get()
        if column and value:
            filtered_df = self.df[self.df[column] == value]
            self.display_data(filtered_df)

    def sort_data(self):
        if self.df is not None:
            sorted_df = self.df.sort_values(by=self.df.columns[0])  # Default sort by the first column
            self.display_data(sorted_df)

    def drop_na(self):
        if self.df is not None:
            cleaned_df = self.df.dropna()
            self.display_data(cleaned_df)

    def fill_na(self):
        if self.df is not None:
            filled_df = self.df.fillna(0)  # Filling NA with 0, can be modified
            self.display_data(filled_df)

    def remove_duplicates(self):
        if self.df is not None:
            deduplicated_df = self.df.drop_duplicates()
            self.display_data(deduplicated_df)

    def apply_grouping(self):
        column = self.group_column.get()
        agg_func = self.agg_function.get()
        if column:
            grouped_df = self.df.groupby(column).agg(agg_func).reset_index()
            self.display_data(grouped_df)

    def plot_data(self):
        plot_type = self.plot_type.get()
        x_column = self.x_column.get()
        y_column = self.y_column.get()
        if plot_type and x_column and y_column:
            if plot_type == 'line':
                self.df.plot(x=x_column, y=y_column, kind='line')
            elif plot_type == 'bar':
                self.df.plot(x=x_column, y=y_column, kind='bar')
            elif plot_type == 'hist':
                self.df[y_column].plot(kind='hist')
            elif plot_type == 'scatter':
                self.df.plot(x=x_column, y=y_column, kind='scatter')
            plt.show()

    def export_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if file_path:
            try:
                if file_path.endswith('.csv'):
                    self.df.to_csv(file_path, index=False)
                elif file_path.endswith('.xlsx'):
                    self.df.to_excel(file_path, index=False)
                messagebox.showinfo("Success", "Data exported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export data: {e}")

    def display_data(self, data):
        if data is not None:
            self.clear_frame()
            table = Table(self.frame, dataframe=data, showtoolbar=True, showstatusbar=True)
            table.show()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PandasTkApp(root)
    root.mainloop()

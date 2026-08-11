import pandas as pd
from pathlib import Path
class DataExplorer:

    def __init__(self):
        self.df = None
        self.file_name = None

    def load_csv(self, file_path):
        try:
            self.df = pd.read_csv(file_path)
            self.file_name = Path(file_path).name

        except FileNotFoundError:
            print("File not Found")

        except Exception as ex:
            print(f"""Could not load CSV
                  Reason: {ex}""")

        else:
            print("===================================")
            print("CSV loaded successfully\n")

            print(f"Dataset: {self.file_name} \n")

            rows, columns = self.df.shape
            print("Rows : ", rows)
            print("Columns : ", columns)
            print("===================================/n/n")

    def is_loaded(self):
        if self.df is None:
            print("Please load a CSV file first.")
            return False

        return True

    def dataset_info(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        rows, columns = self.df.shape
        print(f"Dataset Dimensions: {rows} rows x {columns} columns\n")

        print("Detailed Information: ")
        self.df.info()

    def show_shape(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        rows, columns = self.df.shape
        print(f"The dataset has {rows} rows and {columns} columns./n")

    def show_columns(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        print("\n")
        for index, column_name in enumerate(self.df.columns, start=1):
            print(f"{index}. {column_name}")

    def show_dtypes(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        print("Column Datatypes: ")
        print(self.df.dtypes,"\n")

    def head(self, rows=5):
        if not self.is_loaded():
            return
        assert self.df is not None

        print(self.df.head(rows),"\n")

    def tail(self, rows=5):
        if not self.is_loaded():
            return
        assert self.df is not None

        print(self.df.tail(rows),"\n")

    def missing_values(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        print("\n Number of Missing Values:")
        print(self.df.isnull().sum(),"\n")

    def statistics(self):
        """
        Display statistical summary of the dataset.
        """

        if not self.is_loaded():
            return
        assert self.df is not None

        # Count the columns having number and object
        numeric_count = len(self.df.select_dtypes(include='number').columns)
        object_count = len(self.df.select_dtypes(include='object').columns)

        # Print the number of columns calculated above
        print(f"\n Total Numeric Columns: {numeric_count}")
        print(f"Total Object Columns: {object_count} \n ")

        print("Statistical summary:")
        print(self.df.describe(include='all'),"\n")

    def correlation_matrix(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        print("\n Correlation matrix: ")
        numeric_df = self.df.select_dtypes(include=['number'])
        print(numeric_df.corr(),"\n")

    def remove_missing_values(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        rows, columns = self.df.shape
        print("\n Original Rows: ", rows)

        self.df = self.df.dropna()

        new_rows, columns = self.df.shape
        print("After Removal Rows: ", new_rows)
        print(f"{rows-new_rows} rows removed \n")

    def export_csv(self,name):
        if not self.is_loaded():
            return
        assert self.df is not None

        export_dir = Path("exports")
        export_dir.mkdir(parents=True, exist_ok=True)

        path = "exports/" + name
        self.df.to_csv(path,index= False)
        print(f"""CSV exported successfully!
Location: {path} \n """)


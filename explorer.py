import pandas as pd


class DataExplorer:

    def __init__(self):
        self.df = None

    def load_csv(self, file_path):
        try:
            self.df = pd.read_csv(file_path)
        except FileNotFoundError:
            print("File not Found")

        except Exception as ex:
            print(ex)

        else:
            print("CSV loaded successfully")
            rows, columns = self.df.shape
            print("Rows : ", rows)
            print("Columns : ", columns)

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
        print("Rows: ", rows)
        print("Columns: ", columns)
        print("Datatype: ", self.df.dtypes)
        self.df.info()

    def show_shape(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        rows, columns = self.df.shape
        print(f"The dataset has {rows} rows and {columns} columns.")
        pass

    def show_columns(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        print(self.df.columns.to_list())

    def show_dtypes(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        print("Column Datatypes: ")
        print(self.df.dtypes)
        pass

    def head(self, rows=5):
        if not self.is_loaded():
            return
        assert self.df is not None

        print(self.df.head(rows))

    def tail(self, rows=5):
        if not self.is_loaded():
            return
        assert self.df is not None

        print(self.df.tail(rows))

    def missing_values(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        print("Number of Missing Values:")
        print(self.df.isnull().sum())
        pass

    def statistics(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        print("Statistical summary:")
        print(self.df.describe(include='all'))

    def correlation_matrix(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        print("Correlation matrix: ")
        numeric_df = self.df.select_dtypes(include=['number'])
        print(numeric_df.corr())

    def remove_missing_values(self):
        if not self.is_loaded():
            return
        assert self.df is not None

        rows, columns = self.df.shape
        print("Original Rows: ", rows)

        cleaned = self.df.dropna()

        new_rows, columns = cleaned.shape
        print("After Removal Rows: ", new_rows)
        print(f"{rows-new_rows} rows removed")

    def export_csv(self,name):
        if not self.is_loaded():
            return
        assert self.df is not None

        path = "exports/" + name
        self.df.to_csv(path,index= False)
        print(f"""CSV exported successfully!
                Location: {path}""")

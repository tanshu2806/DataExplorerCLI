from numpy import dtype
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
            print("Rows : ",rows)
            print("Columns : ",columns)   

    def dataset_info(self):
        if self.df.empty:
            print("Please upload the CSV first.")
        else:
            rows, column = self.df.shape
            print("Rows: ", rows)     
            print("Columns: ", column)
            print("Datatype: ",dtype)
            print("Memory Usage: ", self.df.info())

    def head(self):
        print(self.df.head())

    def tail(self):
        print(self.df.tail())     
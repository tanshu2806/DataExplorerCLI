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
            print("Clomns : ",columns)        
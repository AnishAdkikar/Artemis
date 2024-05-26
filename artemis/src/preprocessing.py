from abc import ABC, abstractmethod
import pandas as pd
from PyPDF2 import PdfReader 

class Preprocessing(ABC):
    @abstractmethod
    def load_data(self, source):
        pass

    @abstractmethod
    def preprocess(self):
        pass

class DatasetPreprocessing(Preprocessing):
    def __init__(self):
        self.df = None

    def load_data(self, source):
        self.df =  pd.read_csv(source)
    
    def preprocess(self,func):
        self.df = func(self.df)
        return [" ".join(str(x) for x in row) for row in self.df.values]
    
class PdfPreprocessing(Preprocessing):
    def __init__(self):
        self.reader = None
        self.pages = None

    def load_data(self, source):
        self.reader = PdfReader(source)
        self.pages = len(self.reader.pages)
    
    def preprocess(self):
        texts = []
        for i in range(self.pages):
            data = self.reader.pages[i].extract_text().strip().split('\n')
            data = [x.strip().replace('\n','') for x in data if x not in (' ','',""," ") ]
            texts.extend(data)
        return texts

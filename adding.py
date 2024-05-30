import artemis
import pandas as pd

def custom_processing(df):
    df = pd.DataFrame(df, columns=['condition_label', 'medical_abstract'])
    df.replace(to_replace =1,  
                    value = "Neoplasms ||||",  
                    inplace = True) 
    df.replace(to_replace =2,  
                    value = "Digestive system diseases ||||",  
                    inplace = True) 
    df.replace(to_replace =3,  
                    value = "Nervous system diseases ||||",  
                    inplace = True) 
    df.replace(to_replace =4,  
                    value = "Cardiovascular diseases ||||",  
                    inplace = True) 
    df.replace(to_replace =5,  
                    value = "General pathological conditions ||||",  
                    inplace = True) 
    return df

vectordb = artemis.VectorDb(user="testing_train2")
print("Conection Sucessful")
api = artemis.OpenAITopping()
processing = artemis.DatasetPreprocessing()
processing.load_data("/home/deathv/Desktop/code/FYP/resources/medical_tc_train.csv")
texts = processing.preprocess(custom_processing)
print(len(texts))
vectors = vectordb.convert_to_vectors(api.request,texts)
vectordb.add_vector(vectors)
print("Addition Sucessful")
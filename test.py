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

vectordb = artemis.VectorDb(user="testing", password="testig")
print("Conection Sucessful")
api = artemis.OpenAITopping()
processing = artemis.DatasetPreprocessing()
# processing.load_data("/home/deathv/Desktop/code/FYP/resources/medical_tc_test.csv")
# texts = processing.preprocess(custom_processing)
# print(len(texts))
# vectors = vectordb.convert_to_vectors(api.request,texts)
# print(len(vectors))
# vectordb.add_vector(vectors)
# print("Addition Sucessful")
query = '''Human papillomavirus in women with vulvar intraepithelial neoplasia III. Untreated cases of vulvar intraepithelial neoplasia (VIN) III may progress to invasive vulvar carcinoma. Tissues from 29 New Zealand women with VIN III were examined for the presence of human papillomavirus (HPV) types 6, 11, 16 and 18 by in situ hybridization and polymerase chain reaction. HPV 16, the only HPV type detected in the lesions, was identified in about half the cases. HPV-positive women were younger than HPV-negative women, and their lesions displayed koilocytosis more often. In four of five cases in which there was a progression to invasive cancer, HPV 16 was detected in both the VIN III and invasive cancer tissue.'''
query_vector = vectordb.convert_to_vectors(api.request,[query])
res = vectordb.query(query_vector[query])
print([x.split("||||")[0].strip() for x in res])
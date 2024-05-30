import artemis

vectordb = artemis.VectorDb(user="testing")
print("Conection Sucessful")
api = artemis.OpenAITopping()
query = '''Human papillomavirus in women with vulvar intraepithelial neoplasia III. Untreated cases of vulvar intraepithelial neoplasia (VIN) III may progress to invasive vulvar carcinoma. Tissues from 29 New Zealand women with VIN III were examined for the presence of human papillomavirus (HPV) types 6, 11, 16 and 18 by in situ hybridization and polymerase chain reaction. HPV 16, the only HPV type detected in the lesions, was identified in about half the cases. HPV-positive women were younger than HPV-negative women, and their lesions displayed koilocytosis more often. In four of five cases in which there was a progression to invasive cancer, HPV 16 was detected in both the VIN III and invasive cancer tissue.'''
query_vector = vectordb.convert_to_vectors(api.request,[query])
res = vectordb.query(query_vector[query])
print([x.split("||||")[0].strip() for x in res])
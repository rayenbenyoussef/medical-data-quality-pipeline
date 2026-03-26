import pandas as pd
import os
#from utils import plotBarNulls

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

df_edstays = pd.read_csv(os.path.join(BASE_DIR,'data','raw','edstays.csv'))
df_triage = pd.read_csv(os.path.join(BASE_DIR,'data','raw','triage.csv'))
df_vitalsign = pd.read_csv(os.path.join(BASE_DIR,'data','raw','vitalsign.csv'))
df_diagnosis = pd.read_csv(os.path.join(BASE_DIR,'data','raw','diagnosis.csv'))
df_medrecon = pd.read_csv(os.path.join(BASE_DIR,'data','raw','medrecon.csv'))
df_pyxis = pd.read_csv(os.path.join(BASE_DIR,'data','raw','pyxis.csv'))

'''
    ploting the frequancy of null values in each dataframe to visualize the extent of missing data

plotBarNulls(df_edstays, 'Null Count of ED Stays DataFrame')
plotBarNulls(df_triage, 'Null Count of Triage DataFrame')
plotBarNulls(df_vitalsign, 'Null Count of Vital Signs DataFrame')
plotBarNulls(df_diagnosis, 'Null Count of Diagnosis DataFrame')
plotBarNulls(df_medrecon, 'Null Count of Medication Recon DataFrame')
plotBarNulls(df_pyxis, 'Null Count of Pyxis DataFrame')

'''
print(df_edstays.info())
#mapping the arrival transport modes to numerical codes for easier analysis and modeling
print(df_edstays["arrival_transport"].unique())
df_transport=[
    (1, 'Ambulance'),
    (2, 'Walk-in'),
    (3, 'Other'),
    (4, 'Unknown')
]
df_transport=pd.DataFrame(df_transport, columns=['Code', 'Transport'])
df_transport.to_csv(os.path.join(BASE_DIR,"data","processed","transport_mapping.csv"), index=False)
df_edstays['arrival_transport'] = df_edstays['arrival_transport'].map({'AMBULANCE': 1, 'WALK IN': 2, 'OTHER': 3, 'UNKNOWN': 4})

time_regEx=r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
print(str(df_edstays[df_edstays["intime"].astype(str).str.match(time_regEx)].shape[0])+" / "+str(df_edstays.shape[0])+" in intime match the datetime format")
print(str(df_edstays[df_edstays["outtime"].astype(str).str.match(time_regEx)].shape[0])+" / "+str(df_edstays.shape[0])+" in outime match the datetime format")
print(str(df_edstays[df_edstays["intime"]<=df_edstays["outtime"]].shape[0])+" / "+str(df_edstays.shape[0])+" in datetime logicly correct (intime <= outtime)")

print(df_edstays["gender"].unique())
df_gender=[
    (1,"M"),
    (2,"F")
]
df_gender=pd.DataFrame(df_gender,columns=["Code","Gender"])
df_gender.to_csv(os.path.join(BASE_DIR,"data","processed","gender_mapping.csv"), index=False)
df_edstays['gender']=df_edstays['gender'].map({'M':1, 'F':2})

print(df_edstays['race'].unique())
df_race=[
    (1, 'UNKNOWN'),
    (2, 'EUROPEAN'),
    (3, 'HISPANIC/LAT')
]
df_edstays['race']=df_edstays['race'].map({'PATIENT DECLINED TO ANSWER':1,'UNKNOWN':1,})


print(df_edstays.info())
print(df_edstays.head())





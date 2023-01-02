# Import necessary libraries:

import numpy as np
import pandas as pd 
df = pd.read_csv('immo_data.csv')

#Delete unnecessary columns:
df = df.drop(['new_price','classified_condition_isNewlyBuilt','classified_parking_parkingSpaceCount_outdoor',
'classified_parking_parkingSpaceCount_indoor','classified_wellnessEquipment_hasSwimmingPool',
'classified_specificities_SME_office_exists','classified_outdoor_terrace_exists','classified_outdoor_garden_surface',
'classified_basementExists','classified_atticExists','bedroom_count','classified_condition_isNewlyBuilt',
'classified_outdoor_terrace_exists','classified_outdoor_garden_surface','classified_basementExists','classified_atticExists',
'classified_certificates_primaryEnergyConsumptionLevel','classified_building_condition','classified_building_constructionYear',
'classified_visualisationOption','classified_zip','classified_transactionType','Unnamed: 0'], axis=1)

##Delete rows with incomplete information:
df = df.dropna()
df=df.drop_duplicates(inplace=False)

#Delete rows that contain zero value in columns:
df = df[df.bedroom != 0]
df = df[df.construction_Year != 0]
df = df[df.price !=0]
df = df[df.classified_id !=0]

#check to be sure no empty value in dataset:
df.isna().any().sum()

#Arrange the houses that are located in the same city together
df = df.sort_values(by ='province' )

#Delete provinces that do not belong to Belgium:
df = df[df["location"].str.contains("Luxembourg") == False]

#svae the clean dataset
df.to_csv('immo_data.csv', index=False)


# Author: Aíquis Gomes (aiquis.gomes@turner.com)
# Date Created: 2017-06-10
# The script goal is to add all LG IMEI files send by them weekly in only one xlsx file to make it easy to upload to the system.
# The files they send weekly correspond to the devices production of the week of devices that have access to the EI Plus promotion (3 months of free subscription).


import glob
import pandas as pd

path = r'/home/aiquis/EI/lg_imeis/' #files path

#Create a list with all the path + files desired
allFiles = glob.glob(path+"*_26052017_*.xlsx") #change the date here for the first date in the file names for the period desired

imeis = pd.DataFrame()
aux_list = []

#In this loop each file of allFiles is read and stored in a aux_list, generating a list of list, where each inside list
#represents the content of each of the files read
for file in allFiles:
    fileread = pd.read_excel(file, index_col = None, header = 0)
    aux_list.append(fileread)
    
#Concatenating the list of files to make a big list with all the records of all files and assigning it to the DataFrame
imeis = pd.concat(aux_list)

#Deleting the 'SHIPMENT' column that is useless to the system
imeis.drop('SHIPEMENT', axis = 1, inplace = True)

#Creating the spreadsheet that is going to be uploaded to the system
writer = pd.ExcelWriter('home/aiquis/EI/' + 'imeis_upload.xlsx', engine = 'xlsxwriter')
imeis.to_excel(writer, index = False)
writer.save()
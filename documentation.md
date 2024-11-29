# Changes made

### Get the Data

At first one needs to download the data. Here the new .csv files are located under the folder _data_ <br>

1. https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/start.html <br> The files are located at the bottom of the page. Make sure you downlaod the _.csv_ file and not the _.xslx_ <br> Name: (Liste der Ladesäulen (CSV) (csv / 11 MB) )
2. https://www.suche-postleitzahl.org/downloads <br> At the right handside there is a column named _PLZ Download_. In there is an entry named _plz_einwohner_.<br> You need to download it as .csv file

#### Cleansing the files
The file _plz_einwohner_ is already good as it is. But the other one needs to be cleaned first.<br>
The file _Ladesaeulenregister.csv_ has a header which needs to be removed. You may delete everything up until "Betreiber;Straße;Hausnummer;Adresszusatz;Postleitzahl, ..."

## Modify main.py
The further data cleansing is done by python. There are already functions written under _core/methods.py._ <br>
In this file you need to call _preprop_resid_ on _plz_einwohner_ and _preprop_lstat_ on _Ladesaeulenregister.csv_. The files need to be read in as a pandas Dataframe first. <br>

At last you need to call the method _make_streamlit_electric_Charging_resid_ from _core/methods.py._.<br> 
It takes in the two dataframes, the one containing the data from _Ladesaeulenregister.csv_ needs to be given first.

### Further Changes
I am not sure why, but the _preprop_lstat_ removes the number of charging_stations. It needs to be added.<br>
prior:

    dframe2               	= dframe.loc[:,['Postleitzahl', 'Bundesland', 'Breitengrad', 'Längengrad', 'Nennleistung Ladeeinrichtung [kW]']]
    dframe2.rename(columns  = {"Nennleistung Ladeeinrichtung [kW]":"KW", "Postleitzahl": "PLZ"}, inplace = True)

updated:
   
    dframe2               	= dframe.loc[:,['Postleitzahl', 'Bundesland', 'Breitengrad', 'Längengrad', 'Nennleistung Ladeeinrichtung [kW]', 'Anzahl Ladepunkte']]
    dframe2.rename(columns  = {"Nennleistung Ladeeinrichtung [kW]":"KW", "Postleitzahl": "PLZ", "Anzahl Ladepunkte": "Number"}, inplace = True)

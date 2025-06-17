#Bibliotheken importieren
import pypsa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Daten einlesen
pv_erzeugung = 
wind_erzeugung = 
netzbezug = np.inf
netzeinspeisung = 
elektrische_last = 
thermische_last = 

#Leistungen
elektrolyse_leistung = 
brennstoffzelle_leistung =
h2_speicher_leistung = 
batterie_leistung = 

#Energien
h2_speicher_energie = 
batterie_energie = 

#Kosten
elektrolyse_kosten = 
brennstoffzelle_kosten = 
pv_kosten = 
pv_annuity = 
windkosten = 
wind_annuity =
stromkosten = 
gaskosten = 


df_data = 


#PyPSA Netzwerk erstellen
network = pypsa.Network()
network.set_snapshots(df_data.index)


#Basissystem aufbauen
network.add('Bus', name = 'Strom')
network.add('Bus', name = 'Netz')
network.add('Bus', name = 'storage_bus')

network.add('Load', name = 'electrical_load', bus = 'Netz', p_set = )

network.add('Generator', name = 'grid', bus = 'Netz', p_nom = , marginal_cost = )
network.add('Generator', name = 'PV', bus = 'Strom', p_max_pu = , capital_cost = )
network.add('Generator', name = 'Wind', bus = 'Strom', p_max_pu = , capital_cost = )
network.add('Generator', name = 'infeed', bus = 'Strom', p_nom = , marginal_cost = , sign = -1 )

network.add('Link', name = 'electricity_link', bus0 = 'Strom', bus1 = 'Netz', p_nom = , efficiency = )
network.add('Link', name = 'einspeicherung', bus0 = 'Strom', bus1 = 'storage_bus', p_nom = , efficiency = )
network.add('Link', name = 'auspeicherung', bus0 = 'storage_bus', bus1 = 'Strom', p_nom = , efficiency = )

network.add('Storage_Unit', name = 'electricity_storage', bus = 'storage', p_nom = , capital_cost = )

#thermisches System
network.add('Bus', name = 'gas_bus')
network.add('Bus', name = 'thermal_bus')
network.add('Bus', name = 'thermal_storage_bus')

network.add('Load', name = 'thermal_load', bus = 'thermal_bus', p_set =  )

network.add('Storage_Unit', name = 'h2_storage', bus = 'gas_bus', p_nom = , capital_cost = )
network.add('Storage_Unit', name = 'thermal_storage', bus = 'thermal_storage_bus', p_nom = , capital_cost = )

network.add('Link', name = 'electrolysis', bus0 = 'Netz', bus1 = 'gas_bus', p_nom = , efficiency = )
network.add('Link', name = 'fuelcell', bus0 = 'gas_bus', bus1 = 'Netz', p_nom = , efficiency = )
network.add('Link', name = 'heatpump', bus0 = 'Netz', bus1 = 'thermal_bus', p_nom = , efficiency = )
network.add('Link', name = 'einspeicherung_wärme', bus0 = 'thermal_bus', bus1 = 'thermal_storage_bus', p_nom = , efficiency = )
network.add('Link', name = 'ausspeicherung_wärme', bus0 = 'thermal_storage_bus', bus1 = 'thermal_bus', p_nom = , efficiency = )
network.add('Link', name = 'gas_combustion', bus0 = 'gas_bus', bus1 = 'thermal_bus', p_nom = , efficiency = )

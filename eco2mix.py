import wget
import os

REGIONS = [
    "Auvergne-Rhône-Alpes",
    "Bourgogne-Franche-Comté",
    "Bretagne",
    "Centre-Val-de-Loire",
    "Grand-Est",
    "Hauts-de-France",
    "Ile-de-France",
    "Normandie",
    "Nouvelle-Aquitaine",
    "Occitanie",
    "PACA",
    "Pays-de-la-Loire"
]

FILETYPES = [
    "En-cours-Consolide",
    "En-cours-TR",
    "Annuel-Definitif_2013",
    "Annuel-Definitif_2014",
    "Annuel-Definitif_2015",
    "Annuel-Definitif_2016",
    "Annuel-Definitif_2017",
    "Annuel-Definitif_2018",
    "Annuel-Definitif_2019",
    "Annuel-Definitif_2020",
]

#from unidecode import unidecode

for region in REGIONS:
    for filetype in FILETYPES:
        regionurl = region
        if filetype == "En-cours-TR" and region == "Auvergne-Rhône-Alpes":
            regionurl = "Auvergne-Rhone-Alpes"
        elif filetype == "En-cours-TR" and region == "Bourgogne-Franche-Comté":
            regionurl = "Bourgogne-Franche-Comte"
        url = "https://eco2mix.rte-france.com/download/eco2mix/eCO2mix_RTE_{}_{}.zip".format(regionurl, filetype)
        
        #create regions folders inside data
        if not os.path.exists("data/eco2mix/{}".format(region)):
            os.makedirs("data/eco2mix/{}".format(region))

        # download file
        wget.download(url, "data/eco2mix/{}/{}.zip".format(region, filetype))
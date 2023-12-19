import wget
import os

URL = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/"

#download file for all months and years
for year in range(2013, 2024):
    for month in range(1, 13):
        # format url
        url = URL + "synop.{}{}.csv.gz".format(
            str(year), str(month).zfill(2)
        )

        #create year folders inside data
        if not os.path.exists("data/meteo/{}".format(year)):
            os.makedirs("data/meteo/{}".format(year))

        # download file
        wget.download(url, "data/meteo/{}/{}.csv.gz".format(year, str(month).zfill(2)))

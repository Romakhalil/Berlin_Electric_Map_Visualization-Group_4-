import os
currentWorkingDirectory = os.path.dirname(__file__)

# -----------------------------------------------------------------------------

os.chdir(currentWorkingDirectory)
print("Current working directory\n" + os.getcwd())

import pandas                        as pd
import geopandas                     as gpd
from shapely                         import wkt

from core import methods             as m1
from core import HelperTools         as ht
from config                          import pdict

# -----------------------------------------------------------------------------
@ht.timer
def main():
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""

    dataset_path = os.path.join(currentWorkingDirectory, "datasets")
    data_path = os.path.join(currentWorkingDirectory, "data")

    df_geodat_plz = pd.read_csv(os.path.join(dataset_path, pdict["file_geodat_plz"]), sep=";", decimal=",")
    df_residents = pd.read_csv(os.path.join(data_path, pdict["file_residents"]), sep=",", decimal=".")
    df_residents = m1.preprop_resid(df_residents, df_geodat_plz, pdict)
    gdf_residents = gpd.GeoDataFrame(df_residents, geometry=df_geodat_plz["geometry"].apply(wkt.loads))

    df_lstation = pd.read_csv(os.path.join(data_path, pdict["file_lstations"]), sep=";", decimal=",")
    df_lstation = m1.preprop_lstat(df_lstation, df_geodat_plz, pdict)
    gdf_lstation = gpd.GeoDataFrame(df_lstation, geometry=df_geodat_plz["geometry"].apply(wkt.loads))

    m1.make_streamlit_electric_Charging_resid(df_lstation, df_residents, gdf_lstation, gdf_residents)





if __name__ == "__main__": 
    main()


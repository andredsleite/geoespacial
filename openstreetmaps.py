#encode utf-8
import geopandas #conda install -c ioos geopandas , caso use o jupyter notebook e não possua a lib.
import fiona
import matplotlib
%matplotlib inline
#!pip install ipyleaflet;  se nao tiver instalado a lib do leaflet
# !jupyter nbextension enable --py --sys-prefix ipyleaflet; para ativar a extensao
import ipyleaflet
from ipyleaflet import *
map1= Map(center=[ -15.779,-47.929],zoom=10)
map1; #openstreetmaps basico
map1.layers =[basemap_to_tiles(basemaps.CartoDB.DarkMatter)] 
map1; #base com fundo preto. para acessar outras bases digite: basemaps.'tab'(a tecla tab mesmo)

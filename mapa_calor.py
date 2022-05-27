import warnings; warnings.simplefilter('ignore')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib; matplotlib.style.use('ggplot')
from matplotlib.patches import Arc, Circle
from paint_field import paint_field


# Fichero con información de jugadores

ruta_jugadores = "inputs/eventos_2020_2021.csv"
df = pd.read_csv(ruta_jugadores)


# SELECCION DE JUGADOR DE INTERÉS

df_player = df['player']== "Lucas Pérez"

player_map = (df[df_player]['x'],df[df_player]['y'])

color_campo = "green"

paint_field.player_events(color_campo, player_map)

import pandas as pd
from colour import Color
import math

def colorToHex(color):
  return color.hex

def colorRampPalette(n: int, color_list: list):
  color_ramp_list = [Color(color_list[0])]
  n_colors = len(color_list)
  n_i = math.ceil((n - n_colors) / (n_colors - 1)) + 2
  for i, color_i in enumerate(color_list[1:]):
    color_ramp = list(Color(color_list[i]).range_to(Color(color_i), n_i))
    color_ramp_list = color_ramp_list + color_ramp[1:]
  return list(map(colorToHex, color_ramp_list[:n]))

def colorRampPaletteFromDfColumn(df: pd.DataFrame, column: str, color_list: list):
  n = len(df[column].unique())
  return colorRampPalette(n, color_list)


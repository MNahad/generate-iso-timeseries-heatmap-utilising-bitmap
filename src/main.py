import sys
import datetime
from PIL import Image
import numpy as np
import pandas as pd
from typing import Callable
import numpy.typing as npt


def get_img_array(path: str) -> npt.NDArray:
    _img = Image.open(path).convert('L')
    return np.array(_img)


def convert_days_of_year_to_dates(year: int) -> Calla
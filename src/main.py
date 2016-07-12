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


def convert_days_of_year_to_dates(year: int) -> Callable[[int], str]:
    _d = datetime.date.fromisocalendar(year, 1, 1)
    return lambda day: (_d + datetime.timedelta(day)).isoformat()


def save_csv(data: list[tuple[str, int]], path: str) -> None:
    _df = pd.DataFrame(data, columns=['date', 'value'])
    _df.to_csv(path, index=None)


if __name__ == "__main__":
    YEAR = datetime.datetime.now().year
    IMG_PATH = 'img.bm
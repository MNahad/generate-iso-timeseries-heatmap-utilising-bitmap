# Generate Iso Timeseries Heatmap Utilising Bitmap

### Given a bitmap heatmap file, this code can generate a CSV file with ISO 8601 timeseries values.

## Requirements

1. A bitmap file with dimensions 53 x 7 (i.e. 53 weeks and 7 days per week).
1. Python 3

## Setup

1. Install the required packages using `pip install -r requirements.txt`

## API

`python3 src/main.py [YEAR] [IMG_PATH] [CSV_PATH] [REVERSE_HEATMAP]`

### Options

`YEAR` - Specifies the ISO calendar year (default is current year)

`IMG_PATH` - Path to the heatmap image (default is `img.bmp`)

`CSV_PATH` - Path to the output CSV file (default is `csv.csv`)

`REVERSE_HEATMAP` - Flag to reverse the colour values i.e. lighter colours are higher (default is `0`)

## Examples

`python3 src/main.py`

`python3 src/main.py 2016 img.bmp csv.csv 1`

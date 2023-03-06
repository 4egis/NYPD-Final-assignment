import pandas as pd

files = {
    'GDP': 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv',
    'GDP_meta_country': 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562/Metadata_Country_API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv',
    'GDP_meta_indicator': 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562/Metadata_Indicator_API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv',
    'POP': 'API_SP.POP.TOTL_DS2_en_csv_v2_4751604/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv',
    'POP_meta_country': 'API_SP.POP.TOTL_DS2_en_csv_v2_4751604/Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv',
    'POP_meta_indicator': 'API_SP.POP.TOTL_DS2_en_csv_v2_4751604/Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv',
    'co2_emissions': 'co2-fossil-by-nation_zip/data/fossil-fuel-co2-emissions-by-nation_csv.csv'
}

def load_file(path):
    df = pd.read_csv(path)
    return df

def load_data():
    gdp = load_file(files['GDP'])
    pop = load_file(files['POP'])
    co2 = load_file(files['co2_emissions'])
    return gdp, pop, co2


import pandas as pd
import numpy as np


files = {
    'GDP': 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv',
    'POP': 'API_SP.POP.TOTL_DS2_en_csv_v2_4751604/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv',
    'co2_emissions': 'co2-fossil-by-nation_zip/data/fossil-fuel-co2-emissions-by-nation_csv.csv'
}

def load_file(path):
    df = pd.read_csv(path)
    return df

def load_data(gdp_file, pop_file, co2_file):
    gdp = load_file(gdp_file)
    pop = load_file(pop_file)
    co2 = load_file(co2_file)
    return gdp, pop, co2

def load_and_preprocess_data(gdp_file, pop_file, co2_file, start = None, koniec = None):
    gdp, pop, co2 = load_data(gdp_file, pop_file, co2_file)

    # extract years from datasets
    gdp_years = gdp.columns[4:len(gdp.columns) - 1].values
    pop_years = pop.columns[4:len(pop.columns) - 1].values
    co2_years = co2['Year'].unique()

    if start != None and koniec != None:
        if start >= koniec:
            raise Exception("start >= koniec")
        elif start - koniec < 10:
            raise Exception("start - koniec < 10, nie moge obliczyc zad3")
        elif start < min(co2_years):
            start = min(co2_years)
            #raise Exception("start < min(co2_years)")
        elif koniec > max(co2_years):
            koniec = max(co2_years)
            #raise Exception("koniec > max(co2_years)")

        if start != None and koniec == None:
            koniec = max(co2_years)
        elif start == None and koniec != None:
            start = min(co2_years)

        _co2_years = [
            year for year in co2_years
            if start <= year <= koniec
        ]
        co2_years = _co2_years

    co2_years = list(map(str, co2_years))

    # find common years in all datasets
    common_years = np.intersect1d(gdp_years, pop_years)
    common_years = np.intersect1d(common_years, co2_years)

    # extract common years from datasets
    gdp = gdp[['Country Name'] + list(common_years)]
    pop = pop[['Country Name'] + list(common_years)]
    common_years = list(map(int, common_years))
    co2 = co2[co2['Year'].isin(common_years)]

    # reshape co2 dataset
    co2 = co2[['Year', 'Country', 'Total']]
    co2 = co2.pivot(index="Country", columns="Year", values="Total")
    co2 = co2.reset_index()
    co2.rename(columns={'Country': 'Country Name'}, inplace=True)
    co2.columns = co2.columns.astype(str)

    # gdp/pop contry to capital letters
    gdp['Country Name'] = gdp['Country Name'].str.upper()
    pop['Country Name'] = pop['Country Name'].str.upper()

    # find common countries in all datasets
    common_countries = np.intersect1d(gdp['Country Name'].unique(), pop['Country Name'].unique())
    common_countries = np.intersect1d(common_countries, co2['Country Name'].unique())

    # extract common countries from datasets
    gdp = gdp[gdp['Country Name'].isin(common_countries)]
    pop = pop[pop['Country Name'].isin(common_countries)]
    co2 = co2[co2['Country Name'].isin(common_countries)]

    # concatenate datasets and group by country
    df = pd.concat([gdp, pop, co2], keys=['gdp', 'pop', 'co2'], names=['WHAT', None]).reset_index(level='WHAT')
    df.reset_index(drop=True, inplace=True)

    return df
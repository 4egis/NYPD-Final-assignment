from IO import load
import numpy as np
import pandas as pd



gdp, pop, co2 = load.load_data()


#extract years from datasets
gdp_years = gdp.columns[4:len(gdp.columns)-1].values
pop_years = pop.columns[4:len(pop.columns)-1].values
co2_years = co2['Year'].unique()
co2_years = list(map(str, co2_years))

#find common years in all datasets
common_years = np.intersect1d(gdp_years, pop_years)
common_years = np.intersect1d(common_years, co2_years)

#extract common years from datasets
gdp = gdp[['Country Name'] + list(common_years)]
pop = pop[['Country Name'] + list(common_years)]
common_years = list(map(int, common_years))
co2 = co2[co2['Year'].isin(common_years)]

#reshape co2 dataset
co2 = co2[['Year', 'Country', 'Total']]
co2 = co2.pivot(index="Country", columns="Year", values="Total")
co2 = co2.reset_index()
co2.rename(columns = {'Country':'Country Name'}, inplace = True)
co2.columns = co2.columns.astype(str)

#gdp/pop contry to capital letters
gdp['Country Name'] = gdp['Country Name'].str.upper()
pop['Country Name'] = pop['Country Name'].str.upper()

#find common countries in all datasets
common_countries = np.intersect1d(gdp['Country Name'].unique(), pop['Country Name'].unique())
common_countries = np.intersect1d(common_countries, co2['Country Name'].unique())

#extract common countries from datasets
gdp = gdp[gdp['Country Name'].isin(common_countries)]
pop = pop[pop['Country Name'].isin(common_countries)]
co2 = co2[co2['Country Name'].isin(common_countries)]

#find country with max CO2 for each year
max_co2_countries = []
for year in common_years:
    max_co2_country = co2[str(year)].idxmax()
    max_co2_countries.append(max_co2_country)

print(max_co2_countries)

"""# concatenate datasets and group by country
df = pd.concat([gdp, pop, co2], keys=['gdp', 'pop', 'co2'], names=['WHAT', None]).reset_index(level='WHAT')
df.reset_index(drop=True, inplace=True)
df = df.groupby('Country Name')"""




"""# find max CO2 for each year
max_co2_countries = []
for year in common_years:
    max_co2_country = df[str(year)].idxmax()[0]
    max_co2_countries.append(max_co2_country)


# print results
for year, country in zip(common_years, max_co2_countries):
    print(f"The country with the highest CO2 emissions in {year} was {country}.")
"""


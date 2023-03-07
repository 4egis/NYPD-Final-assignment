from IO import load
from analize import utils
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("gdp_input_file", help="path to file with gdp data")
parser.add_argument("pop_input_file", help="path to file with population data")
parser.add_argument("co2_input_file", help="path to file with co2 emissions data")
parser.add_argument(
    "count_lines", type=int, default=10, nargs="?", help="Number of lines to be copied, default 10"
)
parser.add_argument('-start', type=int)
parser.add_argument('-koniec', type=int)


def zad1(df):
    """ Zadanie nr 1 """
    print('\n\n########## PUNKT PIERWSZY ##########\n')
    highest_co2_per_capita, info = utils.find_highest_co2_per_capita(df)
    print(info)
    print(highest_co2_per_capita.head())

    utils.test_first_task(df)


def zad2(df):
    """ Zadanie nr 2 """
    print('\n\n########## PUNKT DRUGI ##########\n')
    highest_gdp_per_capita, info = utils.find_highest_gdp_per_capita(df)
    print(info)
    print(highest_gdp_per_capita.head())


def zad3(df):
    """ Zadanie nr 3 """
    print('\n\n########## PUNKT TRZECI ##########\n')
    the_highest_first, the_lowest_first, info = utils.co2_per_capita_over_10_years(df)
    print(info)

    top_x = 10  # Ile pierwszych chcemy wyprintować

    print(f'{top_x} krajów z najwyższą różnicą w latach 2014-2005\n')
    print(the_highest_first.head(top_x))

    print(f'\n\n{top_x} krajów z najniższą różnicą w latach 2014-2005\n')
    print(the_lowest_first.head(top_x))

    utils.test_third_task(df)


args = parser.parse_args()
df = load.load_and_preprocess_data(gdp_file=args.gdp_input_file,
                                   pop_file=args.pop_input_file,
                                   co2_file=args.co2_input_file,
                                   start=args.start,
                                   koniec=args.koniec)
zad1(df)
zad2(df)
zad3(df)

# #scratch pad
# # """#find country with max CO2 for each year
# max_co2_countries = []
# for year in common_years:
#     max_co2_country = co2[str(year)].idxmax()
#     max_co2_countries.append(max_co2_country)

# print(max_co2_countries)

# """

# """# find max CO2 for each year
# max_co2_countries = []
# for year in common_years:
#     max_co2_country = df[str(year)].idxmax()[0]
#     max_co2_countries.append(max_co2_country)


# # print results
# for year, country in zip(common_years, max_co2_countries):
#     print(f"The country with the highest CO2 emissions in {year} was {country}.")
files = {
    'GDP': 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv',
    'POP': 'API_SP.POP.TOTL_DS2_en_csv_v2_4751604/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv',
    'co2_emissions': 'co2-fossil-by-nation_zip/data/fossil-fuel-co2-emissions-by-nation_csv.csv'
}

import pandas as pd
import numpy as np


def find_highest_co2_per_capita(df):

    years = df.columns[2:] # Wybieram tylko lata z kolumn
    countries = df['Country Name'].unique()

    co2_per_capita = pd.DataFrame(columns=years, index=countries)


    for country in countries:
        for year in years:
            df_temporary = df[df['Country Name'] == country] # Tworze pomocniczy dataframe z jednym krajem
            co2 = df_temporary[df_temporary['WHAT'] == 'co2'][year].values[0] # Biore wartosc co2 i pop dla danego roku
            pop = df_temporary[df_temporary['WHAT'] == 'pop'][year].values[0]

            if True in pd.isna([co2, pop]): # Jeśli pop lub co2 jest nan'em to nie obliczam stosunku
                ratio = np.nan
            else: # Jeśli obie wartości istnieja, to obliczam stosunek
                ratio = co2/pop
            # Zapisuję ten stosunek w odpowiednim miejscu w dataframe
            co2_per_capita.at[country, year] = ratio


    cols = [[f'Kraj_{i}', f'Emisja_na_osobe_{i}', f'Calkowita_emisja_{i}'] for i in range (1, 6)] # Tworzę odpowiednie kolumny do nowego dataframe
    cols = sum(cols, []) # doprowadzam kolumny do odpowiedniej postaci
    highest_co2_per_capita = pd.DataFrame(columns=cols, index=years) # Tworze nowy dataframe
    # W tym dataframie bedzie zapisywane top 5 krajów z najwiekszym co2/pop 
    # Kraje są poszeregowane malejąco.
    
    for year in years:
        df_temporary = co2_per_capita[year] # Tworze tymczasowy dataframe w ktorym sa dane tylko dla jednego roku
        top5 = df_temporary.sort_values(ascending=False).head() # Sortuje malejąco i biore top5
        top5 = top5.to_dict() # Zmieniam top5 slownik

        i = 1 # Zmienna pomocnicza do numerowania kolumn
        for key, value in top5.items():
            #key - nazwa kraju
            #value - wartosc stosunku co2/pop
            highest_co2_per_capita.at[year, f'Kraj_{i}'] = key # W wierszu 'year' i kolumnie 'Kraj_{i}' zapisuje nazwe kraju
            highest_co2_per_capita.at[year, f'Emisja_na_osobe_{i}'] = value # To samo ale wartosc stosunku co2/pop
            co2_total = df[(df['Country Name'] == key) & (df['WHAT'] == 'co2')][year].values[0] # wartosc calkowitego co2 dla kraju
            highest_co2_per_capita.at[year, f'Calkowita_emisja_{i}'] = co2_total # zapisuje odszukana wartosc w odpowiednim miejscu
            i += 1


    info = """[INFO] Pięć krajów dla każdego roku o największej emisji CO2 na osobę.
Wyświetlono początek obiektu typu pd.DataFrame, w którym zapisano
rozpatrywany rok, nazwę kraju z największą emisją na mieszkańca,
wartość emisji na mieszkańca oraz całkowitą wartość emisji w danym roku.
Kraje poszeregowano w taki sposób, że wartość emisji na mieszkańca maleje.\n\n"""


    return highest_co2_per_capita, info


def find_highest_gdp_per_capita(df):
    years = df.columns[2:] # Wybieram tylko lata z kolumn
    countries = df['Country Name'].unique()

    gdp_per_capita = pd.DataFrame(columns=years, index=countries)


    for country in countries:
        for year in years:
            df_temporary = df[df['Country Name'] == country] # Tworze pomocniczy dataframe z jednym krajem
            gdp = df_temporary[df_temporary['WHAT'] == 'gdp'][year].values[0] # Biore wartosc gdp i pop
            pop = df_temporary[df_temporary['WHAT'] == 'pop'][year].values[0]

            if True in pd.isna([gdp, pop]): # Jeśli brakuje danych dla gdp lub pop to nie obliczam stosunku
                ratio = np.nan
            else: # Jeśli obie wartości są znane, to obliczam stosunek
                ratio = gdp/pop

            # Zapisuję ten stosunek w odpowiednim miejscu w dataframe
            gdp_per_capita.at[country, year] = ratio


    cols = [[f'Kraj_{i}', f'Dochod_na_osobe_{i}', f'Calkowity_dochod_{i}'] for i in range (1, 6)] # Tworzę odpowiednie kolumny do nowego dataframe
    cols = sum(cols, []) # doprowadzam kolumny do odpowiedniej postaci
    highest_gdp_per_capita = pd.DataFrame(columns=cols, index=years)
    # W tym dataframie bedzie zapisywane top 5 krajów z najwiekszym gdp/pop 
    # Kraje są poszeregowane malejąco, tzn. Emisja_na_osobe_1 jest wieksza niz Emisja_na_osobe_2 itd.
    
    for year in years: # Przechodze po latach
        df_temporary = gdp_per_capita[year] # Tworze tymczasowy dataframe w ktorym sa dane tylko dla jednego roku
        top5 = df_temporary.sort_values(ascending=False).head() # Sortuje malejąco i biore top5
        top5 = top5.to_dict() # Zmieniam top5 slownik

        i = 1 # pomocniczy iterator zeby zapisywac do odpowiednich kolumn
        for key, value in top5.items():
            # key - nazwa kraju
            # value - wartosc stosunku co2/pop
            highest_gdp_per_capita.at[year, f'Kraj_{i}'] = key # W wierszu 'year' i kolumnie 'Kraj_{i}' zapisuje nazwe kraju
            highest_gdp_per_capita.at[year, f'Dochod_na_osobe_{i}'] = value # To samo ale wartosc stosunku co2/pop
            gdp_total = df[(df['Country Name'] == key) & (df['WHAT'] == 'gdp')][year].values[0] # wartosc calkowitego gdp
            highest_gdp_per_capita.at[year, f'Calkowity_dochod_{i}'] = gdp_total # zapisuje odszukana wartosc w odpowiednim miejscu
            i+=1



    info = """[INFO] Pięć krajów dla każdego roku o największym dochodzie na mieszkańca.
Wyświetlono początek obiektu typu pd.DataFrame, w którym zapisano
rozpatrywany rok, nazwę kraju z największym dochodem na mieszkańca,
wartość dochodu na mieszkańca oraz całkowity dochód w danym roku.
Kraje poszeregowano w taki sposób, że wartość dochodu na mieszkańca maleje.\n\n"""


    return highest_gdp_per_capita, info


def co2_per_capita_over_10_years(df):
    countries = df['Country Name'].unique()
    years = df.columns[2:]
    start = years[-11]
    end = years[-1]
    cols = [start, end, f'roznica {end}-{start}'] # kolumny w nowych dataframie
    co2_changes = pd.DataFrame(columns=cols, index=countries)

    for country in countries:
        df_temporary = df[df['Country Name'] == country] # tworze tymczasowy dataframe z danymi tylko dla jednego kraju
        co2_start = df_temporary[df_temporary['WHAT'] == 'co2'][start].values[0] # wybieram co2 dla danego kraju w roku 'start'
        pop_start = df_temporary[df_temporary['WHAT'] == 'pop'][start].values[0] # wybieram pop dla danego kraju w roku 'start'
        ratio_start = co2_start/pop_start # stosunek co2/pop dla roku 2005

        co2_end = df_temporary[df_temporary['WHAT'] == 'co2'][end].values[0] # wybieram co2 dla danego kraju w roku 'end'
        pop_end = df_temporary[df_temporary['WHAT'] == 'pop'][end].values[0] # wybieram pop dla danego kraju w 'end'
        ratio_end = co2_end/pop_end # stosunek co2/pop dla roku 'end'

        ratio_diff = ratio_end - ratio_start # roznica stosunków w roku 'end' minus w roku 'start'

        co2_changes.at[country, start] = ratio_start # zapisuje w dataframie stosunek w roku 2005, 2014 oraz obliczona roznice
        co2_changes.at[country, end] = ratio_end
        co2_changes.at[country, f'roznica {end}-{start}'] = ratio_diff

    # Odrzucam te wiersze, gdzie różnica jest nan
    co2_changes = co2_changes[co2_changes[f'roznica {end}-{start}'].notna()]



    # Tworze dwa nowe dataframe'y - wartosci rosnaco i malejaco
    the_highest_first = co2_changes.sort_values(by=f'roznica {end}-{start}', ascending=False)
    the_lowest_first = co2_changes.sort_values(by=f'roznica {end}-{start}')

    info = """[INFO] Kraje, które najbardziej zmniejszyły i zwiększyły
emisję CO2 w ostatnich 10 latach (z danych), czyli w latach 2005-2014.
Przygotowano dwa obiektu typu pd.DataFrame, w których zapisano
nazwy krajów, wartość emisji CO2 w przeliczeniu na mieszkańca 
w roku 2004 oraz w roku 2015, a także różnicę pomiędzy tymi wartościami.
W przypadku określenia zakresu lat, brany jest ostatni rok z zakresu oraz 10 lat wcześniej.
Obiekty następnie posortowano, względem wartości tej różnicy. Pierwszy obiekt
przedstawia różnicę malejąco (pierwsze X krajów, które najbardziej zwiększyły
emisję CO2 na mieszkańca), natomiast w drugim obiekcie ta różnica rośnie
(pierwsze X krajów, któe najbardziej zmniejszyły tę wartość).
Osiem krajów zostało odrzuconych, ze względu na brak danych, pozwalających
na obliczenie wartości emisji CO2 na mieszkańca.\n\n"""

    return the_highest_first, the_lowest_first, info


def test_first_task(df):
    result, _ = find_highest_co2_per_capita(df)
    assert type(result) == pd.DataFrame # sprawdzam czy typ zwracanej zmiennej to dataframe
    assert result.index.is_unique # sprawdzam czy każdy rok jest unikalny
    assert result.isna().sum().sum() == 0 # sprawdzam czy suma nanów w CALYM dataframie jest równa 0

    # Tworze liste z kolumnami 'Kraj_1', ..., 'Kraj_5'
    # i dla kazdego wiersza w obiekcie pd.dataframe
    # wybieram wartosci tylko dla tych kolumn, czyli 5 nazw krajów
    # porównuje długosc np.array z tymi nazwami krajów - len(result[cols].iloc[i].values)
    # do długosci unikalnych wartosci w tej liście - len(np.unique(result[cols].iloc[i].values))
    # sprawdzam, czy kazda wartosc na tej liscie jest unikalna
    # i nie pojawia się przypadkowo ten sam kraj w dwoch lub wiecej kolumnach
    cols = [col for col in result.columns if 'Kraj' in col]
    for i in range(len(result)):
        assert len(np.unique(result[cols].iloc[i].values)) == len(result[cols].iloc[i].values)



def test_third_task(df):

    the_highest_first, the_lowest_first, info = co2_per_capita_over_10_years(df)

    years_start = the_highest_first.columns[0] # wyciagam poczatek przedzialu lat
    years_end = the_highest_first.columns[1] # wyciagam koniec przedzialu lat

    dfs = [the_highest_first, the_lowest_first]

    for df in dfs:
        assert df.index.is_unique # Unikatowe kraje w indeksie
        assert df.isna().sum().sum() == 0 # Suma nanów rowna 0
        
        for i in range(len(df)): # Czy zgadza sie roznica
            diff = df.iloc[i][f'roznica {years_end}-{years_start}']
            value_start = df.iloc[i][years_start]
            value_end = df.iloc[i][years_end]
            assert value_end - value_start == diff
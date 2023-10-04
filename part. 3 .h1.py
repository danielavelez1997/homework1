##
def total_registered_cases(countries,country_name):
    for country,values in countries.items():
        if country_name in country:
            x= sum(values)
            return x


list_countries={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
'Italy': [6, 8, 1, 7]}


total_registered_cases(list_countries,'Spain')
##

def total_registered_cases_per_country(countries):
    total_per_country={}
    for country, values in countries.items():
        total_per_country[country]= sum (values)
    return total_per_country

list_countries={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
'Italy': [6, 8, 1, 7]}
total_registered_cases_per_country(list_countries)


##
def total_registered_cases_per_country(countries):
    total_per_country={}
    for country, values in countries.items():
        total_per_country[country]= sum (values)
    return total_per_country

list_countries={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
'Italy': [6, 8, 1, 7]}
total_registered_cases_per_country(list_countries)

def country_with_most_cases(countries):
    total_per_country=total_registered_cases_per_country(countries)
    most_registered= max(total_per_country.items(),key=lambda x:x[1])
    return most_registered

list_countries={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
'Italy': [6, 8, 1, 7]}
country_with_most_cases(list_countries)
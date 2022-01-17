country_population = {"USA":331002651,"China":1439323776,"India":1380004385,"UK":67886011}
sorted_by_key = {key:value for key,value in sorted(country_population.items())}
sorted_by_value = {key:value for key,value in sorted(country_population.items(),key= lambda value:value[1])}
sorted_by_greatest_value = {key:value for key,value in sorted(country_population.items(),key= lambda value:value[1],reverse=True)}
print(sorted_by_key)
print(sorted_by_value)
print(sorted_by_greatest_value)
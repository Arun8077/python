cs_cources = {'hist', 'match', 'eng', 'hindi'}
art_cources = {'sanskrit', 'hindi', 'homesci'}
print(type(cs_cources))
print(cs_cources)
print(cs_cources)
print(cs_cources.intersection(art_cources)) ## will print the command value
print(cs_cources.difference(art_cources)) ## will print the different values in set-1 - cs_cources
print(cs_cources.union(art_cources)) ## It will print the combine unique cources in both.
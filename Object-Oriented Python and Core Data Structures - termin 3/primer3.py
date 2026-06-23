# Koristeći lambda izraz prečisti listu kategorija, 
# tako da nema beline pre ili nakon imena kategorije 
# i sva slova prebaci u mala.

raw_categories= ["   Electronics ", "    FASHION", "home  ", "Food "]

res = list(map(lambda x: x.lower().strip() , raw_categories))
#res = list(map(lambda x: x.lower() , raw_categories))
#res2 = list(map(lambda x: x.strip() , res))
print(res)
# Geef een bedrag voor alle producten
product1 = float(input("Hoeveel kost product 1?"))
product2 = float(input("Hoeveel kost product 2?"))
product3 = float(input("Hoeveel kost product 3?"))
product4 = float(input("Hoeveel kost product 4?"))
product5 = float(input("Hoeveel kost product 5?"))

# Tel alle bedragen bij elkaar op
subtotaal = product1 + product2 + product3 + product4 + product5
print (subtotaal)

# Bereken de belasting
belasting = 0.07 * subtotaal
print (belasting)

# Bereken het totale bedrag
totaal = subtotaal + belasting
print (totaal)

import matplotlib.pyplot as plt

labels = "Île-de-France", "Rhône-Alpes", "Provence Alpes\nCôte d'Azur", "Nord Pas de Calais"
areas = [12011, 43698, 31400, 12414]  # in km2
population = [11577, 6058, 4818, 4048]  # in million
colors = ['darkcyan', 'lightgreen', 'lightsteelblue', 'lightskyblue']
explode = (1, 0, 0, 0)

plt.pie(areas,
        # explode=explode,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        )
plt.axis('equal')
plt.savefig("france_region_areas.pdf")
plt.close()

plt.pie(population,
        # explode=explode,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        )

plt.axis('equal')
plt.savefig("france_region_population.pdf")
plt.close()

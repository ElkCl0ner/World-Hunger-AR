import matplotlib.pyplot as plt
import numpy as np

# Variables
years = []
for x in range(2001,2020):
    years.append(x)

numYears = len(years)

# Get data
file = open('data.txt', 'r')

# Get each line (pack of 3)
counter = 0
while True:
    counter += 1

    line = file.readline()

    # End loop if end-of-file reached
    if not line:
        print("Done")
        break

    insecurity = line[:-1].split(";")

    line = file.readline()

    if line == "\n":
        continue
    
    pop = line[:-1].split("\t")
    population = []
    for x in pop:
        population.append(float(x))

    line = file.readline()
    under = line.split("\t")
    undernourished = []
    for x in under:
        undernourished.append(float(x))
    

    # Plot
    yearsPlot = np.arange(numYears)
    plt.plot(yearsPlot, population, label = 'Total population')
    plt.plot(yearsPlot, undernourished, label = 'Undernourished population')
    plt.xlabel("Year")
    plt.ylabel("People (Millions)")
    plt.xticks(yearsPlot, years)
    #plt.yticks(np.arange(0,plt.gca().get_ylim()[1],1))
    plt.title(insecurity[0])
    plt.tick_params(axis ='x', rotation =60)
    plt.get_current_fig_manager().resize(1000, 1000)
    plt.legend()
    plt.gcf().set_size_inches(8, 6)
    plt.savefig('plots/image{}.png'.format(counter), dpi=100)
    plt.clf()

# End
file.close()

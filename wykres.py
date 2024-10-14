import pandas as pd
import matplotlib.pyplot as plt

# Tworzenie przykładowych danych
data = {
    'rok': [2020, 2021, 2022, 2023],
    'sprzedaż': [1500, 1800, 2200, 2500]
}
df = pd.DataFrame(data)

df.plot(x='rok', y='sprzedaż', marker='o')
plt.title("Sprzedaż w latach")
plt.xlabel("Rok")
plt.grid()
plt.show()

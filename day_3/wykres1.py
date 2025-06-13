import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 34, 56]

plt.plot(x, y, color="red")
plt.title("Wykres")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")

plt.savefig("wykres.pdf")
plt.show()

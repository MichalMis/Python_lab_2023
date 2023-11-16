import pandas as pd
import matplotlib.pyplot as plt

file_path = 'train.csv'
data = pd.read_csv(file_path)
# print(data)
#2_b
if data.duplicated().any():
    print("Dane zawierają duplikaty")
else:
    print("Dane nie zawierają duplikatów")

data = data.drop_duplicates()
#print(data)
if data.duplicated().any():
    print("Dane zawierają duplikaty")
else:
    print("Dane nie zawierają duplikatów")

#2_c

corr = data['age'].corr(data['limit_bal'])
print(f"Korelacja {corr}")

#2d 
data['total_bill_amt'] = data.filter(like = 'bill_amt').sum(axis=1)
print(data['total_bill_amt'])

#2e
oldest  = data.nlargest(10,'age')
#print(oldest)
oldest = oldest[['limit_bal', 'age'] + list(oldest.filter(like = 'education')) + ['total_bill_amt']]
print(oldest)

#2f
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Histogram limitu kredytu (subplot 1)
axes[0, 0].hist(data['limit_bal'], bins=20, color='skyblue')
axes[0, 0].set_title('Limit kredytu')
axes[0, 0].set_xlabel('Limit kredytu')
axes[0, 0].set_ylabel('Liczba klientów')

# Histogram wieku (subplot 2)
axes[0, 1].hist(data['age'], bins=20, color='salmon')
axes[0, 1].set_title('Wiek')
axes[0, 1].set_xlabel('Wiek')
axes[0, 1].set_ylabel('Liczba klientów')

# Zależność limitu kredytu od wieku (subplot 3)
axes[1, 0].scatter(data['age'], data['limit_bal'], color='green')
axes[1, 0].set_title('Zależność limitu kredytu od wieku')
axes[1, 0].set_xlabel('Wiek')
axes[1, 0].set_ylabel('Limit kredytu')

# Usunięcie pustego subplotu (4)
fig.delaxes(axes[1, 1])
plt.tight_layout()

# Wyświetlenie wykresu
plt.show()
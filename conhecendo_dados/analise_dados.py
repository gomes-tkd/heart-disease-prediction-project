import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados
data = pd.read_csv('heart.csv', sep=',', encoding='iso-8859-1')

# ==============================================================================
# 1. O GRÁFICO INTERATIVO (PLOTLY)
# ==============================================================================
hist1 = px.histogram(data, x='Age', nbins=100)
hist1.update_layout(width=800, height=500, title_text='Age Distribution (Interativo - Plotly)')
hist1.show()

# ==============================================================================
# 2. O HISTOGRAMA DE IDADE (SEABORN/MATPLOTLIB)
# ==============================================================================
plt.figure(figsize=(10, 6))
sns.histplot(
    data=data,
    x='Age',
    bins=100,
    color='orange',
    kde=True,
    stat='count'
)
plt.title('Age Distribution (Static)')
plt.show() # Fecha e exibe este gráfico

# ==============================================================================
# 3. A DISTRIBUIÇÃO DE SEXO (SEABORN/MATPLOTLIB)
# ==============================================================================
plt.figure(figsize=(8, 6))
sns.countplot(
    data=data,
    x='Sex',
    hue='Sex',
    palette='viridis',
)
plt.title('Sex Distribution')
plt.show() # Fecha e exibe este gráfico

# ==============================================================================
# 4. A DISTRIBUIÇÃO DE DOR NO PEITO (SEABORN/MATPLOTLIB)
# ==============================================================================
plt.figure(figsize=(10, 6))
sns.countplot(
    data=data,
    x='ChestPainType',
    hue='ChestPainType',
    palette='viridis',
)
plt.title('Chest Pain Type Distribution')
plt.show() # Fecha e exibe este gráfico


# ==============================================================================
# 5. A DISTRIBUIÇÃO DE PRESSÃO SANGUÍNEA EM REPOUSO (SEABORN/MATPLOTLIB)
# ==============================================================================
countRestingBP = data['RestingBP'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
sns.histplot(
    data=data,
    x='RestingBP',
    bins=100,
    # color='orange',
    kde=True,
    stat='count'
)
plt.title('Blood pressure')
plt.show() # Fecha e exibe este gráfico
print(countRestingBP)

# ==============================================================================
# 6. A DISTRIBUIÇÃO DE COLESTEROL SÉRICO (MG/DL) (SEABORN/MATPLOTLIB)
# ==============================================================================
cholesterolData = data['Cholesterol'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.histplot(
    data=data,
    x='Cholesterol',
    bins=100,
    color='orange',
    kde=True,
    stat='count'
)
plt.title('Cholesterol Distribution')
plt.show()
print(cholesterolData)

# ==============================================================================
# 7. A DISTRIBUIÇÃO DE AÇÚCAR NO SANGUE (SEABORN/MATPLOTLIB)
# ==============================================================================
blood_bs_data = data['FastingBS'].value_counts().sort_index()
print(blood_bs_data)
plt.figure(figsize=(10, 6))
sns.histplot(
    data=data,
    x='FastingBS',
    bins=100,
    color='orange',
    kde=True,
    stat='count'
)
plt.title('Fasting BS Distribution')
plt.show()

sns.countplot(
    data=data,
    x='FastingBS',
    hue='FastingBS',
    palette='viridis',
)
plt.title('Fasting BS Count Distribution')
plt.show()



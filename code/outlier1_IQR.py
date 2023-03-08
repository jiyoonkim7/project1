sns.boxplot(y=df['exercise'])

Q1=df['exercise'].quantile(0.25)
print("Q1:", Q1)

Q3=df['exercise'].quantile(0.75)
print("Q3:", Q3)

IQR=Q3-Q1
print("IQR: ", IQR)

lower_bound = Q1 - 1.5*IQR
print("Lower Bound:", lower_bound)

upper_bound = Q3 + 1.5*IQR
print("Upper Bound:", upper_bound)

df_clean = df[(df['exercise']>lower_bound)&(df['exercise']<upper_bound)]

sns.boxplot(y = df_clean['exercise'])
import matplotlib.pyplot as plt
import main

result_data_1 = {
    'Country': [i[0] for i in main.data_1],
    'Number of sportsmen': [i[1] for i in main.data_1]
}

result_data_2 = {
    'Medal': [i[0] for i in main.data_2],
    'Number of sportsmen': [i[1] for i in main.data_2]
}

result_data_3 = {
    'Games': [i[0] for i in main.data_3],
    'Number of sportsmen': [i[1] for i in main.data_3]
}


plt.bar(result_data_1['Country'], result_data_1['Number of sportsmen'], width=0.5)
plt.xlabel('Countries')
plt.ylabel('Number of sportsmen')
plt.show()

fig, ax = plt.subplots()
ax.pie(result_data_2['Number of sportsmen'], labels=result_data_2['Medal'], normalize=True)
plt.axis('equal')
plt.show()

plt.scatter(result_data_3['Games'], result_data_3['Number of sportsmen'])
plt.show()

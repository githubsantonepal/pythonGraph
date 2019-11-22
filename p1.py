
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(7,5))
names=['Santosh','Parbati','Sujina','Arya']
scores1=[89,78,93,57]
scores2=[78,76,77,87]
positions1=[0,1,2,3]
positions2=[0.4,1.4,2.4,3.4]
positionsx=[0.2,1.2,2.2,3.2]
plt.bar(positions1, scores1, width=0.4, color='g')
plt.bar(positions2, scores2, width=0.4)
plt.xticks(positionsx, names)
plt.show()

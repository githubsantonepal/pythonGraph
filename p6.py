#import matplotlib library
import matplotlib.pyplot as plt
from matplotlib import style

#website traffic data
#number of users visitors on the website
web_customers=[112,100,123,40,30]

#Time distribution in hrs
time_hrs=[4,6,10,16,20]

#select the style of the plot
style.use('ggplot')

#plot the website traffic data
plt.plot(time_hrs,web_customers, 'r-',label='website traffic')

#setting title of the plot
plt.title('Website Traffic')

#setting X axis
plt.xlabel('Hours')

#setting Y axis
plt.ylabel('No. of Users')

# To display the legend
plt.legend(loc=3)

#displaying the graph

plt.show()
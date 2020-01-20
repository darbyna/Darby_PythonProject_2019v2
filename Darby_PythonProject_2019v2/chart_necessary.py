from imports_necessary import *


#This will simply be the code series for the chart required for this project.


data= pd.read_csv(r'C:\Users\admin\Documents\Pileq_XonoRex_File.csv')
data.head()
data.sort_index()
data_plot= data.plot(kind= 'bar', title= 'Pileq Domination Statistics')
data_plot.set_xlabel('Planets of Interest') 
data_plot.set_ylabel('Counts by Billions')
data_plot.set_xticklabels(data['Column1'])
plt.show()


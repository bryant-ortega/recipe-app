from io import BytesIO 
import base64
import matplotlib.pyplot as plt

def get_graph():
   #create a BytesIO buffer for the image
   buffer = BytesIO()         

   #create a plot with a bytesIO object as a file-like object. Set format to png
   plt.savefig(buffer, format='png')

   #set cursor to the beginning of the stream
   buffer.seek(0)

   #retrieve the content of the file
   image_png=buffer.getvalue()

   #encode the bytes-like object
   graph=base64.b64encode(image_png)

   #decode to get the string as output
   graph=graph.decode('utf-8')

   #free up the memory of buffer
   buffer.close()

   #return the image/graph
   return graph

#chart_type: user input o type of chart,
#data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
  #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
  #AGG is preferred solution to write PNG files
  plt.switch_backend('AGG')

  #specify figure size
  fig=plt.figure(figsize=(6,3))

  if chart_type == '#1':
    # Bar chart of cooking times
    plt.bar(data['recipe_name'], data['category'])
    plt.xlabel('Recipe Name')
    plt.ylabel('Category')
    plt.xticks(rotation=45, ha='right')

  elif chart_type == '#2':
    # pie chart logic
    category_counts = data['category'].value_counts()
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

  elif chart_type == '#3':
    # Line chart logic
    # Assuming you have fields like 'date_added' and a numerical field like 'cooking_time'
    data = data.sort_values('date_added')
    plt.plot(data['date_added'], data['cooking_time'])
    plt.xlabel('Date Added')
    plt.ylabel('Cooking Time')
    plt.xticks(rotation=45)


  else:
    print ('unknown chart type')

  #specify layout details
  plt.tight_layout()

  #render the graph to file
  chart =get_graph() 
  plt.close(fig)  # Clear the figure after saving it
  return chart      
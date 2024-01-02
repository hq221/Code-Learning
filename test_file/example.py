import matplotlib.pyplot as plt

# Example data
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]

# Create a scatter plot
plt.scatter(x_values, y_values)

# Annotate each point with its (x, y) value
for i in range(len(x_values)):
    plt.annotate(f'({x_values[i]}, {y_values[i]})', # text to show
                 (x_values[i], y_values[i]),         # point to annotate
                 textcoords="offset points",         # how to position the text
                 xytext=(0,10),                      # distance from text to points (x,y)
                 ha='center')                        # horizontal alignment can be left, right or center

# Set the labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('X vs Y with values')

# Show the plot
plt.show()


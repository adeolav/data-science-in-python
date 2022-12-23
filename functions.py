# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv("ransom.csv")
# Display DataFrame
print(r)

# Plot a graph
plt.plot(x_values, y_values)

# Display the graph
plt.show()

# Use * to represent the missing four letters
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)

# Call lookup_plate() with the keyword argument for color
lookup_plate(plate, color="Green")

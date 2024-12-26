import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(csv_file, x_column, y_column, title):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_column], df[y_column], marker='o')
    
    # Customize the plot
    plt.title(title)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    
    # Save the plot
    output_file = f"{title.lower().replace(' ', '_')}.png"
    plt.savefig(output_file)
    print(f"Plot saved as {output_file}")

# Example usage
visualize_data("sales_data.csv", "Month", "Revenue", "Monthly Revenue")

import pandas as pd

def read_csv_to_table(file_path):
    """
    Reads a CSV file and outputs the data as a Pandas DataFrame.

    Parameters:
    - file_path: str, the path to the CSV file to read.

    Returns:
    - A Pandas DataFrame containing the data from the CSV file.
    """
    try:
        # Read the CSV file using Pandas
        df = pd.read_csv(file_path)
        
        # Return the DataFrame
        return df
    except Exception as e:
        # If an error occurs, print the error
        print(f"Error reading the CSV file: {e}")

# Example usage:
# Assuming you have a CSV file named 'data.csv' in the same directory as this script.
file_path = 'emails.csv'
df = read_csv_to_table(file_path)
import pandas as pd

def df_to_styled_html(df, output_file):
    """
    Converts a DataFrame to an HTML file with CSS styling.

    Parameters:
    - df: Pandas DataFrame, the DataFrame to convert.
    - output_file: str, the path to the output HTML file.
    """
    # Convert the DataFrame to HTML
    html = df.to_html()

    # Define CSS styles for the table
    css_style = """
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
    """

    # Combine the CSS and HTML
    full_html = f"<!DOCTYPE html>\n<html>\n<head>\n{css_style}\n</head>\n<body>\n{html}\n</body>\n</html>"

    # Write the HTML to the specified file
    with open(output_file, "w") as file:
        file.write(full_html)

# Example usage:
# Assuming df is your DataFrame
df_to_styled_html(df, "output.html")



# print(df)

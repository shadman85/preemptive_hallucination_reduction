import pandas as pd
import re 
# Load the Excel file


# Load the CSV file
file_path = 'G:/visual hel/3_nli_scores2.csv'
df = pd.read_csv(file_path)

# Define keywords to include, and construct a regex pattern for whole words
include_keywords = ["What ","Which ","Where "]
# Create a regex pattern that matches any of the keywords as whole words
include_pattern = r'\b(' + '|'.join(include_keywords) + r')\b'

# Function to check if any include keywords are present as whole words in the text
def check_row(text):
    # Return True if any include keyword as a whole word is found, otherwise False
    if re.search(include_pattern, text.lower()):
        return True
    return False

# Filter rows to keep only those with the include keywords in the 'question' column
filtered_df = df[df['question'].apply(lambda x: check_row(str(x)))]

# Save the filtered rows to a new CSV file
output_path = 'G:/visual hel/extracted/what2.csv'
filtered_df.to_csv(output_path, index=False)  # Use to_csv() for saving to a CSV file

print("Filtered rows containing the keywords have been saved to:", output_path)



# file_path = 'G:/visual hel/3_nli_scores2.csv'
# df = pd.read_csv(file_path)

# # Define keywords to exclude, and construct a regex pattern for whole words
# # exclude_keywords = ["How "," how "," many "]
# exclude_keywords = ["What "," how "," many "]
# # Create a regex pattern that matches any of the keywords as whole words
# exclude_pattern = r'\b(' + '|'.join(exclude_keywords) + r')\b'

# # Function to check if any exclude keywords are present as whole words in the text
# def reverse_check_row(text):
#     # Return False if any exclude keyword as a whole word is found, otherwise True
#     if re.search(exclude_pattern, text.lower()):
#         return False
#     return True

# # Filter rows to keep only those without the exclude keywords in the 'question' column
# filtered_df = df[df['question'].apply(lambda x: reverse_check_row(str(x)))]


# # Save the filtered rows back to a new Excel file
# output_path = 'G:/visual hel/extracted/how_many.csv'
# filtered_df.to_csv(output_path, index=False)

# print("Filtered rows have been saved to:", output_path)


import os


# Function to read the API key from settings.txt
def read_api_key(filepath='settings'):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} was not found.")

    with open(filepath, 'r') as file:
        for line in file:
            if line.startswith('API_KEY='):
                return line.strip().split('=')[1]

    raise ValueError("API_KEY not found in the settings file.")


# Use the read_api_key function to retrieve the API key
api_key = read_api_key()

# Print the API key to verify (for testing purposes, you might want to remove this in production)
print(f"API Key: {api_key}")
API_KEY = api_key
modelList = ['google/palm-2-chat-bison-32k',"nothingiisreal/mn-celeste-12b"]
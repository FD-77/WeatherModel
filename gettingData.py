import kagglehub

# Download latest version
path = kagglehub.dataset_download("danbraswell/new-york-city-weather-18692022")

print("Path to dataset files:", path)

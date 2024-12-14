# metrics_config.py

# Metrics to Monitor
METRICS = {
    "carbon_levels": {
        "description": "CO2 and CH4 concentration in ppm",
        "units": "ppm",
        "data_source": "NASA Earth Exchange",
    },
    "temperature": {
        "description": "Global and regional temperature variations",
        "units": "Celsius",
        "data_source": "NOAA",
    },
    "ocean_acidity": {
        "description": "pH levels across oceans",
        "units": "pH",
        "data_source": "Copernicus",
    },
    "deforestation_rates": {
        "description": "Satellite imagery to track forest cover changes",
        "units": "%",
        "data_source": "Google Earth Engine",
    },
    "biodiversity_loss": {
        "description": "Species population tracking",
        "units": "counts",
        "data_source": "Conservation APIs",
    },
    "disaster_indicators": {
        "description": "Real-time disaster signals",
        "units": "varied",
        "data_source": "NOAA and custom sensors",
    },
}

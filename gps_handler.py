"""
LiRA (Light-weight Road Assessment) - GPS Handler
Developed by: Saketcharan Chauhan M & Abubakr Siddiq Mohammed
Description: Logic for integrating location data into road assessments.
"""

class GPSHandler:
    def __init__(self):
        self.current_lat = 0.0
        self.current_lon = 0.0

    def update_location(self, lat, lon):
        """
        Updates the internal coordinates.
        """
        self.current_lat = lat
        self.current_lon = lon

    def get_location_string(self):
        """
        Returns a formatted string of the current location.
        """
        if self.current_lat == 0.0 and self.current_lon == 0.0:
            return "Unknown Location"
        return f"{self.current_lat:.6f}, {self.current_lon:.6f}"

    def get_map_url(self):
        """
        Generates a Google Maps URL for the current location.
        """
        if self.current_lat == 0.0 and self.current_lon == 0.0:
            return "#"
        return f"https://www.google.com/maps?q={self.current_lat},{self.current_lon}"

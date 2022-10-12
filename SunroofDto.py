class SunroofDTO:
    def __init__(self):
        self.hoursOfUsableSunlightPerYear = None
        self.sqFeetAvailableForSolarPanels = None
        self.recommendedSolarInstallationSizeInKW = None
        self.recommendedSolarInstallationSizeInSqFt = None
        self.address = None
        self.lat = None
        self.long = None
        self.error = None

    def __str__(self):
        return str(self.__dict__)


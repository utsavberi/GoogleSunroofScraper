import threading
import csv

from Scraper import Scraper


def convertToIterable(result):
    res = []
    for dto in result:
        res.append([
            dto.address,
            dto.lat,
            dto.long,
            dto.hoursOfUsableSunlightPerYear,
            dto.sqFeetAvailableForSolarPanels,
            dto.recommendedSolarInstallationSizeInKW,
            dto.recommendedSolarInstallationSizeInSqFt
        ])
    return res


class ScraperThread(threading.Thread):
    def __init__(self, latLongs, filename):
        threading.Thread.__init__(self)
        self.latLongs = latLongs
        self.filename = filename

    def run(self):
        scrapper = Scraper()
        result = scrapper.scrapeByLatLongs(self.latLongs)
        f = open('output/' + self.filename, 'w')

        # create the csv writer
        writer = csv.writer(f)

        writer.writerow(["address",
            "lat",
            "long",
            "hoursOfUsableSunlightPerYear",
            "sqFeetAvailableForSolarPanels",
            "recommendedSolarInstallationSizeInKW",
            "recommendedSolarInstallationSizeInSqFt"])
        # write a row to the csv file
        writer.writerows(convertToIterable(result))

# GoogleSunroofScraper

Scraper for google project sunroof (https://sunroof.withgoogle.com/building/42.35852239999999/-71.0561664/#?f=buy)

Takes in input from the input directory which contains `<longitude,latitude,address>` and scrapes project sunroof with the latitudes longitudes provided in the file.

The results are then stored in the output directory in the following format:
`<address, lat, long, hoursOfUsableSunlightPerYear, sqFeetAvailableForSolarPanels, recommendedSolarInstallationSizeInKW, recommendedSolarInstallationSizeInSqFt>`

## Usage
1. Open the project and add the input file in the input folder
2. Open main.py and update the following constants:  
  a. NUMBER_OF_RECORDS_IN_FILE.  
  b. FILE_PATH.  
  c. MAX_THREAD_COUNT.  
3. Run main.py
4. Once the script completes running all output will be stored in the output folder

from SunroofDto import SunroofDTO

class PageToSunroofDtoTranslator:
    def translate(self, page, latLongAddress) -> SunroofDTO:
        result = SunroofDTO()

        try:
            ua = page.query_selector_all('.panel-facts li')
            result.hoursOfUsableSunlightPerYear = int(
            ua[0].query_selector('.panel-fact-text').inner_html().split("\n")[1].strip().replace(",", ""))
            result.sqFeetAvailableForSolarPanels = int(
            ua[1].query_selector('.panel-fact-text').inner_html().split("\n")[1].strip().replace(",", ""))

            result.recommendedSolarInstallationSizeInKW = float(
            page.query_selector('.recommended-size', strict=True).inner_text().split(" ")[0])
            result.recommendedSolarInstallationSizeInSqFt = float(
            page.query_selector('.recommended-size', strict=True).inner_text().split("\n")[1][1:-5].replace(",", ""))
            result.error = "NoError"
        except:
            try:
                result.error = page.query_selector('.notfound-card ').inner_text()
                # print("not found error")
            except:
                result.error = "maybe blocked"
                page.screenshot(path='errorScreenshots/'+str(latLongAddress[0])+str(latLongAddress[1])+"screenshot.png")
                print("maybe blocked")

        result.lat = latLongAddress[0]
        result.long = latLongAddress[1]
        result.address = latLongAddress[2]

        return result

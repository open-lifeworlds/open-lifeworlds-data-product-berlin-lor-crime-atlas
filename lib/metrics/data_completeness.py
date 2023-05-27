import json
import os
import unittest

file_path = os.path.realpath(__file__)
script_path = os.path.dirname(file_path)

data_path = os.path.join(script_path, "..", "..", "data")

key_figure_group = "berlin-lor-crime-atlas"

statistic_properties = [
    "offences",
    "robbery",
    "street_robbery_purse_snatching",
    "bodily_harm",
    "dangerous_and_grievous_bodily_harm",
    "deprivation_of_liberty_coercion_threat_stalking",
    "theft",
    "motor_vehicle_theft",
    "theft_from_motor_vehicle",
    "bicycle_theft",
    "residential_burglary",
    "fire_offences",
    "arson",
    "damage_to_property",
    "damage_to_property_by_graffiti",
    "narcotics_offences",
    "kieztaten"
]


class FilesTestCase(unittest.TestCase):
    pass


for year in [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]:
    for half_year in ["00"]:
        for lor_area_type in ["districts", "forecast-areas", "district-regions"]:
            file = os.path.join(data_path, f"{key_figure_group}-{year}-{half_year}",
                                f"{key_figure_group}-{year}-{half_year}-{lor_area_type}.geojson")
            setattr(
                FilesTestCase,
                f"test_{key_figure_group}_{year}_{half_year}_{lor_area_type}".replace('-', '_'),
                lambda self, file=file: self.assertTrue(os.path.exists(file))
            )


class PropertiesTestCase(unittest.TestCase):
    pass


for year in [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]:
    for half_year in ["00"]:
        for lor_area_type in ["districts", "forecast-areas", "district-regions"]:
            file = os.path.join(data_path, f"{key_figure_group}-{year}-{half_year}",
                                f"{key_figure_group}-{year}-{half_year}-{lor_area_type}.geojson")
            if os.path.exists(file):
                with open(file=file, mode="r", encoding="utf-8") as geojson_file:
                    geojson = json.load(geojson_file, strict=False)

                for feature in geojson["features"]:
                    feature_id = feature["properties"]["id"]
                    setattr(
                        PropertiesTestCase,
                        f"test_{key_figure_group}_{year}_{half_year}_{lor_area_type}_{feature_id}".replace('-', '_'),
                        lambda self, feature=feature: self.assertTrue(
                            all(property in feature["properties"] for property in statistic_properties))
                    )

if __name__ == '__main__':
    unittest.main()

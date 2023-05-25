import os

import pandas as pd

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def convert_data_to_csv(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(source_path)):

        # Make results path
        subdir = subdir.replace(f"{source_path}/", "")
        os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

        for file_name in sorted(files):
            source_file_path = os.path.join(source_path, subdir, file_name)
            convert_file_to_csv(source_path, source_file_path, clean=clean, quiet=quiet)


def convert_file_to_csv(source_path, source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    source_file_name = source_file_name.split(os.path.sep)[-1]

    # Determine engine
    if source_file_extension == ".xlsx":
        engine = "openpyxl"
    elif source_file_extension == ".xls":
        engine = None
    else:
        return

    sheets = ["Fallzahlen_2013", "Fallzahlen_2014", "Fallzahlen_2015", "Fallzahlen_2016", "Fallzahlen_2017",
              "Fallzahlen_2018", "Fallzahlen_2019", "Fallzahlen_2020", "Fallzahlen_2021", "Fallzahlen_2022"]

    # Iterate over sheets
    for sheet in sheets:
        try:
            skiprows = 5
            names = ["id", "name", "offences", "robbery", "street_robbery_purse_snatching",
                     "bodily_harm", "dangerous_and_grievous_bodily_harm",
                     "deprivation_of_liberty_coercion_threat_stalking",
                     "theft", "motor_vehicle_theft", "theft_from_motor_vehicle", "bicycle_theft",
                     "residential_burglary",
                     "fire_offences", "arson",
                     "damage_property", "damage_property_by_graffiti",
                     "narcotics_offences", "kieztaten"]
            drop_columns = ["name"]

            dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows,
                                      usecols=list(range(0, len(names))), names=names) \
                .drop(columns=drop_columns, errors="ignore") \
                .replace("Eso", 0) \
                .dropna() \
                .assign(id=lambda x: x["id"].astype(str).str.zfill(6))

            # Drop columns that represent the a complete district or the complete city
            dataframe = dataframe[~dataframe["id"].str.endswith("0000")]
            dataframe = dataframe[~dataframe["id"].str.startswith("9999")]



            year = sheet.split(sep="_")[1]
            half_year = "00"
            file_path_csv = os.path.join(source_path, f"{source_file_name}-{year}-{half_year}", f"{source_file_name}-{year}-{half_year}.csv")

            # Check if result needs to be generated
            if clean or not os.path.exists(file_path_csv):
                # Write csv file
                if dataframe.shape[0] > 0:
                    os.makedirs(os.path.join(source_path, f"{source_file_name}-{year}-{half_year}"), exist_ok=True)
                    dataframe.to_csv(file_path_csv, index=False)
                    if not quiet:
                        print(f"✓ Convert {os.path.basename(file_path_csv)}")
                else:
                    if not quiet:
                        print(dataframe.head())
                        print(f"✗️ Empty {os.path.basename(file_path_csv)}")
            elif not quiet:
                print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        except Exception as e:
            print(f"✗️ Exception: {str(e)}")

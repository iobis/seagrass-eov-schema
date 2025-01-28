import pandas as pd


def export_sheet(sheet_name, output_path):
    df = excel_data.parse(sheet_name)
    df.to_csv(output_path, index=False)
    print(f"Saved {sheet_name} to {output_path}")


xlsx_file = "spreadsheet/Duffy_supplemental_material_data_dictionary_schema_20250127.xlsx"
excel_data = pd.ExcelFile(xlsx_file)

export_sheet("Example Event", "data/event.csv")
export_sheet("Example Occurrence", "data/occurrence.csv")
export_sheet("Example Extended Measurement-or", "data/mof.csv")

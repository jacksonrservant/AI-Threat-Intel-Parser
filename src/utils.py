from openpyxl import Workbook

def export_iocs_to_excel(iocs_dict, filename="exported_iocs.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "IOCs"

    ws.append(["Type", "Value"])

    for ioc_type, values in iocs_dict.items():
        for val in set(values):
            ws.append([ioc_type, val])

    wb.save(filename)
    print(f"✅ Exported IOCs to {filename}")
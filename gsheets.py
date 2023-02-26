from gspread import service_account

SHEET = service_account('key.json').open_by_key('1epsjIw9fg0qwpfceiz99seXadFJCCqotUynx6uRfdVE')

def get_all(work_sheet_name):
    WKS_DIAS = SHEET.worksheet(work_sheet_name)
    return WKS_DIAS.get_all_records()

def get_hour(work_sheet_name):
    return get_all(work_sheet_name)[0]['Horário']
    


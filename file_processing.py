import json, csv, openpyxl

from dearpygui import dearpygui as dpg

import site_pool, site_processing


def load_site_from_json() -> None:
    def json_load(sender, app_data):
        file_path = app_data['file_path_name']

        with open(file_path) as file:
            sites: dict = json.load(file)

            for site_name in sites.keys():
                author    = sites[site_name]['AUTHOR']    if sites[site_name]['AUTHOR']    != '' else 'NONE'
                date      = sites[site_name]['DATE']      if sites[site_name]['DATE']      != '' else 'NONE'
                time      = sites[site_name]['TIME']      if sites[site_name]['TIME']      != '' else 'NONE'
                latitude  = sites[site_name]['LATITUDE']  if sites[site_name]['LATITUDE']  != '' else 'NONE'
                longitude = sites[site_name]['LONGITUDE'] if sites[site_name]['LONGITUDE'] != '' else 'NONE'
                length    = sites[site_name]['LENGTH']    if sites[site_name]['LENGTH']    != '' else 'NONE'
                width     = sites[site_name]['WIDTH']     if sites[site_name]['WIDTH']     != '' else 'NONE'
                species   = {}

                for i in range(1, 101):
                    species.update({i: {}})
                    species[i]['SPECIES'] = sites[site_name]['SPECIES'][str(i)]['SPECIES']
                    species[i]['TIER'] = sites[site_name]['SPECIES'][str(i)]['TIER']
                    species[i]['ABUNDANCE'] = sites[site_name]['SPECIES'][str(i)]['ABUNDANCE']

                site_pool.current_local_sites[f'{site_name}_[JSON]'] = {
                    'AUTHOR': author,
                    'DATE': date,
                    'TIME': time,
                    'LATITUDE': latitude,
                    'LONGITUDE': longitude,
                    'LENGTH': str(length),
                    'WIDTH': str(width),
                    'SPECIES': species                }
                site_pool.current_site_names.append(f'{site_name}_[JSON]')

        site_processing.update_sites_list()
        dpg.configure_item(item='choose_site_to_manage_combobox', default_value=f'{site_name}_[JSON]')
        site_processing.view_site()

    with dpg.file_dialog(width=700, height=400, default_path='sites', callback=json_load):
        dpg.add_file_extension('.json')


def save_as_json() -> None:
    if dpg.get_value(item='choose_site_to_manage_combobox'):
        site_name = dpg.get_value(item='choose_site_to_manage_combobox')

        author    = site_pool.current_local_sites[site_name]['AUTHOR']
        date      = site_pool.current_local_sites[site_name]['DATE']
        time      = site_pool.current_local_sites[site_name]['TIME']
        latitude  = site_pool.current_local_sites[site_name]['LATITUDE']
        longitude = site_pool.current_local_sites[site_name]['LONGITUDE']
        length    = site_pool.current_local_sites[site_name]['LENGTH']
        width     = site_pool.current_local_sites[site_name]['WIDTH']
        species   = {}

        for i in range(1, 101):
            species.update({str(i): {}})
            species[str(i)]['SPECIES']   = site_pool.current_local_sites[site_name]['SPECIES'][i]['SPECIES']
            species[str(i)]['TIER']      = site_pool.current_local_sites[site_name]['SPECIES'][i]['TIER']
            species[str(i)]['ABUNDANCE'] = site_pool.current_local_sites[site_name]['SPECIES'][i]['ABUNDANCE']

        site_data = {
            'AUTHOR': author,
            'DATE': date,
            'TIME': time,
            'LATITUDE': latitude,
            'LONGITUDE': longitude,
            'LENGTH': length,
            'WIDTH': width,
            'SPECIES': species}


        def json_save(sender, app_data):
            print(app_data)
            directory = app_data['file_path_name']
            print(directory)
            with open(f'{directory}\{site_name}.json', 'w') as file:
                json.dump({f'{site_name}': site_data}, file, indent=4)

        with dpg.file_dialog(width=700, height=400, default_path='sites', callback=json_save):
            pass
    else:
        with dpg.window(label='ERROR', popup=True, pos=dpg.get_mouse_pos()):
            dpg.add_text('ERROR!')
            dpg.add_text('No site is chosen.')


def load_from_csv() -> None:
    def csv_load(sender, app_data):
        file_path = app_data['file_path_name']
        print(app_data)

        site_name = ''
        site_data = {
            'AUTHOR': '',
            'DATE': '',
            'TIME': '',
            'LATITUDE': '',
            'LONGITUDE': '',
            'WIDTH': '',
            'LENGTH': '',
            'SPECIES': {}
        }

        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=';')

            row_no = 0
            for current_row in csv_reader:
                print(current_row)
                if row_no == 1:
                    site_name = current_row[0]
                    site_data['AUTHOR'] = current_row[1]
                    site_data['DATE'] = current_row[2]
                    site_data['TIME'] = current_row[3]
                if row_no == 3:
                    site_data['LATITUDE'] = current_row[0]
                    site_data['LONGITUDE'] = current_row[1]
                    site_data['LENGTH'] = current_row[2]
                    site_data['WIDTH'] = current_row[3]
                if row_no >= 5:
                    site_data['SPECIES'][int(current_row[0])] = {}
                    site_data['SPECIES'][int(current_row[0])]['SPECIES'] = current_row[1]
                    site_data['SPECIES'][int(current_row[0])]['TIER'] = current_row[2]
                    site_data['SPECIES'][int(current_row[0])]['ABUNDANCE'] = current_row[3]
                row_no += 1

            site_pool.current_local_sites[f'{site_name}_[CSV]'] = site_data
            site_pool.current_site_names.append(f'{site_name}_[CSV]')
            site_processing.update_sites_list()
            dpg.configure_item(item='choose_site_to_manage_combobox', default_value=f'{site_name}_[CSV]')
            site_processing.view_site()

    with dpg.file_dialog(width=700, height=400, default_path='sites', callback=csv_load):
        dpg.add_file_extension('.csv')


def save_as_csv() -> None:
    if dpg.get_value(item='choose_site_to_manage_combobox') != '':
        site_name = dpg.get_value(item='choose_site_to_manage_combobox')
        site_data = site_pool.current_local_sites[site_name]

        def csv_save(sender, app_data):
            path = app_data['file_path_name']

            with open(f'{path}\{site_name}.csv', 'x') as file:
                csv_writer = csv.writer(file, delimiter=';', lineterminator=';\n')

                csv_writer.writerow(['SITE_NAME',             'AUTHOR',               'DATE',              'TIME'])
                csv_writer.writerow([site_name,               site_data['AUTHOR'],    site_data['DATE'],   site_data['TIME']])
                csv_writer.writerow(['LATITUDE',              'LONGITUDE',            'LENGTH',            'WIDTH'])
                csv_writer.writerow([site_data['LATITUDE'],   site_data['LONGITUDE'], site_data['LENGTH'], site_data['WIDTH']])

                csv_writer.writerow(['SPECIES_ID', 'SPECIES', 'TIER', 'ABUNDANCE'])
                for i in range(1, 101):
                    species_id = i
                    species = site_data['SPECIES'][i]['SPECIES']
                    tier = site_data['SPECIES'][i]['TIER']
                    abundance = site_data['SPECIES'][i]['ABUNDANCE']
                    csv_writer.writerow([species_id, species, tier, abundance])



        with dpg.file_dialog(width=700, height=400, default_path='sites', callback=csv_save):
            pass
    else:
        with dpg.window(label='ERROR', popup=True, pos=dpg.get_mouse_pos()):
            dpg.add_text('ERROR!')
            dpg.add_text('No site is chosen.')


def load_from_xlsx() -> None:
    def xlsx_load(sender, app_data):
        filename = app_data['file_path_name']

        site_name = ''
        site_data = {
            'AUTHOR': '',
            'DATE': '',
            'TIME': '',
            'LATITUDE': '',
            'LONGITUDE': '',
            'WIDTH': '',
            'LENGTH': '',
            'SPECIES': {}
        }

        workbook = openpyxl.load_workbook(filename)
        current_sheet = workbook.active

        site_name      = current_sheet.cell(row=2, column=1).value
        site_data['AUTHOR']    = current_sheet.cell(row=2, column=2).value
        site_data['DATE']      = current_sheet.cell(row=2, column=3).value
        site_data['TIME']      = current_sheet.cell(row=2, column=4).value

        site_data['LATITUDE']  = current_sheet.cell(row=4, column=1).value
        site_data['LONGITUDE'] = current_sheet.cell(row=4, column=2).value
        site_data['LENGTH']    = current_sheet.cell(row=4, column=3).value
        site_data['WIDTH']     = current_sheet.cell(row=4, column=4).value

        for i in range(1, 101):
            site_data['SPECIES'][i] = {}
            site_data['SPECIES'][i]['SPECIES'] = current_sheet.cell(row=i+5, column=2).value if current_sheet.cell(row=i+5, column=2).value != None else ''
            site_data['SPECIES'][i]['TIER'] = current_sheet.cell(row=i+5, column=3).value if current_sheet.cell(row=i+5, column=3).value != None else ''
            site_data['SPECIES'][i]['ABUNDANCE'] = current_sheet.cell(row=i+5, column=4).value if current_sheet.cell(row=i+5, column=4).value != None else ''

        site_pool.current_local_sites[f'{site_name}_[XLSX]'] = site_data
        site_pool.current_site_names.append(f'{site_name}_[XLSX]')
        site_processing.update_sites_list()
        dpg.configure_item(item='choose_site_to_manage_combobox', default_value=f'{site_name}_[XLSX]')
        site_processing.view_site()

    with dpg.file_dialog(width=700, height=400, default_path='sites', callback=xlsx_load):
        dpg.add_file_extension('.xlsx')


def save_as_xlsx() -> None:
    if dpg.get_value(item='choose_site_to_manage_combobox') != '':
        def xlsx_save(sender, app_data):
            site_name = dpg.get_value(item='choose_site_to_manage_combobox')
            path = app_data['file_path_name']

            workbook = openpyxl.Workbook()
            current_sheet = workbook.active

            current_sheet.cell(row=1, column=1).value = 'SITE_NAME'
            current_sheet.cell(row=1, column=2).value = 'AUTHOR'
            current_sheet.cell(row=1, column=3).value = 'DATE'
            current_sheet.cell(row=1, column=4).value = 'TIME'

            current_sheet.cell(row=3, column=1).value = 'LATITUDE'
            current_sheet.cell(row=3, column=2).value = 'LONGITUDE'
            current_sheet.cell(row=3, column=3).value = 'LENGTH'
            current_sheet.cell(row=3, column=4).value = 'WIDTH'

            current_sheet.cell(row=2, column=1).value = site_name
            current_sheet.cell(row=2, column=2).value = site_pool.current_local_sites[site_name]['AUTHOR']
            current_sheet.cell(row=2, column=3).value = site_pool.current_local_sites[site_name]['DATE']
            current_sheet.cell(row=2, column=4).value = site_pool.current_local_sites[site_name]['TIME']

            current_sheet.cell(row=4, column=1).value = site_pool.current_local_sites[site_name]['LATITUDE']
            current_sheet.cell(row=4, column=2).value = site_pool.current_local_sites[site_name]['LONGITUDE']
            current_sheet.cell(row=4, column=3).value = site_pool.current_local_sites[site_name]['LENGTH']
            current_sheet.cell(row=4, column=4).value = site_pool.current_local_sites[site_name]['WIDTH']

            for i in range(1, 101):
                current_sheet.cell(row=i+5, column=1).value = i+5
                current_sheet.cell(row=i+5, column=2).value = site_pool.current_local_sites[site_name]['SPECIES'][i]['SPECIES']
                current_sheet.cell(row=i+5, column=3).value = site_pool.current_local_sites[site_name]['SPECIES'][i]['TIER']
                current_sheet.cell(row=i+5, column=4).value = site_pool.current_local_sites[site_name]['SPECIES'][i]['ABUNDANCE']

            workbook.save(filename=f'{path}\{site_name}.xlsx')

        with dpg.file_dialog(width=700, height=400, default_path='sites', callback=xlsx_save):
            pass
    else:
        with dpg.window(label='ERROR', popup=True, pos=dpg.get_mouse_pos()):
            dpg.add_text('ERROR!')
            dpg.add_text('No site is chosen.')
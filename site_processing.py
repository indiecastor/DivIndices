import site_pool, ecofunclib, dpg_utils
import dearpygui.dearpygui as dpg

def update_sites_list() -> None:
    dpg.configure_item(item='choose_site_to_manage_combobox', items=site_pool.current_site_names)
    dpg.configure_item(item='site_1_to_compare',              items=site_pool.current_site_names)
    dpg.configure_item(item='site_2_to_compare',              items=site_pool.current_site_names)
    dpg.configure_item(item='alfa_diversity_combobox',        items=site_pool.current_site_names)
    for site_name in site_pool.current_site_names:
        if site_name not in site_pool.gamma_shown_sites:
            dpg.add_selectable(parent='gamma_diversity_list', label=f'>> {site_name}', tag=f'{site_name}_site_selectable')
            site_pool.gamma_shown_sites.append(site_name)

def count_species(site_name) -> int:
    counter: int = 0
    for i in range(1, 101):
        if site_pool.current_local_sites[site_name]['SPECIES'][i]['SPECIES'] != '':
            counter+= 1
    return counter

def get_pc_species_list(site_name) -> dict:
    species_result = dict()
    for i in range(1, 101):
        current_species_name = site_pool.current_local_sites[site_name]['SPECIES'][i]['SPECIES']
        current_species_abundance = site_pool.current_local_sites[site_name]['SPECIES'][i]['ABUNDANCE']
        if current_species_name != '' and current_species_name not in species_result.keys():
            species_result[current_species_name] = ecofunclib.convert_drude_to_projective_covering(current_species_abundance)
    return species_result


def get_site_from_ast() -> None:
    if dpg.get_value(item='site_name_input') != '':
        name = dpg.get_value(item='site_name_input')
        author =     dpg.get_value(item='site_author_input')
        latitude =   dpg.get_value(item='site_latitude_input')
        longitude = dpg.get_value(item='site_longitude_input')
        date =       dpg.get_value(item='site_date_input')
        time =       dpg.get_value(item='site_time_input')
        length = dpg.get_value(item='site_length_input')
        width = dpg.get_value(item='site_width_input')

        species = dict()
        for i in range(1, 101):
            species.update({i: {}})
            species[i].update({'SPECIES': dpg.get_value(f'ast_{i}_1')})
            species[i].update({'TIER': dpg.get_value(f'ast_{i}_2')})
            species[i].update({'ABUNDANCE': dpg.get_value(f'ast_{i}_3')})

        site = {
            'AUTHOR': author,
            'LATITUDE': latitude,
            'LONGITUDE': longitude,
            'DATE': date,
            'TIME': time,
            'SPECIES': species,
            'LENGTH': length,
            'WIDTH': width
        }
        site_pool.current_local_sites[name] = site
        site_pool.current_site_names.append(name)
        update_sites_list()
        print(site)
    else:
        with dpg.window(label='ERROR', popup=True, pos=dpg.get_mouse_pos()):
            dpg.add_text('ERROR!')
            dpg.add_text('No site is chosen.')

def view_site() -> None:

    chosen_site_name = dpg.get_value(item='choose_site_to_manage_combobox')
    chosen_site_species = site_pool.current_local_sites[chosen_site_name]['SPECIES']

    chosen_site_author    = site_pool.current_local_sites[chosen_site_name]['AUTHOR']     if site_pool.current_local_sites[chosen_site_name]['AUTHOR']     != '' else 'NONE'
    chosen_site_date      = site_pool.current_local_sites[chosen_site_name]['DATE']       if site_pool.current_local_sites[chosen_site_name]['DATE']       != '' else 'NONE'
    chosen_site_time      = site_pool.current_local_sites[chosen_site_name]['TIME']       if site_pool.current_local_sites[chosen_site_name]['TIME']       != '' else 'NONE'
    chosen_site_latitude  = site_pool.current_local_sites[chosen_site_name]['LATITUDE']   if site_pool.current_local_sites[chosen_site_name]['LATITUDE']   != '' else 'None'
    chosen_site_longitude = site_pool.current_local_sites[chosen_site_name]['LONGITUDE']  if site_pool.current_local_sites[chosen_site_name]['LONGITUDE']  != '' else 'NONE'
    chosen_site_length    = site_pool.current_local_sites[chosen_site_name]['LENGTH']     if site_pool.current_local_sites[chosen_site_name]['LENGTH']     != '' else 'NONE'
    chosen_site_width     = site_pool.current_local_sites[chosen_site_name]['WIDTH']      if site_pool.current_local_sites[chosen_site_name]['WIDTH']      != '' else 'NONE'

    chosen_site_total_species = count_species(chosen_site_name)

    dpg.configure_item(item='site_name_mng', default_value=chosen_site_name, color=[52, 201, 235, 255])
    dpg.configure_item(item='site_author_mng', default_value=chosen_site_author, color=dpg_utils.parameters_color(chosen_site_author))
    dpg.configure_item(item='site_date_mng', default_value=chosen_site_date, color=dpg_utils.parameters_color(chosen_site_date))
    dpg.configure_item(item='site_time_mng', default_value=chosen_site_time, color=dpg_utils.parameters_color(chosen_site_time))
    dpg.configure_item(item='site_latitude_mng', default_value=chosen_site_latitude, color=dpg_utils.parameters_color(chosen_site_latitude))
    dpg.configure_item(item='site_longitude_mng', default_value=chosen_site_longitude, color=dpg_utils.parameters_color(chosen_site_longitude))
    dpg.configure_item(item='site_length_mng', default_value=chosen_site_length, color=dpg_utils.parameters_color(chosen_site_length))
    dpg.configure_item(item='site_width_mng', default_value=chosen_site_width, color=dpg_utils.parameters_color(chosen_site_width))
    dpg.configure_item(item='site_total_species_mng', default_value=chosen_site_total_species, color=[0, 225, 0, 225])


    species_id = 1
    for i in range(1, 101):
        dpg.configure_item(item=f'vst_{i}_{1}', default_value=site_pool.current_local_sites[chosen_site_name]["SPECIES"][species_id]['SPECIES'])
        dpg.configure_item(item=f'vst_{i}_{2}', default_value=site_pool.current_local_sites[chosen_site_name]["SPECIES"][species_id]['TIER'])
        dpg.configure_item(item=f'vst_{i}_{3}', default_value=site_pool.current_local_sites[chosen_site_name]["SPECIES"][species_id]['ABUNDANCE'])
        species_id += 1

def clear_site_input_table() -> None:
    dpg.configure_item(item='site_name_input', default_value='')
    dpg.configure_item(item='site_author_input', default_value='')
    dpg.configure_item(item='site_date_input', default_value='')
    dpg.configure_item(item='site_time_input', default_value='')
    dpg.configure_item(item='site_latitude_input', default_value='')
    dpg.configure_item(item='site_longitude_input', default_value='')

    for i in range(1, 101):
        for n in range(1, 4):
            dpg.configure_item(item=f'ast_{i}_{n}', default_value='')

def clear_site_management_table() -> None:
    dpg.configure_item(item='site_name_mng', default_value='')
    dpg.configure_item(item='site_author_mng', default_value='')
    dpg.configure_item(item='site_date_mng', default_value='')
    dpg.configure_item(item='site_time_mng', default_value='')
    dpg.configure_item(item='site_latitude_mng', default_value='')
    dpg.configure_item(item='site_longitude_mng', default_value='')
    dpg.configure_item(item='site_length_mng', default_value='')
    dpg.configure_item(item='site_width_mng', default_value='')
    dpg.configure_item(item='site_total_species_mng', default_value='')

    for i in range(1, 101):
        for n in range(1, 4):
            dpg.configure_item(item=f'vst_{i}_{n}', default_value='')

def delete_site() -> None:
    if dpg.get_value(item='choose_site_to_manage_combobox') != '':
        chosen_site_name = dpg.get_value(item='choose_site_to_manage_combobox')
        dpg.configure_item(item='choose_site_to_manage_combobox', default_value='')
        site_pool.current_local_sites.pop(chosen_site_name)
        site_pool.current_site_names.remove(chosen_site_name)
        clear_site_management_table()
        update_sites_list()
    else:
        with dpg.window(label='ERROR', popup=True, pos=dpg.get_mouse_pos()):
            dpg.add_text('ERROR!')
            dpg.add_text('No site is chosen.')

def get_site_species_list(chosen_site_name: str) -> list[str, ...]:
    species = []
    for i in range(1, 101):
        if site_pool.current_local_sites[chosen_site_name]['SPECIES'][i]['SPECIES'] != '':
            species.append(site_pool.current_local_sites[chosen_site_name]['SPECIES'][i]['SPECIES'])
    return set(species)

def get_sites_from_multidimensional_selectable() -> None:
    for site in site_pool.current_site_names:
        if dpg.get_value(item=f'{site}_site_selectable'):
            site_pool.multidimensional_indices_selected_sites.append(site)


def count_pairwise_average(index: str in ['Jakkard', 'Sorensen', 'Ochiai', 'Kulczinsky', 'Szymkiewicz-Simpson', 'Braun-Blanquet'], sites: list):
    counts_done = []
    counter: float = 0.0

    for site_x in sites:
        for site_y in sites:
            if (site_x == site_y) or (f'{site_x}&{site_y}' in counts_done) or (f'{site_y}&{site_x}' in counts_done):
                pass
            else:
                match index:
                    case 'Jakkard':             counter += ecofunclib.jakkard_index(get_site_species_list(site_x), get_site_species_list(site_y))
                    case 'Sorensen':            counter += ecofunclib.sorensen_index(get_site_species_list(site_x), get_site_species_list(site_y))
                    case 'Ochiai':              counter += ecofunclib.ochiai_index(get_site_species_list(site_x), get_site_species_list(site_y))
                    case 'Kulczinsky':          counter += ecofunclib.kulczinsky_index(get_site_species_list(site_x), get_site_species_list(site_y))
                    case 'Szymkiewicz-Simpson': counter += ecofunclib.szymkiewicz_simpson_index(get_site_species_list(site_x), get_site_species_list(site_y))
                    case 'Braun-Blanquet':      counter += ecofunclib.braun_blanquet_index(get_site_species_list(site_x), get_site_species_list(site_y))
                counts_done.append(f'{site_x}&{site_y}')
    return counter / len(counts_done)



def count_two_dimensional_indices():
    index = dpg.get_value(item='two_dimensional_index_to_compare_with')
    site_1_name = dpg.get_value(item='site_1_to_compare')
    site_2_name = dpg.get_value(item='site_2_to_compare')
    site_1_species = get_site_species_list(site_1_name)
    site_2_species = get_site_species_list(site_2_name)

    result = 0.0

    match index:
        case 'Jakkard':
            result = ecofunclib.jakkard_index(site_1_species, site_2_species)
        case 'Sorensen':
            result = ecofunclib.sorensen_index(site_1_species, site_2_species)
        case 'Ochiai':
            result = ecofunclib.ochiai_index(site_1_species, site_2_species)
        case 'Kulczinsky':
            result = ecofunclib.kulczinsky_index(site_1_species, site_2_species)
        case 'Szymkiewicz-Simpson':
            result = ecofunclib.szymkiewicz_simpson_index(site_1_species, site_2_species)
        case 'Braun-Blanquet':
            result = ecofunclib.braun_blanquet_index(first_species=site_1_species, second_species=site_2_species)

    dpg.configure_item(item='two_dimensional_index_result', default_value=str(result), color=[0, 225, 0, 225])

def accept_changes() -> None:
    site_name_old = dpg.get_value(item='choose_site_to_manage_combobox')
    site_name_new = dpg.get_value(item='edit_name_input')

    for i in range(1, 101):
        for n in range(1, 4):
            dpg.configure_item(item=f'vst_input_text_{i}_{n}', show=False)
            dpg.configure_item(item=f'vst_{i}_{n}', show=True, default_value=dpg.get_value(item=f'vst_input_text_{i}_{n}'))

    if site_name_new != site_name_old:
        site_pool.current_local_sites[site_name_new] = {}
        site_pool.current_local_sites[site_name_new]['AUTHOR'] = dpg.get_value(item='edit_author_input')
        site_pool.current_local_sites[site_name_new]['DATE'] = dpg.get_value(item='edit_date_input')
        site_pool.current_local_sites[site_name_new]['TIME'] = dpg.get_value(item='edit_time_input')
        site_pool.current_local_sites[site_name_new]['LATITUDE'] = dpg.get_value(item='edit_latitude_input')
        site_pool.current_local_sites[site_name_new]['LONGITUDE'] = dpg.get_value(item='edit_longitude_input')
        site_pool.current_local_sites[site_name_new]['LENGTH'] = dpg.get_value(item='edit_length_input')
        site_pool.current_local_sites[site_name_new]['WIDTH'] = dpg.get_value(item='edit_width_input')
        site_pool.current_local_sites[site_name_new]['SPECIES'] = {}

        for i in range(1, 101):
            site_pool.current_local_sites[site_name_new]['SPECIES'][i] = {}
            site_pool.current_local_sites[site_name_new]['SPECIES'][i]['SPECIES'] = dpg.get_value(item=f'vst_input_text_{i}_1')
            site_pool.current_local_sites[site_name_new]['SPECIES'][i]['TIER'] = dpg.get_value(item=f'vst_input_text_{i}_2')
            site_pool.current_local_sites[site_name_new]['SPECIES'][i]['ABUNDANCE'] = dpg.get_value(item=f'vst_input_text_{i}_3')

        del site_pool.current_local_sites[site_name_old]
        print(site_name_old in site_pool.current_local_sites.keys())
        site_pool.current_site_names.remove(site_name_old)
        site_pool.current_site_names.append(site_name_new)

        dpg.configure_item(item='choose_site_to_manage_combobox', default_value=site_name_new)
        update_sites_list()
        view_site()
    else:
        site_pool.current_local_sites[site_name_old]['AUTHOR'] = dpg.get_value(item='edit_author_input')
        site_pool.current_local_sites[site_name_old]['DATE'] = dpg.get_value(item='edit_date_input')
        site_pool.current_local_sites[site_name_old]['TIME'] = dpg.get_value(item='edit_time_input')
        site_pool.current_local_sites[site_name_old]['LATITUDE'] = dpg.get_value(item='edit_latitude_input')
        site_pool.current_local_sites[site_name_old]['LONGITUDE'] = dpg.get_value(item='edit_longitude_input')
        site_pool.current_local_sites[site_name_old]['LENGTH'] = dpg.get_value(item='edit_length_input')
        site_pool.current_local_sites[site_name_old]['WIDTH'] = dpg.get_value(item='edit_width_input')

        for i in range(1, 101):
            site_pool.current_local_sites[site_name_old]['SPECIES'][i]['SPECIES'] = dpg.get_value(item=f'vst_input_text_{i}_1')
            site_pool.current_local_sites[site_name_old]['SPECIES'][i]['TIER'] = dpg.get_value(item=f'vst_input_text_{i}_2')
            site_pool.current_local_sites[site_name_old]['SPECIES'][i]['ABUNDANCE'] = dpg.get_value(item=f'vst_input_text_{i}_3')

    dpg.configure_item(item='edit_name_input', show=False, default_value='')
    dpg.configure_item(item='edit_author_input', show=False, default_value='')
    dpg.configure_item(item='edit_date_input', show=False, default_value='')
    dpg.configure_item(item='edit_time_input', show=False, default_value='')
    dpg.configure_item(item='edit_latitude_input', show=False, default_value='')
    dpg.configure_item(item='edit_longitude_input', show=False, default_value='')
    dpg.configure_item(item='edit_length_input', show=False, default_value='')
    dpg.configure_item(item='edit_width_input', show=False, default_value='')

    dpg.configure_item(item='site_name_mng',      show=True, default_value=site_name_new)
    dpg.configure_item(item='site_author_mng',    show=True, default_value=site_pool.current_local_sites[site_name_new]['AUTHOR'])
    dpg.configure_item(item='site_date_mng',      show=True, default_value=site_pool.current_local_sites[site_name_new]['DATE'])
    dpg.configure_item(item='site_time_mng',      show=True, default_value=site_pool.current_local_sites[site_name_new]['TIME'])
    dpg.configure_item(item='site_latitude_mng',  show=True, default_value=site_pool.current_local_sites[site_name_new]['LATITUDE'])
    dpg.configure_item(item='site_longitude_mng', show=True, default_value=site_pool.current_local_sites[site_name_new]['LONGITUDE'])
    dpg.configure_item(item='site_length_mng',    show=True, default_value=site_pool.current_local_sites[site_name_new]['LENGTH'])
    dpg.configure_item(item='site_width_mng',     show=True, default_value=site_pool.current_local_sites[site_name_new]['WIDTH'])

    dpg.configure_item(item='accept_changes_button', show=False)
    dpg.configure_item(item='dismiss_changes_button', show=False)

    dpg.configure_item(item='site_total_species_mng', default_value=count_species(site_name_new))

    dpg.configure_item(item='choose_site_to_manage_combobox', default_value=site_name_new)
    update_sites_list()

def dismiss_changes() -> None:
    for i in range(1, 101):
        for n in range(1, 4):
            dpg.configure_item(item=f'vst_input_text_{i}_{n}', show=False, default_value='')
            dpg.configure_item(item=f'vst_{i}_{n}', show=True)

    dpg.configure_item(item='site_name_mng',      show=True)
    dpg.configure_item(item='site_author_mng',    show=True)
    dpg.configure_item(item='site_date_mng',      show=True)
    dpg.configure_item(item='site_time_mng',      show=True)
    dpg.configure_item(item='site_latitude_mng',  show=True)
    dpg.configure_item(item='site_longitude_mng', show=True)
    dpg.configure_item(item='site_length_mng',    show=True)
    dpg.configure_item(item='site_width_mng',     show=True)

    dpg.configure_item(item='edit_name_input',      default_value='',  show=False)
    dpg.configure_item(item='edit_author_input',    default_value='',  show=False)
    dpg.configure_item(item='edit_date_input',      default_value='',  show=False)
    dpg.configure_item(item='edit_time_input',      default_value='',  show=False)
    dpg.configure_item(item='edit_latitude_input',  default_value='',  show=False)
    dpg.configure_item(item='edit_longitude_input', default_value='',  show=False)
    dpg.configure_item(item='edit_length_input',    default_value='',  show=False)
    dpg.configure_item(item='edit_width_input',     default_value='',  show=False)

    dpg.configure_item(item='accept_changes_button', show=False)
    dpg.configure_item(item='dismiss_changes_button', show=False)


def edit_site() -> None:
    if dpg.get_value(item='choose_site_to_manage_combobox') != '':
        dpg.configure_item(item='accept_changes_button', show=True)
        dpg.configure_item(item='dismiss_changes_button', show=True)

        site_name_old = dpg.get_value(item='choose_site_to_manage_combobox')

        dpg.configure_item(item='site_name_mng',      show=False)
        dpg.configure_item(item='site_author_mng',    show=False)
        dpg.configure_item(item='site_date_mng',      show=False)
        dpg.configure_item(item='site_time_mng',      show=False)
        dpg.configure_item(item='site_latitude_mng',  show=False)
        dpg.configure_item(item='site_longitude_mng', show=False)
        dpg.configure_item(item='site_length_mng',    show=False)
        dpg.configure_item(item='site_width_mng',     show=False)

        dpg.configure_item(item='edit_name_input',      default_value=site_name_old, show=True)
        dpg.configure_item(item='edit_author_input',    default_value=site_pool.current_local_sites[site_name_old]['AUTHOR'],     show=True)
        dpg.configure_item(item='edit_date_input',      default_value=site_pool.current_local_sites[site_name_old]['DATE'],       show=True)
        dpg.configure_item(item='edit_time_input',      default_value=site_pool.current_local_sites[site_name_old]['TIME'],       show=True)
        dpg.configure_item(item='edit_latitude_input',  default_value=site_pool.current_local_sites[site_name_old]['LATITUDE'],   show=True)
        dpg.configure_item(item='edit_longitude_input', default_value=site_pool.current_local_sites[site_name_old]['LONGITUDE'],  show=True)
        dpg.configure_item(item='edit_length_input',    default_value=site_pool.current_local_sites[site_name_old]['LENGTH'],     show=True)
        dpg.configure_item(item='edit_width_input',     default_value=site_pool.current_local_sites[site_name_old]['WIDTH'],      show=True)

        for i in range(1, 101):
            for n in range(1, 4):
                dpg.configure_item(item=f'vst_{i}_{n}', show=False)
                dpg.configure_item(item=f'vst_input_text_{i}_{n}', show=True, default_value=dpg.get_value(item=f'vst_{i}_{n}'), width=dpg.get_item_width(item=f'vst_{0}_{n}'))
    else:
        with dpg.window(label='ERROR', popup=True, pos=dpg.get_mouse_pos()):
            dpg.add_text('ERROR!')
            dpg.add_text('No site is chosen.')
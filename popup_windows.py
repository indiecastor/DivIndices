import dearpygui.dearpygui as dpg

import dpg_utils
import ecofunclib
import site_pool
import site_processing


def create_alfa_diversity_window() -> None:
    """ Creates alfa diversity window. Counts Shannon-Weaver, Simpson and reversed Simpson indices."""
    with dpg.window(pos=(20, 20), autosize=True, label='Alfa-diversity'):
        site_name      = dpg.get_value(item='alfa_diversity_combobox')
        site_species = site_processing.get_pc_species_list(site_name)

        site_author    = site_pool.current_local_sites[site_name]['AUTHOR']    if site_pool.current_local_sites[site_name]['AUTHOR'] != '' else 'NONE'
        site_date      = site_pool.current_local_sites[site_name]['DATE']      if site_pool.current_local_sites[site_name]['DATE'] != '' else 'NONE'
        site_time      = site_pool.current_local_sites[site_name]['TIME']      if site_pool.current_local_sites[site_name]['TIME'] != '' else 'NONE'
        site_latitude  = site_pool.current_local_sites[site_name]['LATITUDE']  if site_pool.current_local_sites[site_name]['LATITUDE'] != '' else 'NONE'
        site_longitude = site_pool.current_local_sites[site_name]['LONGITUDE'] if site_pool.current_local_sites[site_name]['LONGITUDE'] != '' else 'NONE'


        shannon_weaver_index_value  = round(ecofunclib.shannon_weaver_index(site_processing.get_pc_species_list(site_name)), 4)
        simpson_index_value         = round(ecofunclib.simpson_index(site_processing.get_pc_species_list(site_name)), 4)
        inverse_simpson_index_value = round(ecofunclib.inverse_simpson_index(site_processing.get_pc_species_list(site_name)), 4)

        # Site info
        with dpg.group():
            with dpg.group(horizontal=True):
                dpg.add_text('Site name:')
                dpg.add_text(site_name, color=[52, 201, 235, 255])
            with dpg.group(horizontal=True):
                dpg.add_text('Author:')
                dpg.add_text(site_author, color=dpg_utils.parameters_color(site_author))
            with dpg.group(horizontal=True):
                dpg.add_text('Date:')
                dpg.add_text(site_date, color=dpg_utils.parameters_color(site_date))
            with dpg.group(horizontal=True):
                dpg.add_text('Time:')
                dpg.add_text(site_time, color=dpg_utils.parameters_color(site_time))
            with dpg.group(horizontal=True):
                dpg.add_text('Latitude:')
                dpg.add_text(site_latitude, color=dpg_utils.parameters_color(site_latitude))
            with dpg.group(horizontal=True):
                dpg.add_text('Longitude:')
                dpg.add_text(site_longitude, color=dpg_utils.parameters_color(site_longitude))
            with dpg.group(horizontal=True):
                dpg.add_text('Total species:')
                dpg.add_text(str(site_processing.count_species(site_name)), color=[52, 201, 235, 255])

        dpg.add_text()
        dpg.add_text('===== Alfa-diversity =====')
        with dpg.group():
            with dpg.group(horizontal=True):
                dpg.add_text('Shannon-Weaver index:')
                dpg.add_text(shannon_weaver_index_value, color=dpg_utils.shannon_weaver_index_color(shannon_weaver_index_value))
            with dpg.group(horizontal=True):
                dpg.add_text('Simpson index:')
                dpg.add_text(simpson_index_value, color=dpg_utils.index_0_to_1_color(simpson_index_value))
            with dpg.group(horizontal=True):
                dpg.add_text('Inverse Simpson index:')
                dpg.add_text(inverse_simpson_index_value, color=dpg_utils.inversed_simpson_index_color(inverse_simpson_index_value))


def create_beta_diversity_window():
    if dpg.get_value(item='site_1_to_compare') != '' and dpg.get_value(item='site_2_to_compare') != '':
        site_1_name = dpg.get_value(item='site_1_to_compare')
        site_2_name = dpg.get_value(item='site_2_to_compare')

        site_1_species = site_processing.get_site_species_list(site_1_name)
        site_2_species = site_processing.get_site_species_list(site_2_name)

        site_1_author    = site_pool.current_local_sites[site_1_name]['AUTHOR']     if site_pool.current_local_sites[site_1_name]['AUTHOR']    != '' else 'NONE'
        site_1_date      = site_pool.current_local_sites[site_1_name]['DATE']       if site_pool.current_local_sites[site_1_name]['DATE']      != '' else 'NONE'
        site_1_time      = site_pool.current_local_sites[site_1_name]['TIME']       if site_pool.current_local_sites[site_1_name]['TIME']      != '' else 'NONE'
        site_1_latitude  = site_pool.current_local_sites[site_1_name]['LATITUDE']   if site_pool.current_local_sites[site_1_name]['LATITUDE']  != '' else 'NONE'
        site_1_longitude = site_pool.current_local_sites[site_1_name]['LONGITUDE']  if site_pool.current_local_sites[site_1_name]['LONGITUDE'] != '' else 'NONE'

        site_2_author    = site_pool.current_local_sites[site_2_name]['AUTHOR']     if site_pool.current_local_sites[site_2_name]['AUTHOR']    != '' else 'NONE'
        site_2_date      = site_pool.current_local_sites[site_2_name]['DATE']       if site_pool.current_local_sites[site_2_name]['DATE']      != '' else 'NONE'
        site_2_time      = site_pool.current_local_sites[site_2_name]['TIME']       if site_pool.current_local_sites[site_2_name]['TIME']      != '' else 'NONE'
        site_2_latitude  = site_pool.current_local_sites[site_2_name]['LATITUDE']   if site_pool.current_local_sites[site_2_name]['LATITUDE']  != '' else 'NONE'
        site_2_longitude = site_pool.current_local_sites[site_2_name]['LONGITUDE']  if site_pool.current_local_sites[site_2_name]['LONGITUDE'] != '' else 'NONE'

        jakkard_index_value             = round(ecofunclib.jakkard_index(            site_1_species, site_2_species), 4)
        sorensen_index_value            = round(ecofunclib.sorensen_index(           site_1_species, site_2_species), 4)
        ochiai_index_value              = round(ecofunclib.ochiai_index(             site_1_species, site_2_species), 4)
        kulczinsky_index_value          = round(ecofunclib.kulczinsky_index(         site_1_species, site_2_species), 4)
        szymkiewicz_simpson_index_value = round(ecofunclib.szymkiewicz_simpson_index(site_1_species, site_2_species), 4)
        braun_blanquet_index_value      = round(ecofunclib.braun_blanquet_index(     site_1_species, site_2_species), 4)

        with dpg.window(pos=(20, 20), width=600, height=400, label='Two-dimensional comparison'):
            # Sites info
            with dpg.group(horizontal=True):
                with dpg.group():
                    dpg.add_text('===== First site =====')
                    with dpg.group(horizontal=True):
                        dpg.add_text('Site name:')
                        dpg.add_text(site_1_name, color=[52, 201, 235, 255])
                    with dpg.group(horizontal=True):
                        dpg.add_text('Author:')
                        dpg.add_text(site_1_author, color=dpg_utils.parameters_color(site_1_author))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Date:')
                        dpg.add_text(site_1_date, color=dpg_utils.parameters_color(site_1_date))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Time:')
                        dpg.add_text(site_1_time, color=dpg_utils.parameters_color(site_1_time))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Latitude:')
                        dpg.add_text(site_1_latitude, color=dpg_utils.parameters_color(site_1_latitude))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Longitude:')
                        dpg.add_text(site_1_longitude, color=dpg_utils.parameters_color(site_1_longitude))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Total species:')
                        dpg.add_text(str(site_processing.count_species(site_1_name)), color=[52, 201, 235, 255])

                with dpg.group():
                    dpg.add_text('===== Second site =====')
                    with dpg.group(horizontal=True):
                        dpg.add_text('Site name:')
                        dpg.add_text(site_2_name, color=[52, 201, 235, 255])
                    with dpg.group(horizontal=True):
                        dpg.add_text('Author:')
                        dpg.add_text(site_2_author, color=dpg_utils.parameters_color(site_2_author))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Date:')
                        dpg.add_text(site_2_date, color=dpg_utils.parameters_color(site_2_date))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Time:')
                        dpg.add_text(site_2_time, color=dpg_utils.parameters_color(site_2_time))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Latitude:')
                        dpg.add_text(site_2_latitude, color=dpg_utils.parameters_color(site_2_latitude))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Longitude:')
                        dpg.add_text(site_2_longitude, color=dpg_utils.parameters_color(site_2_longitude))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Total species:')
                        dpg.add_text(str(site_processing.count_species(site_2_name)), color=[52, 201, 235, 255])

            # Comparison results
            dpg.add_text()
            with dpg.group():
                dpg.add_text('===== Comparison results =====')
                with dpg.group(horizontal=True):
                    dpg.add_text('Jakakrd index:')
                    dpg.add_text(jakkard_index_value, color=dpg_utils.index_0_to_1_color(jakkard_index_value))
                with dpg.group(horizontal=True):
                    dpg.add_text('Sorensen index:')
                    dpg.add_text(sorensen_index_value,
                                 color=dpg_utils.index_0_to_1_color(sorensen_index_value))
                with dpg.group(horizontal=True):
                    dpg.add_text('Ochiai index:')
                    dpg.add_text(ochiai_index_value, color=dpg_utils.index_0_to_1_color(ochiai_index_value))
                with dpg.group(horizontal=True):
                    dpg.add_text('Kulczinsky index:')
                    dpg.add_text(kulczinsky_index_value,
                                 color=dpg_utils.index_0_to_1_color(kulczinsky_index_value))
                with dpg.group(horizontal=True):
                    dpg.add_text('Szymkiewicz-Simpson index:')
                    dpg.add_text(szymkiewicz_simpson_index_value,
                                 color=dpg_utils.index_0_to_1_color(szymkiewicz_simpson_index_value))
                with dpg.group(horizontal=True):
                    dpg.add_text('Braun-Blanquet index:')
                    dpg.add_text(braun_blanquet_index_value,
                                 color=dpg_utils.index_0_to_1_color(braun_blanquet_index_value))

def create_gamma_diversity_window():
    with dpg.window(width=600, height=600, pos=(20, 20), label='Multidimensional comparison', autosize=True, on_close=site_pool.multidimensional_indices_selected_sites.clear()):

        site_processing.get_sites_from_multidimensional_selectable()
        site_names = site_pool.multidimensional_indices_selected_sites.copy()

        species = []
        for site in site_pool.multidimensional_indices_selected_sites:
            species.append(site_processing.get_site_species_list(site))


        jakkard_index_result              = round(site_processing.count_pairwise_average(sites=site_names, index='Jakkard'), 4)
        sorensen_index_result             = round(site_processing.count_pairwise_average(sites=site_names, index='Sorensen'), 4)
        ochiai_index_result               = round(site_processing.count_pairwise_average(sites=site_names, index='Ochiai'), 4)
        kulczinsky_index_result           = round(site_processing.count_pairwise_average(sites=site_names, index='Kulczinsky'), 4)
        szymkiewicz_simpson_index_result  = round(site_processing.count_pairwise_average(sites=site_names, index='Szymkiewicz-Simpson'), 4)
        braun_blanquet_index_result       = round(site_processing.count_pairwise_average(sites=site_names, index='Braun-Blanquet'), 4)

        beta_whittaker_measure_value     = round(ecofunclib.beta_whittaker_measure(species), 4)

        with dpg.group(horizontal=True):
            for site in site_names:
                with dpg.group():
                    dpg.add_text(f'===== {site} =====')
                    with dpg.group(horizontal=True):
                        dpg.add_text('Site name:')
                        dpg.add_text(site, color=[52, 201, 235, 255])
                    with dpg.group(horizontal=True):
                        dpg.add_text('Author:')
                        dpg.add_text(site_pool.current_local_sites[site]['AUTHOR'] if site_pool.current_local_sites[site]['AUTHOR'] != '' else 'NONE', color=dpg_utils.parameters_color(site_pool.current_local_sites[site]['AUTHOR']))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Date:')
                        dpg.add_text(site_pool.current_local_sites[site]['DATE'] if site_pool.current_local_sites[site]['DATE'] != '' else 'NONE', color=dpg_utils.parameters_color(site_pool.current_local_sites[site]['DATE']))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Time:')
                        dpg.add_text(site_pool.current_local_sites[site]['TIME'] if site_pool.current_local_sites[site]['TIME'] != '' else 'NONE', color=dpg_utils.parameters_color(site_pool.current_local_sites[site]['TIME']))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Latitude:')
                        dpg.add_text(site_pool.current_local_sites[site]['LATITUDE'] if site_pool.current_local_sites[site]['LATITUDE'] != '' else 'NONE', color=dpg_utils.parameters_color(site_pool.current_local_sites[site]['LATITUDE']))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Longitude:')
                        dpg.add_text(site_pool.current_local_sites[site]['LONGITUDE'] if site_pool.current_local_sites[site]['LONGITUDE'] != '' else 'NONE', color=dpg_utils.parameters_color(site_pool.current_local_sites[site]['LONGITUDE']))
                    with dpg.group(horizontal=True):
                        dpg.add_text('Total species:')
                        dpg.add_text(str(site_processing.count_species(site)), color=[52, 201, 235, 255])
        dpg.add_text()
        dpg.add_text('========== Comparison results ===================================================================================')
        dpg.add_text('Pairwise average')
        with dpg.group(horizontal=True):
            with dpg.group():
                dpg.add_text('Jakkard:')
                dpg.add_text(jakkard_index_result, color=dpg_utils.index_0_to_1_color(jakkard_index_result))
            with dpg.group():
                dpg.add_text('Sorensen:')
                dpg.add_text(sorensen_index_result, color=dpg_utils.index_0_to_1_color(sorensen_index_result))
            with dpg.group():
                dpg.add_text('Ochiai:')
                dpg.add_text(ochiai_index_result, color=dpg_utils.index_0_to_1_color(ochiai_index_result))
            with dpg.group():
                dpg.add_text('Kulczinsky:')
                dpg.add_text(kulczinsky_index_result, color=dpg_utils.index_0_to_1_color(kulczinsky_index_result))
            with dpg.group():
                dpg.add_text('Szymkiewicz-Simpson:')
                dpg.add_text(szymkiewicz_simpson_index_result, color=dpg_utils.index_0_to_1_color(szymkiewicz_simpson_index_result))
            with dpg.group():
                dpg.add_text('Braun-Blanquet:')
                dpg.add_text(braun_blanquet_index_result, color=dpg_utils.index_0_to_1_color(braun_blanquet_index_result))

        with dpg.group(horizontal=True):
            dpg.add_text("Whittaker's beta-diversity measure:")
            dpg.add_text(beta_whittaker_measure_value)
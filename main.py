import dearpygui.dearpygui as dpg
import CONSTANTS, site_pool, popup_windows, site_processing, tooltips
import file_processing


def main():
    dpg.create_context()

    big_let_start = 0x00C0  # Capital "A" in cyrillic alphabet
    big_let_end = 0x00DF  # Capital "Я" in cyrillic alphabet
    small_let_end = 0x00FF  # small "я" in cyrillic alphabet
    remap_big_let = 0x0410  # Starting number for remapped cyrillic alphabet
    alph_len = big_let_end - big_let_start + 1  # adds the shift from big letters to small
    alph_shift = remap_big_let - big_let_start  # adds the shift from remapped to non-remapped
    with dpg.font_registry():
        with dpg.font("fonts/SegoeUI.ttf", 18) as default_font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
            biglet = remap_big_let  # Starting number for remapped cyrillic alphabet
            for i1 in range(big_let_start, big_let_end + 1):  # Cycle through big letters in cyrillic alphabet
                dpg.add_char_remap(i1, biglet)  # Remap the big cyrillic letter
                dpg.add_char_remap(i1 + alph_len, biglet + alph_len)  # Remap the small cyrillic letter
                biglet += 1  # choose next letter
            dpg.bind_font(default_font)

    dpg.create_viewport(title='DivIndices', width=1100, height=800, resizable=False, x_pos=20, y_pos=20, small_icon='images\icon.ico', large_icon='images\icon.ico')
    with dpg.window(tag="Primary Window"):

        dpg.add_text(CONSTANTS.INTRO, wrap=400)
        with dpg.collapsing_header(label=CONSTANTS.ADD_SITE_HEADER, default_open=True, tag='add_plot_collapsing_header'):
            dpg.add_text('Here you can add trial sites!')

            # Plot data
            with dpg.group(horizontal=True):
                with dpg.group(horizontal=True):
                    with dpg.group():
                        dpg.add_input_text(tag='site_name_input',       width=300, hint=CONSTANTS.TRIAL_SITE_NAME_HINT)
                        dpg.add_input_text(tag='site_author_input',     width=300, hint=CONSTANTS.TRIAL_SITE_AUTHOR_HINT)
                        dpg.add_input_text(tag='site_latitude_input',   width=300, hint=CONSTANTS.TRIAL_SITE_LATITUDE_HINT)
                        dpg.add_input_text(tag='site_longitude_input', width=300, hint=CONSTANTS.TRIAL_SITE_LONGITUDE_HINT)
                    with dpg.group():
                        dpg.add_input_text(tag='site_date_input',       width=300, hint=CONSTANTS.TRIAL_SITE_DATE_HINT)
                        dpg.add_input_text(tag='site_time_input',       width=300, hint=CONSTANTS.TRIAL_SITE_TIME_HINT)
                        dpg.add_input_text(tag='site_length_input',     width=300, hint=CONSTANTS.TRIAL_SITE_LENGTH_HINT)
                        dpg.add_input_text(tag='site_width_input',      width=300, hint=CONSTANTS.TRIAL_SITE_WIDTH_HINT)


            # Site addition table
            with dpg.table(tag='add_site_tab', width=1000, height=200, no_pad_innerX=True,
                                     borders_outerV=False, borders_innerV=True,
                                     borders_outerH=True, borders_innerH=True, scrollY=True, no_clip=True):
                dpg.add_table_column(parent='add_site_tab', tag='ast_0_0', label='ID', width=20, width_fixed=True)
                dpg.add_table_column(parent='add_site_tab', tag='ast_0_1', label='SPECIES', width=820, width_fixed=True)
                dpg.add_table_column(parent='add_site_tab', tag='ast_0_2', label='TIER', width=50, width_fixed=True)
                dpg.add_table_column(parent='add_site_tab', tag='ast_0_3', label='ABUNDANCE', width=100, width_fixed=True)
            for i in range(1, 101):
                with dpg.table_row(parent='add_site_tab'):
                    dpg.add_text(str(i))
                    for n in range(1, 4):
                        dpg.add_input_text(tag=f'ast_{i}_{n}', width=dpg.get_item_width(item=f'ast_0_{n}'))

            with dpg.group(horizontal=True, height=35):
                dpg.add_button(label='ADD SITE', width=186, callback=site_processing.get_site_from_ast)
                dpg.add_button(width=200, label='CLEAR ALL', callback=site_processing.clear_site_input_table)

        with dpg.collapsing_header(label=CONSTANTS.MANAGE_SITES_HEADER, default_open=True):

            dpg.add_combo(width=308, tag='choose_site_to_manage_combobox', items=site_pool.current_site_names, callback=site_processing.view_site, label=' Choose site')

            with dpg.group(horizontal=True, height=35):
                dpg.add_button(label='Edit',             width=150, callback=site_processing.edit_site, tag='edit_site_button')
                dpg.add_button(label='Delete',           width=150, callback=site_processing.delete_site)
            with dpg.group(horizontal=True, height=35):
                dpg.add_button(label='Save as .json', tag='save_as_json_button', width=150, callback=file_processing.save_as_json)
                dpg.add_button(label='Save as .csv', width=150, callback=file_processing.save_as_csv)
                dpg.add_button(label='Save as .xlsx', width=150, callback=file_processing.save_as_xlsx)
            with dpg.group(horizontal=True, height=35):
                dpg.add_button(width=150, label='Load from .json', tag='load_from_json_button', callback=file_processing.load_site_from_json)
                with dpg.tooltip(parent='load_from_json_button', delay=0.5):
                    dpg.add_text('Correct .json file format:')
                    dpg.add_text(CONSTANTS.CORRECT_JSON_FORMAT_HINT)
                dpg.add_button(width=150, label='Load from .csv', tag='load_from_csv_button', callback=file_processing.load_from_csv)
                with dpg.tooltip(parent='load_from_csv_button', delay=0.5):
                    dpg.add_text('Correct .csv file format:')
                    dpg.add_text(CONSTANTS.CORRECT_CSV_FORMAT_HINT)
                dpg.add_button(width=150, label='Load from .xlsx', tag='load_from_xlsx_button', callback=file_processing.load_from_xlsx)
                with dpg.tooltip(parent='load_from_xlsx_button', delay=0.5):
                    width, height, channels, data = dpg.load_image(r"images\xlsx_load_hint.png")
                    with dpg.texture_registry():
                        dpg.add_static_texture(width=width, height=height, default_value=data, tag="xlsx_load_hint")
                    dpg.add_text('Correct .xlsx file format:')
                    dpg.add_image('xlsx_load_hint')

            # Site data
            with dpg.group(horizontal=True):
                with dpg.group():
                    with dpg.group(horizontal=True, tag='name_mng_gr'):
                        dpg.add_text('Site name:')
                        dpg.add_text(tag='site_name_mng')
                    with dpg.group(horizontal=True, tag='author_mng_gr'):
                        dpg.add_text('Author:')
                        dpg.add_text(tag='site_author_mng')
                    with dpg.group(horizontal=True, tag='date_mng_gr'):
                        dpg.add_text('Date:')
                        dpg.add_text(tag='site_date_mng')
                    with dpg.group(horizontal=True, tag='time_mng_gr'):
                        dpg.add_text('Time:')
                        dpg.add_text(tag='site_time_mng')
                    with dpg.group(horizontal=True, tag='latitude_mng_gr'):
                        dpg.add_text('Latitude:')
                        dpg.add_text(tag='site_latitude_mng')
                    with dpg.group(horizontal=True, tag='longitude_mng_gr'):
                        dpg.add_text('Longitude:')
                        dpg.add_text(tag='site_longitude_mng')
                with dpg.group():
                    with dpg.group(horizontal=True, tag='length_mng_gr'):
                        dpg.add_text('Length:')
                        dpg.add_text(tag='site_length_mng')
                    with dpg.group(horizontal=True, tag='width_mng_gr'):
                        dpg.add_text('Width:')
                        dpg.add_text(tag='site_width_mng')
                    with dpg.group(horizontal=True):
                        dpg.add_text('Total species:')
                        dpg.add_text(tag='site_total_species_mng')
                    with dpg.group(horizontal=True):
                        dpg.add_button(label='Accept', tag='accept_changes_button', width=150, height=30, show=False, callback=site_processing.accept_changes)
                        dpg.add_button(label='Dismiss', tag='dismiss_changes_button', width=150, height=30, show=False, callback=site_processing.dismiss_changes)

            # Hidden input_texts for editing
            dpg.add_input_text(parent='name_mng_gr',      tag='edit_name_input',     width=250, show=False)
            dpg.add_input_text(parent='author_mng_gr',    tag='edit_author_input',   width=250, show=False)
            dpg.add_input_text(parent='date_mng_gr',      tag='edit_date_input',     width=250, show=False)
            dpg.add_input_text(parent='time_mng_gr',      tag='edit_time_input',     width=250, show=False)
            dpg.add_input_text(parent='latitude_mng_gr',  tag='edit_latitude_input', width=250, show=False)
            dpg.add_input_text(parent='longitude_mng_gr', tag='edit_longitude_input',width=250, show=False)
            dpg.add_input_text(parent='length_mng_gr',    tag='edit_length_input',   width=250, show=False)
            dpg.add_input_text(parent='width_mng_gr',     tag='edit_width_input',    width=250, show=False)


            with dpg.table(tag='view_site_table', width=777, height=200, no_clip=True, scrollY=True,
                               borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True) as view_table:
                dpg.add_table_column(parent='view_site_table', tag='vst_0_0', label='ID', width=38, width_fixed=True)
                dpg.add_table_column(parent='view_site_table', tag='vst_0_1',label='SPECIES')
                dpg.add_table_column(parent='view_site_table', tag='vst_0_2',label='LAYER', width=200, width_fixed=True)
                dpg.add_table_column(parent='view_site_table', tag='vst_0_3',label='ABUNDANCE', width=70, width_fixed=True)
                for i in range(1, 101):
                    with dpg.table_row(parent='view_site_table', height=20):
                        dpg.add_text(str(i))
                        for n in range(1, 4):
                            with dpg.group(tag=f'gr_vst_{i}_{n}'):
                                dpg.add_text(tag=f'vst_{i}_{n}')
                                dpg.add_input_text(tag=f'vst_input_text_{i}_{n}', show=False)



        with dpg.collapsing_header(label=CONSTANTS.COMPARE_SITES_HEADER, default_open=True):

            dpg.add_text('==== One-dimensional indices ====')
            with dpg.group(horizontal=True):
                dpg.add_text('Choose site:')
                dpg.add_combo(tag='alfa_diversity_combobox', items=site_pool.current_site_names, width=300)
                dpg.add_button(label='View!', callback=popup_windows.create_alfa_diversity_window)

            dpg.add_text('==== Two-dimensional indices ====')
            with dpg.group(horizontal=True):
                with dpg.group():
                    with dpg.group(horizontal=True):
                        dpg.add_text('Choose site 1:')
                        dpg.add_combo(tag='site_1_to_compare', width=300, items=site_pool.current_site_names)
                    with dpg.group(horizontal=True):
                        dpg.add_text('Choose site 2:')
                        dpg.add_combo(tag='site_2_to_compare', width=300, items=site_pool.current_site_names)
                with dpg.group(horizontal=True):
                    with dpg.group():
                        dpg.add_button(label='Compare!', tag='two_dimensional_comparison_button', height=42, width=150, callback=popup_windows.create_beta_diversity_window)
            dpg.add_text('==== Multidimensional indices ====')
            with dpg.group(horizontal=True):
                with dpg.group(width=406):
                    dpg.add_text('Choose multiple sites:')
                    with dpg.group(tag='gamma_diversity_list'):
                        for site in site_pool.current_site_names:
                            if site not in site_pool.gamma_shown_sites:
                                dpg.add_selectable(label=f'>> {site}', tag=f'{site}_site_selectable', width=400)
                                site_pool.gamma_shown_sites.append(site)
                with dpg.group(horizontal=True):
                    with dpg.group():
                        dpg.add_button(label='Compare!', height=42, width=150, callback=popup_windows.create_gamma_diversity_window)


    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == '__main__':
    main()
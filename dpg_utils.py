def index_0_to_1_color(index_value):
    if index_value <= 0.25:
        return [255, 0, 0, 255]
    elif index_value <= 0.50:
        return [255, 125, 0, 255]
    elif index_value <= 0.75:
        return [255, 255, 0, 255]
    elif index_value <= 1:
        return [0, 255, 0, 255]

def parameters_color(parameter):
    if parameter == '' or parameter == 'NONE' or parameter == 'None' or parameter == None:
        return [255, 0, 0, 255]
    else:
        return [0, 255, 0, 255]

def shannon_weaver_index_color(index_value):
    if index_value <= 1:
        return [255, 0, 0, 255]
    elif index_value <= 2:
        return [255, 125, 0, 255]
    elif index_value < 3:
        return [255, 255, 0, 255]
    elif index_value >= 3:
        return [0, 255, 0, 255]


def inversed_simpson_index_color(index_value):
    if index_value <= 2:
        return [255, 0, 0, 255]
    elif index_value <= 3:
        return [255, 125, 0, 255]
    elif index_value < 4.5:
        return [255, 255, 0, 255]
    elif index_value >= 4.5:
        return [0, 255, 0, 255]

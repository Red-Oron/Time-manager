from time import timezone
from variable_constants import ACTIVITIES

PLOT_WIDTH, PLOT_START_WIDTH, PLOT_WIDTH_STEP = 9, 3.5, 0.45
PLOT_HEIGTH, PLOT_START_HEIGTH, PLOT_HEIGTH_STEP = 5.7, 2.2, 0.25
UTC_OFFSET, LABELS_IN_ROW, DAYS_OF_WEEK = -timezone, len(ACTIVITIES), ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
FULL, EXCLUDE_VOIDS = False, False
s, m, h = 1, 60, 3600

INTRO = """Hello! This program is created to count similarity measures in envoronmental science and doing some other stuff! Both english and cyrillic letters are allowed, but english ones are preferable as well as latin species names. \n
Developer:
    vk.com/oi_ko
    t.me/castroiko
"""
TRIAL_SITE_HELP = 'Note: Site name and contents are required, and location, date, time, author et.c. are optional. Also only species name are required and everything else is optional.'

TRIAL_SITE_NAME_HINT      = 'Trial site name e.g. Kazan, plot #17'
TRIAL_SITE_AUTHOR_HINT    = 'Author e.g. Piper Castor'
TRIAL_SITE_LATITUDE_HINT  = 'Latitude e.g. 55.833190'
TRIAL_SITE_LONGITUDE_HINT = 'Longitude e.g. 48.835341'
TRIAL_SITE_DATE_HINT      = 'Date e.g. 28.06.2024'
TRIAL_SITE_TIME_HINT      = 'Time e.g. 19:48'
TRIAL_SITE_LENGTH_HINT    = 'Length in meters'
TRIAL_SITE_WIDTH_HINT     = 'Width in meters'

TWO_DIMENSIONAL_INDICES = ['Jakkard', 'Sorensen', 'Ochiai', 'Kulczinsky', 'Szymkiewicz-Simpson', 'Braun-Blanquet']

ADD_SITE_HEADER      = '================================================== ADD PLOTS ================================================================================='
MANAGE_SITES_HEADER  = '================================================= MANAGE PLOTS =============================================================================='
COMPARE_SITES_HEADER = '================================================ COMPARE PLOTS ================================================================================'

CORRECT_JSON_FORMAT_HINT = """{
  "TEST_JSON": {
    "AUTHOR": "Piper Castor",
    "LATITUDE": "55.834694",
    "LONGITUDE": "48.832726",
    "DATE": "11.07.2024",
    "TIME": "11:13",
    "LENGTH": "20",
    "WIDTH": "20",
    "SPECIES": {
      "1": {
        "SPECIES": "Aegopodium podagraria",
        "TIER": "D",
        "ABUNDANCE": "cop2"
      },
      "2": {
        "SPECIES": "Matteuccia struthioptheris",
        "TIER": "D",
        "ABUNDANCE": "cop1"
      },
      "3": {
        "SPECIES": "Pinus sylvestris",
        "TIER": "A",
        "ABUNDANCE": "cop2"
      }..."""
CORRECT_CSV_FORMAT_HINT = """SITE_NAME;AUTHOR;DATE;TIME;
Zaymische 1;Tarasov V. I., Sharich V. D., Vertikova Y. E.;06.07.2024;11:09;
LATITUDE;LONGITUDE;LENGTH;WIDTH;
55.844899;48.804209;20;20;
SPECIES_ID;SPECIES;TIER;ABUNDANCE;
1;Aegopodium podagraria;C;cop3;
2;Equisetum sylvaticum;C;sol;
3;Asarum europaeum;C;sp;
4;Aconitum axcelsium;C;sol;
5;Mercurialis perrenis;C;sol;
6;Padus avium;C;sol;
7;Carex pilosa;C;sp;
8;Ranunculus cassubicus;C;sol;
9;Geum urbanum;C;sol;
10;...;...;...;"""
import time
import pygame
import sys
from os import environ
from pygame.locals import *

pygame.init()
pygame.display.set_caption(' ')
BLANC = (219, 227, 230)
NOIR = (0, 0, 0)
w = 1272
c = w / 19
La = int(c * 18 + 0.5)
l = int(c * 11 + 0.5)
data1 = {
    0  : ['H', 'Hydrogène', '1.00794', 1, 1, 'Autres Non-Métaux'],
    1  : ['He', 'Hélium', '4.002602', 18, 1, 'Gaz Nobles'],
    2  : ['Li', 'Lithium', '6.941', 1, 2, 'Métaux Alcalins'],
    3  : ['Be', 'Béryllium', '9.012182', 2, 2, 'Méteaux alcalino-terreux'],
    4  : ['B', 'Bore', '10.811', 13, 2, 'Métaloïdes', ],
    5  : ['C', 'Carbone', '12.0107', 14, 2, 'Autres Non-Métaux'],
    6  : ['N', 'Azote', '14.0067', 15, 2, 'Autres Non-Métaux'],
    7  : ['O', 'Oxygène', '15.9994', 16, 2, 'Autres Non-Métaux'],
    8  : ['F', 'Fluor', '18.9984032', 17, 2, 'Autres Non-Métaux'],
    9  : ['Ne', 'Néon', '20.1797', 18, 2, 'Gaz Nobles'],
    10 : ['Na', 'Sodium', '22.98976', 1, 3, 'Métaux Alcalins'],
    11 : ['Mg', 'Magnésium', '24.305', 2, 3, 'Méteaux alcalino-terreux'],
    12 : ['Al', 'Aluminium', '26.9815386', 13, 3, 'Métaux Pauvres'],
    13 : ['Si', 'Silicon', '28.0855', 14, 3, 'Métaloïdes'],
    14 : ['P', 'Phosphore', '30.973762', 15, 3, 'Autres Non-Métaux'],
    15 : ['S', 'Soufre', '32.065', 16, 3, 'Autres Non-Métaux'],
    16 : ['Cl', 'Chlore', '35.453', 17, 3, 'Autres Non-Métaux'],
    17 : ['Ar', 'Argon', '39.948', 18, 3, 'Gaz Nobles'],
    18 : ['K', 'Potassium', '39.948', 1, 4, 'Métaux Alcalins'],
    19 : ['Ca', 'Calcium', '40.078', 2, 4, 'Méteaux alcalino-terreux'],
    20 : ['Sc', 'Scandium', '44.955912', 3, 4, 'Métaux de transition'],
    21 : ['Ti', 'Titanium', '47.867', 4, 4, 'Métaux de transition'],
    22 : ['V', 'Vanadium', '50.9415', 5, 4, 'Métaux de transition'],
    23 : ['Cr', 'Chrome', '51.9961', 6, 4, 'Métaux de transition'],
    24 : ['Mn', 'Manganèse', '54.938045', 7, 4, 'Métaux de transition'],
    25 : ['Fe', 'Fer', '55.845', 8, 4, 'Métaux de transition'],
    26 : ['Co', 'Cobalt', '58.933195', 9, 4, 'Métaux de transition'],
    27 : ['Ni', 'Nickel', '58.6934', 10, 4, 'Métaux de transition'],
    28 : ['Cu', 'Cuivre', '63.546', 11, 4, 'Métaux de transition'],
    29 : ['Zn', 'Zinc', '65.38', 12, 4, 'Métaux de transition'],
    30 : ['Ga', 'Gallium', '69.723', 13, 4, 'Métaux Pauvres'],
    31 : ['Ge', 'Germanium', '72.63', 14, 4, 'Métaloïdes'],
    32 : ['As', 'Arsenic', '74.9216', 15, 4, 'Métaloïdes'],
    33 : ['Se', 'Sélénium', '78.96', 16, 4, 'Autres Non-Métaux'],
    34 : ['Br', 'Brome', '79.904', 17, 4, 'Autres Non-Métaux'],
    35 : ['Kr', 'Krypton', '83.798', 18, 4, 'Gaz Nobles'],
    36 : ['Rb', 'Rubidium', '85.4678', 1, 5, 'Métaux Alcalins'],
    37 : ['Sr', 'Strontium', '87.62', 2, 5, 'Méteaux alcalino-terreux'],
    38 : ['Y', 'Yttrium', '88.90585', 3, 5, 'Métaux de transition'],
    39 : ['Zr', 'Zirconium', '91.224', 4, 5, 'Métaux de transition'],
    40 : ['Nb', 'Niobium', '92.90628', 5, 5, 'Métaux de transition'],
    41 : ['Mo', 'Molybdène', '95.96', 6, 5, 'Métaux de transition'],
    42 : ['Tc', 'Technétium', '(98)', 7, 5, 'Métaux de transition'],
    43 : ['Ru', 'Ruthénium', '101.07', 8, 5, 'Métaux de transition'],
    44 : ['Rh', 'Rhodium', '102.9055', 9, 5, 'Métaux de transition'],
    45 : ['Pd', 'Palladium', '106.42', 10, 5, 'Métaux de transition'],
    46 : ['Ag', 'Argent', '107.8682', 11, 5, 'Métaux de transition'],
    47 : ['Cd', 'Cadmium', '112.411', 12, 5, 'Métaux de transition'],
    48 : ['In', 'Indium', '114.818', 13, 5, 'Métaux Pauvres'],
    49 : ['Sn', 'Étain', '118.71', 14, 5, 'Métaux Pauvres'],
    50 : ['Sb', 'Antimoine', '121.76', 15, 5, 'Métaloïdes'],
    51 : ['Te', 'Tellure', '127.6', 16, 5, 'Métaloïdes'],
    52 : ['I', 'Iode', '126.90447', 17, 5, 'Autres Non-Métaux'],
    53 : ['Xe', 'Xenon', '131.293', 18, 5, 'Gaz Nobles'],
    54 : ['Cs', 'Cesium', '132.9054', 1, 6, 'Métaux Alcalins'],
    55 : ['Ba', 'Barium', '132.9054', 2, 6, 'Méteaux alcalino-terreux'],
    56 : ['La', 'Lanthane', '138.90547', 4, 9, 'Lanthanides'],
    57 : ['Ce', 'Cérium', '140.116', 5, 9, 'Lanthanides'],
    58 : ['Pr', 'Praséodyme', '140.90765', 6, 9, 'Lanthanides'],
    59 : ['Nd', 'Néodyme', '144.242', 7, 9, 'Lanthanides'],
    60 : ['Pm', 'Prométhium', '(145)', 8, 9, 'Lanthanides'],
    61 : ['Sm', 'Samarium', '150.36', 9, 9, 'Lanthanides'],
    62 : ['Eu', 'Europium', '151.964', 10, 9, 'Lanthanides'],
    63 : ['Gd', 'Gadolinium', '157.25', 11, 9, 'Lanthanides'],
    64 : ['Tb', 'Terbium', '158.92535', 12, 9, 'Lanthanides'],
    65 : ['Dy', 'Dysprosium', '162.5', 13, 9, 'Lanthanides'],
    66 : ['Ho', 'Holmium', '164.93032', 14, 9, 'Lanthanides'],
    67 : ['Er', 'Erbium', '167.259', 15, 9, 'Lanthanides'],
    68 : ['Tm', 'Thulium', '168.93421', 16, 9, 'Lanthanides'],
    69 : ['Yb', 'Ytterbium', '173.054', 17, 9, 'Lanthanides'],
    70 : ['Lu', 'Lutétium', '174.9668', 18, 9, 'Lanthanides'],
    71 : ['Hf', 'Hafnium', '178.49', 4, 6, 'Métaux de transition'],
    72 : ['Ta', 'Tantale', '180.94788', 5, 6, 'Métaux de transition'],
    73 : ['W', 'Tungstène', '183.84', 6, 6, 'Métaux de transition'],
    74 : ['Re', 'Rhénium', '186.207', 7, 6, 'Métaux de transition'],
    75 : ['Os', 'Osmium', '190.23', 8, 6, 'Métaux de transition'],
    76 : ['Ir', 'Iridium', '192.217', 9, 6, 'Métaux de transition'],
    77 : ['Pt', 'Platine', '195.084', 10, 6, 'Métaux de transition'],
    78 : ['Au', 'Or', '196.966569', 11, 6, 'Métaux de transition'],
    79 : ['Hg', 'Mercure', '200.59', 12, 6, 'Métaux de transition'],
    80 : ['Tl', 'Thallium', '204.3833', 13, 6, 'Métaux Pauvres'],
    81 : ['Pb', 'Plomb', '207.2', 14, 6, 'Métaux Pauvres'],
    82 : ['Bi', 'Bismuth', '208.9804', 15, 6, 'Métaux Pauvres'],
    83 : ['Po', 'Polonium', '(209)', 16, 6, 'Métaux Pauvres'],
    84 : ['At', 'Astate', '(210)', 17, 6, 'Métaloïdes'],
    85 : ['Rn', 'Radon', '(222)', 18, 6, 'Gaz Nobles'],
    86 : ['Fr', 'Francium', '(223)', 1, 7, 'Métaux Alcalins'],
    87 : ['Ra', 'Radium', '(226)', 2, 7, 'Méteaux alcalino-terreux'],
    88 : ['Ac', 'Actinium', '(227)', 4, 10, 'Actinides'],
    89 : ['Th', 'Thorium', '232.03806', 5, 10, 'Actinides'],
    90 : ['Pa', 'Protactinium', '231.0588', 6, 10, 'Actinides'],
    91 : ['U', 'Uranium', '238.02891', 7, 10, 'Actinides'],
    92 : ['Np', 'Neptunium', '(237)', 8, 10, 'Actinides'],
    93 : ['Pu', 'Plutonium', '(244)', 9, 10, 'Actinides'],
    94 : ['Am', 'Americium', '(243)', 10, 10, 'Actinides'],
    95 : ['Cm', 'Curium', '(247)', 11, 10, 'Actinides'],
    96 : ['Bk', 'Berkélium', '(247)', 12, 10, 'Actinides'],
    97 : ['Cf', 'Californium', '(251)', 13, 10, 'Actinides'],
    98 : ['Es', 'Einstenium', '(252)', 14, 10, 'Actinides'],
    99 : ['Fm', 'Fermium', '(257)', 15, 10, 'Actinides'],
    100: ['Md', 'Mendelévium', '(258)', 16, 10, 'Actinides'],
    101: ['No', 'Nobélium', '(259)', 17, 10, 'Actinides'],
    102: ['Lr', 'Lawrencium', '(262)', 18, 10, 'Actinides'],
    103: ['Rf', 'Rutherfordium', '(267)', 4, 7, 'Métaux de transition'],
    104: ['Db', 'Dubnium', '(268)', 5, 7, 'Métaux de transition'],
    105: ['Sg', 'Seaborgium', '(271)', 6, 7, 'Métaux de transition'],
    106: ['Bh', 'Bohrium', '(272)', 7, 7, 'Métaux de transition'],
    107: ['Hs', 'Hassium', '(270)', 8, 7, 'Métaux de transition'],
    108: ['Mt', 'Meitnerium', '(276)', 9, 7, 'Inconnus'],
    109: ['Ds', 'Darmstadium', '(281)', 10, 7, 'Inconnus'],
    110: ['Rg', 'Roentgénium', '(280)', 11, 7, 'Inconnus'],
    111: ['Cn', 'Copernicium', '(285)', 12, 7, 'Métaux de transition'],
    112: ['Nh', 'Nihomium', '(284)', 13, 7, 'Inconnus'],
    113: ['Fl', 'Flerovium', '(289)', 14, 7, 'Inconnus'],
    114: ['Mc', 'Moscovium', '(288)', 15, 7, 'Inconnus'],
    115: ['Lv', 'Livermorium', '(293)', 16, 7, 'Inconnus'],
    116: ['Ts', 'Tennesine', '(294)', 17, 7, 'Inconnus'],
    117: ['Og', 'Oganesson', '(294)', 18, 7, 'Inconnus'],
}
data2 = {
    0  : ["1s¹", 1],
    1  : ["1s²", 2],
    2  : ["[He] 2s¹", (2, 1)],
    3  : ["[He] 2s²", (2, 2)],
    4  : ["[He] 2s² 2p¹", (2, 3)],
    5  : ["[He] 2s² 2p²", (2, 4)],
    6  : ["[He] 2s² 2p³", (2, 5)],
    7  : ["[He] 2s² 2p⁴", (2, 6)],
    8  : ["[He] 2s² 2p⁵", (2, 7)],
    9  : ["[He] 2s² 2p⁶", (2, 8)],
    10 : ["[Ne] 3s¹", (2, 8, 1)],
    11 : ["[Ne] 3s²", (2, 8, 2)],
    12 : ["[Ne] 3s² 3p¹", (2, 8, 3)],
    13 : ["[Ne] 3s² 3p²", (2, 8, 4)],
    14 : ["[Ne] 3s² 3p³", (2, 8, 5)],
    15 : ["[Ne] 3s² 3p⁴", (2, 8, 6)],
    16 : ["[Ne] 3s² 3p⁵", (2, 8, 7)],
    17 : ["[Ne] 3s² 3p⁶", (2, 8, 8)],
    18 : ["[Ar] 4s¹", (2, 8, 8, 1)],
    19 : ["[Ar] 4s²", (2, 8, 8, 2)],
    20 : ["[Ar] 4s² 3d¹", (2, 8, 9, 2)],
    21 : ["[Ar] 4s² 3d²", (2, 8, 10, 2)],
    22 : ["[Ar] 4s² 3d³", (2, 8, 11, 2)],
    23 : ["[Ar] 4s¹ 3d⁵", (2, 8, 12, 2)],
    24 : ["[Ar] 4s² 3d⁵", (2, 8, 13, 2)],
    25 : ["[Ar] 4s² 3d⁶", (2, 8, 14, 2)],
    26 : ["[Ar] 4s² 3d⁷", (2, 8, 15, 2)],
    27 : ["[Ar] 4s² 3d⁸", (2, 8, 16, 2)],
    28 : ["[Ar] 4s¹ 3d¹⁰", (2, 8, 18, 1)],
    29 : ["[Ar] 4s² 3d¹⁰", (2, 8, 18, 2)],
    30 : ["[Ar] 4s² 3d¹⁰ 4p¹", (2, 8, 18, 3)],
    31 : ["[Ar] 4s² 3d¹⁰ 4p²", (2, 8, 18, 4)],
    32 : ["[Ar] 4s² 3d¹⁰ 4p³", (2, 8, 18, 5)],
    33 : ["[Ar] 4s² 3d¹⁰ 4p⁴", (2, 8, 18, 6)],
    34 : ["[Ar] 4s² 3d¹⁰ 4p⁵", (2, 8, 18, 7)],
    35 : ["[Ar] 4s² 3d¹⁰ 4p⁶", (2, 8, 18, 8)],
    36 : ["[Kr] 5s¹", (2, 8, 18, 8, 1)],
    37 : ["[Kr] 5s²", (2, 8, 18, 8, 2)],
    38 : ["[Kr] 5s² 4d¹", (2, 8, 18, 9, 2)],
    39 : ["[Kr] 5s² 4d²", (2, 8, 18, 10, 2)],
    40 : ["[Kr] 5s¹ 4d⁴", (2, 8, 18, 12, 1)],
    41 : ["[Kr] 5s¹ 4d⁵", (2, 8, 18, 13, 1)],
    42 : ["[Kr] 5s² 4d⁵", (2, 8, 18, 13, 2)],
    43 : ["[Kr] 5s¹ 4d⁷", (2, 8, 18, 15, 1)],
    44 : ["[Kr] 5s¹ 4d⁸", (2, 8, 18, 16, 1)],
    45 : ["[Kr] 4d¹⁰", (2, 8, 18, 18)],
    46 : ["[Kr] 5s¹ 4d¹⁰", (2, 8, 18, 18, 1)],
    47 : ["[Kr] 5s² 4d¹⁰", (2, 8, 18, 18, 2)],
    48 : ["[Kr] 5s² 4d¹⁰ 5p¹", (2, 8, 18, 18, 3)],
    49 : ["[Kr] 5s² 4d¹⁰ 5p²", (2, 8, 18, 18, 4)],
    50 : ["[Kr] 5s² 4d¹⁰ 5p³", (2, 8, 18, 18, 5)],
    51 : ["[Kr] 5s² 4d¹⁰ 5p⁴", (2, 8, 18, 18, 6)],
    52 : ["[Kr] 5s² 4d¹⁰ 5p⁵", (2, 8, 18, 18, 7)],
    53 : ["[Kr] 5s² 4d¹⁰ 5p⁶", (2, 8, 18, 18, 8)],
    54 : ["[Xe] 6s¹", (2, 8, 18, 18, 8, 1)],
    55 : ["[Xe] 6s²", (2, 8, 18, 18, 8, 2)],
    56 : ["[Xe] 6s² 5d¹", (2, 8, 18, 18, 9, 2)],
    57 : ["[Xe] 6s² 4f¹ 5d¹", (2, 8, 18, 19, 9, 1)],
    58 : ["[Xe] 6s² 4f³", (2, 8, 18, 21, 8, 2)],
    59 : ["[Xe] 6s² 4f⁴", (2, 8, 18, 22, 8, 2)],
    60 : ["[Xe] 6s² 4f⁵", (2, 8, 18, 23, 8, 2)],
    61 : ["[Xe] 6s² 4f⁶", (2, 8, 18, 24, 8, 2)],
    62 : ["[Xe] 6s² 4f⁷", (2, 8, 18, 25, 8, 2)],
    63 : ["[Xe] 6s² 4f⁷ 5d¹", (2, 8, 18, 25, 9, 2)],
    64 : ["[Xe] 6s² 4f⁹", (2, 8, 18, 27, 8, 2)],
    65 : ["[Xe] 6s² 4f¹⁰", (2, 8, 18, 28, 8, 2)],
    66 : ["[Xe] 6s² 4f¹¹", (2, 8, 18, 29, 8, 2)],
    67 : ["[Xe] 6s² 4f¹²", (2, 8, 18, 30, 8, 2)],
    68 : ["[Xe] 6s² 4f¹³", (2, 8, 18, 31, 8, 2)],
    69 : ["[Xe] 6s² 4f¹⁴", (2, 8, 18, 32, 8, 2)],
    70 : ["[Xe] 6s² 4f¹⁴ 5d¹", (2, 8, 18, 32, 9, 2)],
    71 : ["[Xe] 6s² 4f¹⁴ 5d²", (2, 8, 18, 32, 10, 2)],
    72 : ["[Xe] 6s² 4f¹⁴ 5d³", (2, 8, 18, 32, 11, 2)],
    73 : ["[Xe] 6s² 4f¹⁴ 5d⁴", (2, 8, 18, 32, 12, 2)],
    74 : ["[Xe] 6s² 4f¹⁴ 5d⁵", (2, 8, 18, 32, 13, 2)],
    75 : ["[Xe] 6s² 4f¹⁴ 5d⁶", (2, 8, 18, 32, 14, 2)],
    76 : ["[Xe] 6s² 4f¹⁴ 5d⁷", (2, 8, 18, 32, 15, 2)],
    77 : ["[Xe] 6s¹ 4f¹⁴ 5d⁹", (2, 8, 18, 32, 17, 1)],
    78 : ["[Xe] 6s¹ 4f¹⁴ 5d¹⁰", (2, 8, 18, 32, 18, 1)],
    79 : ["[Xe] 6s² 4f¹⁴ 5d¹⁰", (2, 8, 18, 32, 18, 2)],
    80 : ["[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p¹", (2, 8, 18, 32, 18, 3)],
    81 : ["[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p²", (2, 8, 18, 32, 18, 4)],
    82 : ["[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p³", (2, 8, 18, 32, 18, 5)],
    83 : ["[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁴", (2, 8, 18, 32, 18, 6)],
    84 : ["[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁵", (2, 8, 18, 32, 18, 7)],
    85 : ["[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁶", (2, 8, 18, 32, 18, 8)],
    86 : ["[Rn] 7s¹", (2, 8, 18, 32, 18, 8, 1)],
    87 : ["[Rn] 7s²", (2, 8, 18, 32, 18, 8, 2)],
    88 : ["[Rn] 7s² 6d¹", (2, 8, 18, 32, 18, 9, 2)],
    89 : ["[Rn] 7s² 6d²", (2, 8, 18, 32, 18, 10, 2)],
    90 : ["[Rn] 7s² 5f² 6d¹", (2, 8, 18, 32, 20, 9, 2)],
    91 : ["[Rn] 7s² 5f³ 6d¹", (2, 8, 18, 32, 21, 9, 2)],
    92 : ["[Rn] 7s² 5f⁴ 6d¹", (2, 8, 18, 32, 22, 9, 2)],
    93 : ["[Rn] 7s² 5f⁶", (2, 8, 18, 32, 24, 8, 2)],
    94 : ["[Rn] 7s² 5f⁷", (2, 8, 18, 32, 25, 8, 2)],
    95 : ["[Rn] 7s² 5f⁷ 6d¹", (2, 8, 18, 32, 25, 9, 2)],
    96 : ["[Rn] 7s² 5f⁹", (2, 8, 18, 32, 27, 8, 2)],
    97 : ["[Rn] 7s² 5f¹⁰", (2, 8, 18, 32, 28, 8, 2)],
    98 : ["[Rn] 7s² 5f¹¹", (2, 8, 18, 32, 29, 8, 2)],
    99 : ["[Rn] 7s² 5f¹²", (2, 8, 18, 32, 30, 8, 2)],
    100: ["[Rn] 7s² 5f¹³", (2, 8, 18, 32, 31, 8, 2)],
    101: ["[Rn] 7s² 5f¹⁴", (2, 8, 18, 32, 32, 8, 2)],
    102: ["[Rn] 7s² 5f¹⁴ 7p¹", (2, 8, 18, 32, 32, 8, 3)],
    103: ["[Rn] 7s² 5f¹⁴ 6d²", (2, 8, 18, 32, 32, 10, 2)],
    104: ["[Rn] 7s² 5f¹⁴ 6d³", (2, 8, 18, 32, 32, 11, 2)],
    105: ["[Rn] 7s² 5f¹⁴ 6d⁴", (2, 8, 18, 32, 32, 12, 2)],
    106: ["[Rn] 7s² 5f¹⁴ 6d⁵", (2, 8, 18, 32, 32, 13, 2)],
    107: ["[Rn] 7s² 5f¹⁴ 6d⁶", (2, 8, 18, 32, 32, 14, 2)],
    108: ["[Rn] 7s² 5f¹⁴ 6d⁷", (2, 8, 18, 32, 32, 15, 2)],
    109: ["[Rn] 7s² 5f¹⁴ 6d⁸", (2, 8, 18, 32, 32, 16, 2)],
    110: ["[Rn] 7s² 5f¹⁴ 6d⁹", (2, 8, 18, 32, 32, 17, 2)],
    111: ["[Rn] 7s² 5f¹⁴ 6d¹⁰", (2, 8, 18, 32, 32, 18, 2)],
    112: ["[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p¹", (2, 8, 18, 32, 32, 18, 3)],
    113: ["[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p²", (2, 8, 18, 32, 32, 18, 4)],
    114: ["[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p³", (2, 8, 18, 32, 32, 18, 5)],
    115: ["[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁴", (2, 8, 18, 32, 32, 18, 6)],
    116: ["[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁵", (2, 8, 18, 32, 32, 18, 7)],
    117: ["[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁶", (2, 8, 18, 32, 32, 18, 8)],
}
color = {
    'Métaux Alcalins'         : (229, 116, 188),
    'Méteaux alcalino-terreux': (235, 150, 210),
    'Métaux de transition'    : (249, 180, 237),
    'Métaux Pauvres'          : (234, 186, 246),
    'Métaloïdes'              : (220, 179, 255),
    'Autres Non-Métaux'       : (215, 191, 255),
    'Gaz Nobles'              : (196, 199, 255),
    'Lanthanides'             : (173, 207, 255),
    'Actinides'               : (150, 215, 255),
    'Inconnus'                : (200, 175, 255)
}
WINDOW = pygame.display.set_mode([La, l])
surface = pygame.display.get_surface()
rectangles = list()
TRANSPARENT = pygame.Surface((La, l))
TRANSPARENT.set_alpha(255)
TRANSPARENT.fill(BLANC)
magni = pygame.draw.rect(TRANSPARENT, BLANC, (0, 0, 0, 0), 0)
current = magni
window_size_x, window_size_y = 860, 860
a = pygame.image.load('icon.png')
pygame.display.set_icon(a)
exit = magni


def create():
    surface.fill(BLANC)
    k = 56
    h = 88

    for j in range(0, 11):
        for i in range(0, 18):
            if j == 9 and (i > 2):
                rectangles.insert(k, draw_case(i, j))
                k += 1
            elif j == 10 and (i > 2):
                rectangles.insert(h, draw_case(i, j))
                h += 1
            elif j == 1 and (i < 1 or i > 16):
                rectangles.append(draw_case(i, j))
            elif j == 2 and (i < 2 or i > 11):
                rectangles.append(draw_case(i, j))
            elif j == 3 and (i < 2 or i > 11):
                rectangles.append(draw_case(i, j))
            elif 3 < j < 6:
                rectangles.append(draw_case(i, j))
            elif j == 6 and (i < 2 or i > 2):
                rectangles.append(draw_case(i, j))
            elif j == 7 and (i < 2 or i > 2):
                rectangles.append(draw_case(i, j))
            elif j == 9 and i == 1:
                rec = pygame.draw.rect(surface, BLANC, (i * c, j * c, c, c), 0)
                Font = pygame.font.SysFont('Comic Sans MS', 20)
                textsurface = Font.render('LANTHANIDES', True, (0, 0, 0))
                textrect = textsurface.get_rect()
                textrect.center = rec.center
                surface.blit(textsurface, textrect)
            elif j == 10 and i == 1:
                rec = pygame.draw.rect(surface, BLANC, (i * c, j * c, c, c), 0)
                Font = pygame.font.SysFont('Comic Sans MS', 20)
                textsurface = Font.render('ACTINIDES', True, (0, 0, 0))
                textrect = textsurface.get_rect()
                textrect.center = rec.center
                surface.blit(textsurface, textrect)


def draw_case(i, j):
    global rectangles
    z = pygame.draw.rect(surface, NOIR, (i * c, j * c, c, c), 1)
    return z


def fill_case():
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    SymbolFont = pygame.font.SysFont('Comic Sans MS', 20)
    NameFont = pygame.font.SysFont('arial', 9)
    MassFont = pygame.font.SysFont('Comic Sans MS', 10)
    NumberFont = pygame.font.SysFont('Comic Sans MS', 10)

    for rec in rectangles:
        data = data1[rectangles.index(rec)]
        pygame.draw.rect(surface, color[data[5]], rec, 0)
        pygame.draw.rect(surface, BLANC, rec, 1)

    for rec in rectangles:
        data = data1[rectangles.index(rec)]
        textsurface = SymbolFont.render(data[0], True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.center = rec.center
        surface.blit(textsurface, textrect)

    for rec in rectangles:
        data = data1[rectangles.index(rec)]
        textsurface = NameFont.render(data[1], True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.midbottom = rec.midbottom
        surface.blit(textsurface, textrect)

    for rec in rectangles:
        data = data1[rectangles.index(rec)]
        textsurface = MassFont.render(data[2].split('.')[0] + ' ', True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.topright = rec.topright
        surface.blit(textsurface, textrect)

    for rec in rectangles:
        data = rectangles.index(rec) + 1
        textsurface = NumberFont.render(' ' + str(data), True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.topleft = rec.topleft
        surface.blit(textsurface, textrect)


def listen():
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for rect in rectangles:
                    if rect.collidepoint(pos):
                        changecolor(rect)
                    if magni.collidepoint(pos):
                        anim(data2[rectangles.index(current)][1], data1[rectangles.index(current)][0])


def changecolor(rect):
    def _fill(recta):
        global magni, current
        rec = pygame.draw.rect(surface, color[data1[rectangles.index(recta)][5]], (4 * c, 1 * c, c * 2, c * 2), 0)
        magni = rec
        current = recta
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        SymbolFont = pygame.font.SysFont('Comic Sans MS', 40)
        NameFont = pygame.font.SysFont('arial', 18)
        MassFont = pygame.font.SysFont('Comic Sans MS', 20)
        NumberFont = pygame.font.SysFont('Comic Sans MS', 20)

        data = data1[rectangles.index(recta)]
        textsurface = SymbolFont.render(data[0], True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.center = rec.center
        surface.blit(textsurface, textrect)

        textsurface = NameFont.render(data[1], True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.midbottom = rec.midbottom
        surface.blit(textsurface, textrect)

        textsurface = MassFont.render(data[2].split('.')[0] + ' ', True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.topright = rec.topright
        surface.blit(textsurface, textrect)

        data = rectangles.index(recta) + 1
        textsurface = NumberFont.render(' ' + str(data), True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.topleft = rec.topleft
        surface.blit(textsurface, textrect)

        rec = pygame.draw.rect(surface, BLANC, (6 * c, 1 * c, c * 4, c * 2), 0)
        Font = pygame.font.SysFont('Comic Sans MS', 20)
        textsurface = Font.render(data1[rectangles.index(recta)][5], True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.topleft = rec.topleft
        surface.blit(textsurface, textrect)

        textsurface = Font.render(data1[rectangles.index(recta)][2] + " g/mol", True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.midleft = rec.midleft
        surface.blit(textsurface, textrect)

        textsurface = Font.render(data2[rectangles.index(recta)][0], True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.bottomleft = rec.bottomleft
        surface.blit(textsurface, textrect)

    _fill(rect)
    pygame.display.flip()
    pygame.draw.rect(surface, (155, 155, 155), rect, 1)
    pygame.display.flip()
    time.sleep(0.2)
    pygame.draw.rect(surface, BLANC, rect, 1)
    pygame.display.flip()


def main():
    global rectangles, WINDOW, surface, TRANSPARENT
    WINDOW = pygame.display.set_mode([La, l])
    surface = pygame.display.get_surface()
    rectangles = list()
    TRANSPARENT = pygame.Surface((La, l))
    TRANSPARENT.set_alpha(255)
    TRANSPARENT.fill(BLANC)
    pygame.draw.rect(surface, (255, 0, 0), (550, 450, 100, 50))
    rectangles = list()
    create()
    fill_case()
    pygame.display.flip()
    listen()
    pygame.quit()


class Electron(pygame.sprite.Sprite):

    def __init__(self, pos, off, angle, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (180, 206, 179), (10, 10), 10)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.offset = pygame.math.Vector2(off, 0)
        self.angle = angle

    def update(self):
        self.angle -= .25
        # Add the rotated offset vector to the pos vector to get the rect.center.
        self.rect.center = self.pos + self.offset.rotate(self.angle)


def move_anim(start_x, start_y, new_x, new_y):
    global window_size_x, window_size_y
    buffer_screen = pygame.Surface((window_size_x, window_size_y))
    buffer_screen.blit(pygame.display.get_surface(), pygame.display.get_surface().get_rect())

    window_x, window_y = eval(environ['SDL_VIDEO_WINDOW_POS'])
    dist_x, dist_y = new_x - start_x, new_y - start_y
    environ['SDL_VIDEO_WINDOW_POS'] = str(window_x + dist_x) + ',' + str(window_y + dist_y)

    window_size_x += 1 if window_size_x % 2 == 0 else -1

    screen = pygame.display.set_mode((window_size_x, window_size_y), pygame.NOFRAME)
    screen.blit(buffer_screen, buffer_screen.get_rect())
    pygame.display.flip()


def anim(conf_elec, symbol):
    global rectangles
    pressed = False
    start_pos = (0, 0)
    infos = pygame.display.Info()
    environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(infos.current_w // 2, infos.current_h // 2)
    if type(conf_elec) != int:
        y = len(conf_elec)
    else:
        y = 1
    if y == 7:
        K, L, M, N, O, P, Q = conf_elec
    elif y == 6:
        K, L, M, N, O, P, Q = conf_elec[0], conf_elec[1], conf_elec[2], conf_elec[3], conf_elec[4], conf_elec[5] \
            , 0
    elif y == 5:
        K, L, M, N, O, P, Q = conf_elec[0], conf_elec[1], conf_elec[2], conf_elec[3], conf_elec[4], 0, 0
    elif y == 4:
        K, L, M, N, O, P, Q = conf_elec[0], conf_elec[1], conf_elec[2], conf_elec[3], 0, 0, 0
    elif y == 3:
        K, L, M, N, O, P, Q = conf_elec[0], conf_elec[1], conf_elec[2], 0, 0, 0, 0
    elif y == 2:
        K, L, M, N, O, P, Q = conf_elec[0], conf_elec[1], 0, 0, 0, 0, 0
    elif y == 1:
        K, L, M, N, O, P, Q = conf_elec, 0, 0, 0, 0, 0, 0
    else:
        K, L, M, N, O, P, Q = 0, 0, 0, 0, 0, 0, 0
    pygame.init()
    screen = pygame.display.set_mode((window_size_x, window_size_y), pygame.NOFRAME | 256)
    screen_rect = screen.get_rect()
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    [Electron(screen_rect.center, 100, i * 180, all_sprites) for i in range(K)]
    [Electron(screen_rect.center, 150, i * (360 / L), all_sprites) for i in range(L)]
    [Electron(screen_rect.center, 200, i * (360 / M), all_sprites) for i in range(M)]
    [Electron(screen_rect.center, 250, i * (360 / N), all_sprites) for i in range(N)]
    [Electron(screen_rect.center, 300, i * (360 / O), all_sprites) for i in range(O)]
    [Electron(screen_rect.center, 350, i * (360 / P), all_sprites) for i in range(P)]
    [Electron(screen_rect.center, 400, i * (360 / Q), all_sprites) for i in range(Q)]

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                sys.exit()
            elif event.type == 2 or event.type == 3:
                if event.key == 13 :
                    details(symbol)
                else : main()
            elif event.type == MOUSEBUTTONDOWN:
                pressed = True
                start_pos = pygame.mouse.get_pos()

            elif event.type == MOUSEMOTION:
                if pressed:
                    new_pos = pygame.mouse.get_pos()
                    move_anim(*start_pos, *new_pos)
                    pygame.event.clear(pygame.MOUSEBUTTONUP)

            elif event.type == MOUSEBUTTONUP:
                pressed = False
                new_pos = pygame.mouse.get_pos()
                move_anim(*start_pos, *new_pos)
        pygame.font.init()
        SymbolFont = pygame.font.SysFont('arial', 50)
        all_sprites.update()
        screen.fill((64, 86, 98))
        rec = pygame.draw.circle(screen, (250, 212, 216), screen_rect.center, 60, 0)
        textsurface = SymbolFont.render(symbol, True, (100, 123, 133))
        textrect = textsurface.get_rect()
        textrect.center = rec.center
        surface.blit(textsurface, textrect)
        pygame.draw.circle(screen, (136, 160, 168), screen_rect.center, 100, 1)
        if L != 0: pygame.draw.circle(screen, (136, 160, 168), screen_rect.center, 150, 1)
        if M != 0: pygame.draw.circle(screen, (136, 160, 168), screen_rect.center, 200, 1)
        if N != 0: pygame.draw.circle(screen, (136, 160, 168), screen_rect.center, 250, 1)
        if O != 0: pygame.draw.circle(screen, (136, 160, 168), screen_rect.center, 300, 1)
        if P != 0: pygame.draw.circle(screen, (136, 160, 168), screen_rect.center, 350, 1)
        if Q != 0: pygame.draw.circle(screen, (136, 160, 168), screen_rect.center, 400, 1)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(288)


def details(e):
    pressed = False
    start_pos = (0, 0)
    infos = pygame.display.Info()
    environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(infos.current_w // 2, infos.current_h // 2)

    while True:
        pygame.init()
        screen = pygame.display.set_mode((window_size_x, window_size_y), pygame.NOFRAME | 256)
        screen.fill((64, 86, 98))
        rec = pygame.draw.rect(screen, (64, 86, 98), screen)
        SymbolFont = pygame.font.SysFont('Comic Sans MS', 40)
        textsurface = SymbolFont.render(e, True, (0, 0, 0))
        textrect = textsurface.get_rect()
        textrect.center = rec.center
        surface.blit(textsurface, textrect)
        pygame.display.update()
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                sys.exit()
            elif event.type == 2 :
                if event.key == 27:
                    main()
            elif event.type == MOUSEBUTTONDOWN:
                pressed = True
                start_pos = pygame.mouse.get_pos()

            elif event.type == MOUSEMOTION:
                if pressed:
                    new_pos = pygame.mouse.get_pos()
                    move_anim(*start_pos, *new_pos)
                    pygame.event.clear(pygame.MOUSEBUTTONUP)

            elif event.type == MOUSEBUTTONUP:
                pressed = False
                new_pos = pygame.mouse.get_pos()
                move_anim(*start_pos, *new_pos)


main()
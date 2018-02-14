"""A simple utility to get Font's Metadata from file with fonttools"""

import sys
from fontTools.ttLib import TTFont

__author__ = "Utsob Roy"
__license__ = "MIT"
__version__ = "1.1.0"
__maintainer__ = "Utsob Roy"
__email__ = "roy@codesign.com.bd"
__status__ = "Production"


UNICODE_ENCODINGS = {0: 'Unicode 1.0 semantics',
                     1: 'Unicode 1.1 semantics',
                     2: 'Unicode 1.1 semantics',
                     3: 'Unicode 2.0 and onwards semantics, Unicode BMP only (cmap subtable formats 0, 4, 6).',
                     4: 'Unicode 2.0 and onwards semantics, Unicode full repertoire (cmap subtable formats 0, 4, 6, 10, 12).',
                     5: 'Unicode Variation Sequences (cmap subtable format 14).',
                     6: 'Unicode Variation Sequences (cmap subtable format 14).'}


WINDOWS_ENCODINGS = {0: 'Symbol',
                     1: 'Unicode BMP(UCS-2)',
                     2: 'ShiftJIS',
                     3: 'PRC',
                     4: 'Big5',
                     5: 'Wansung',
                     6: 'Johab',
                     7: 'Reserved',
                     8: 'Reserved',
                     9: 'Reserved',
                     10: 'Unicode UCS-4'}


WINDOWS_LANGUAGES = {1025: 'Arabic/Saudi Arabia',
                     1026: 'Bulgarian/Bulgaria',
                     1027: 'Catalan/Catalan',
                     1028: 'Chinese/Taiwan',
                     1029: 'Czech/Czech Republic',
                     1030: 'Danish/Denmark',
                     1031: 'German/Germany',
                     1032: 'Greek/Greece',
                     1033: 'English/United States',
                     1034: 'Spanish (Traditional Sort)/Spain',
                     1035: 'Finnish/Finland',
                     1036: 'French/France',
                     1037: 'Hebrew/Israel',
                     1038: 'Hungarian/Hungary',
                     1039: 'Icelandic/Iceland',
                     1040: 'Italian/Italy',
                     1041: 'Japanese/Japan',
                     1042: 'Korean/Korea',
                     1043: 'Dutch/Netherlands',
                     1044: 'Norwegian (Bokmal)/Norway',
                     1045: 'Polish/Poland',
                     1046: 'Portuguese/Brazil',
                     1047: 'Romansh/Switzerland',
                     1048: 'Romanian/Romania',
                     1049: 'Russian/Russia',
                     1050: 'Croatian/Croatia',
                     1051: 'Slovak/Slovakia',
                     1052: 'Albanian/Albania',
                     1053: 'Swedish/Sweden',
                     1054: 'Thai/Thailand',
                     1055: 'Turkish/Turkey',
                     1056: 'Urdu/Islamic Republic of Pakistan',
                     1057: 'Indonesian/Indonesia',
                     1058: 'Ukrainian/Ukraine',
                     1059: 'Belarusian/Belarus',
                     1060: 'Slovenian/Slovenia',
                     1061: 'Estonian/Estonia',
                     1062: 'Latvian/Latvia',
                     1063: 'Lithuanian/Lithuania',
                     1064: 'Tajik (Cyrillic)/Tajikistan',
                     1066: 'Vietnamese/Vietnam',
                     1067: 'Armenian/Armenia',
                     1068: 'Azeri (Latin)/Azerbaijan',
                     1069: 'Basque/Basque',
                     1070: 'Upper Sorbian/Germany',
                     1071: 'Macedonian (FYROM)/Former Yugoslav Republic of Macedonia',
                     1074: 'Setswana/South Africa',
                     1076: 'isiXhosa/South Africa',
                     1077: 'isiZulu/South Africa',
                     1078: 'Afrikaans/South Africa',
                     1079: 'Georgian/Georgia',
                     1080: 'Faroese/Faroe Islands',
                     1081: 'Hindi/India',
                     1082: 'Maltese/Malta',
                     1083: 'Sami (Northern)/Norway',
                     1086: 'Malay/Malaysia',
                     1087: 'Kazakh/Kazakhstan',
                     1088: 'Kyrgyz/Kyrgyzstan',
                     1089: 'Kiswahili/Kenya',
                     1090: 'Turkmen/Turkmenistan',
                     1091: 'Uzbek (Latin)/Uzbekistan',
                     1092: 'Tatar/Russia',
                     1093: 'Bengali/India',
                     1094: 'Punjabi/India',
                     1095: 'Gujarati/India',
                     1096: 'Odia (formerly Oriya)/India',
                     1097: 'Tamil/India',
                     1098: 'Telugu/India',
                     1099: 'Kannada/India',
                     1100: 'Malayalam/India',
                     1101: 'Assamese/India',
                     1102: 'Marathi/India',
                     1103: 'Sanskrit/India',
                     1104: 'Mongolian (Cyrillic)/Mongolia',
                     1105: 'Tibetan/PRC',
                     1106: 'Welsh/United Kingdom',
                     1107: 'Khmer/Cambodia',
                     1108: 'Lao/Lao P.D.R.',
                     1110: 'Galician/Galician',
                     1111: 'Konkani/India',
                     1114: 'Syriac/Syria',
                     1115: 'Sinhala/Sri Lanka',
                     1117: 'Inuktitut/Canada',
                     1118: 'Amharic/Ethiopia',
                     1121: 'Nepali/Nepal',
                     1122: 'Frisian/Netherlands',
                     1123: 'Pashto/Afghanistan',
                     1124: 'Filipino/Philippines',
                     1125: 'Divehi/Maldives',
                     1128: 'Hausa (Latin)/Nigeria',
                     1130: 'Yoruba/Nigeria',
                     1131: 'Quechua/Bolivia',
                     1132: 'Sesotho sa Leboa/South Africa',
                     1133: 'Bashkir/Russia',
                     1134: 'Luxembourgish/Luxembourg',
                     1135: 'Greenlandic/Greenland',
                     1136: 'Igbo/Nigeria',
                     1144: 'Yi/PRC',
                     1146: 'Mapudungun/Chile',
                     1148: 'Mohawk/Mohawk',
                     1150: 'Breton/France',
                     1152: 'Uighur/PRC',
                     1153: 'Maori/New Zealand',
                     1154: 'Occitan/France',
                     1155: 'Corsican/France',
                     1156: 'Alsatian/France',
                     1157: 'Yakut/Russia',
                     1158: "K'iche/Guatemala",
                     1159: 'Kinyarwanda/Rwanda',
                     1160: 'Wolof/Senegal',
                     1164: 'Dari/Afghanistan',
                     2049: 'Arabic/Iraq',
                     2052: "Chinese/People's Republic of China",
                     2055: 'German/Switzerland',
                     2057: 'English/United Kingdom',
                     2058: 'Spanish/Mexico',
                     2060: 'French/Belgium',
                     2064: 'Italian/Switzerland',
                     2067: 'Dutch/Belgium',
                     2068: 'Norwegian (Nynorsk)/Norway',
                     2070: 'Portuguese/Portugal',
                     2074: 'Serbian (Latin)/Serbia',
                     2077: 'Sweden/Finland',
                     2092: 'Azeri (Cyrillic)/Azerbaijan',
                     2094: 'Lower Sorbian/Germany',
                     2107: 'Sami (Northern)/Sweden',
                     2108: 'Irish/Ireland',
                     2110: 'Malay/Brunei Darussalam',
                     2115: 'Uzbek (Cyrillic)/Uzbekistan',
                     2117: 'Bengali/Bangladesh',
                     2128: "Mongolian (Traditional)/People's Republic of China",
                     2141: 'Inuktitut (Latin)/Canada',
                     2143: 'Tamazight (Latin)/Algeria',
                     2155: 'Quechua/Ecuador',
                     3073: 'Arabic/Egypt',
                     3076: 'Chinese/Hong Kong S.A.R.',
                     3079: 'German/Austria',
                     3081: 'English/Australia',
                     3082: 'Spanish (Modern Sort)/Spain',
                     3084: 'French/Canada',
                     3098: 'Serbian (Cyrillic)/Serbia',
                     3131: 'Sami (Northern)/Finland',
                     3179: 'Quechua/Peru',
                     4097: 'Arabic/Libya',
                     4100: 'Chinese/Singapore',
                     4103: 'German/Luxembourg',
                     4105: 'English/Canada',
                     4106: 'Spanish/Guatemala',
                     4108: 'French/Switzerland',
                     4122: 'Croatian (Latin)/Bosnia and Herzegovina',
                     4155: 'Sami (Lule)/Norway',
                     5121: 'Arabic/Algeria',
                     5124: 'Chinese/Macao S.A.R.',
                     5127: 'German/Liechtenstein',
                     5129: 'English/New Zealand',
                     5130: 'Spanish/Costa Rica',
                     5132: 'French/Luxembourg',
                     5146: 'Bosnian (Latin)/Bosnia and Herzegovina',
                     5179: 'Sami (Lule)/Sweden',
                     6145: 'Arabic/Morocco',
                     6153: 'English/Ireland',
                     6154: 'Spanish/Panama',
                     6156: 'French/Principality of Monaco',
                     6170: 'Serbian (Latin)/Bosnia and Herzegovina',
                     6203: 'Sami (Southern)/Norway',
                     7169: 'Arabic/Tunisia',
                     7177: 'English/South Africa',
                     7178: 'Spanish/Dominican Republic',
                     7194: 'Serbian (Cyrillic)/Bosnia and Herzegovina',
                     7227: 'Sami (Southern)/Sweden',
                     8193: 'Arabic/Oman',
                     8201: 'English/Jamaica',
                     8202: 'Spanish/Venezuela',
                     8218: 'Bosnian (Cyrillic)/Bosnia and Herzegovina',
                     8251: 'Sami (Skolt)/Finland',
                     9217: 'Arabic/Yemen',
                     9225: 'English/Caribbean',
                     9226: 'Spanish/Colombia',
                     9275: 'Sami (Inari)/Finland',
                     10241: 'Arabic/Syria',
                     10249: 'English/Belize',
                     10250: 'Spanish/Peru',
                     11265: 'Arabic/Jordan',
                     11273: 'English/Trinidad and Tobago',
                     11274: 'Spanish/Argentina',
                     12289: 'Arabic/Lebanon',
                     12297: 'English/Zimbabwe',
                     12298: 'Spanish/Ecuador',
                     13313: 'Arabic/Kuwait',
                     13321: 'English/Republic of the Philippines',
                     13322: 'Spanish/Chile',
                     14337: 'Arabic/U.A.E.',
                     14346: 'Spanish/Uruguay',
                     15361: 'Arabic/Bahrain',
                     15370: 'Spanish/Paraguay',
                     16385: 'Arabic/Qatar',
                     16393: 'English/India',
                     16394: 'Spanish/Bolivia',
                     17417: 'English/Malaysia',
                     17418: 'Spanish/El Salvador',
                     18441: 'English/Singapore',
                     18442: 'Spanish/Honduras',
                     19466: 'Spanish/Nicaragua',
                     20490: 'Spanish/Puerto Rico',
                     21514: 'Spanish/United States'}

MACINTOSH_ENCODINGS = {0: 'Roman',
                       1: 'Japanese',
                       2: 'Chinese',
                       3: 'Korean',
                       4: 'Arabic',
                       5: 'Hebrew',
                       6: 'Greek',
                       7: 'Russian',
                       8: 'RSymbol',
                       9: 'Devanagari',
                       10: 'Gurmukhi',
                       11: 'Gujarati',
                       12: 'Oriya',
                       13: 'Bengali',
                       14: 'Tamil',
                       15: 'Telugu',
                       16: 'Kannada',
                       17: 'Malayalam',
                       18: 'Sinhalese',
                       19: 'Burmese',
                       20: 'Khmer',
                       21: 'Thai',
                       22: 'Laotian',
                       23: 'Georgian',
                       24: 'Armenian',
                       25: 'Chinese',
                       26: 'Tibetan',
                       27: 'Mongolian',
                       28: 'Geez',
                       29: 'Slavic',
                       30: 'Vietnamese',
                       31: 'Sindhi',
                       32: 'Uninterpreted'}

MACINTOSH_LANGUAGES = {0: 'English',
                       1: 'French',
                       2: 'German',
                       3: 'Italian',
                       4: 'Dutch',
                       5: 'Swedish',
                       6: 'Spanish',
                       7: 'Danish',
                       8: 'Portuguese',
                       9: 'Norwegian',
                       10: 'Hebrew',
                       11: 'Japanese',
                       12: 'Arabic',
                       13: 'Finnish',
                       14: 'Inuktitut',
                       15: 'Icelandic',
                       16: 'Maltese',
                       17: 'Turkish',
                       18: 'Croatian',
                       19: 'Chinese (Traditional)',
                       20: 'Urdu',
                       21: 'Hindi',
                       22: 'Thai',
                       23: 'Korean',
                       24: 'Lithuanian',
                       25: 'Polish',
                       26: 'Hungarian',
                       27: 'Estonian',
                       28: 'Latvian',
                       29: 'Sami',
                       30: 'Faroese',
                       31: 'Farsi/Persian',
                       32: 'Russian',
                       33: 'Chinese (Simplified)',
                       34: 'Flemish',
                       35: 'Irish Gaelic',
                       36: 'Albanian',
                       37: 'Romanian',
                       38: 'Czech',
                       39: 'Slovak',
                       40: 'Slovenian',
                       41: 'Yiddish',
                       42: 'Serbian',
                       43: 'Macedonian',
                       44: 'Bulgarian',
                       45: 'Ukrainian',
                       46: 'Byelorussian',
                       47: 'Uzbek',
                       48: 'Kazakh',
                       49: 'Azerbaijani (Cyrillic script)',
                       50: 'Azerbaijani (Arabic script)',
                       51: 'Armenian',
                       52: 'Georgian',
                       53: 'Moldavian',
                       54: 'Kirghiz',
                       55: 'Tajiki',
                       56: 'Turkmen',
                       57: 'Mongolian (Mongolian script)',
                       58: 'Mongolian (Cyrillic script)',
                       59: 'Pashto',
                       60: 'Kurdish',
                       61: 'Kashmiri',
                       62: 'Sindhi',
                       63: 'Tibetan',
                       64: 'Nepali',
                       65: 'Sanskrit',
                       66: 'Marathi',
                       67: 'Bengali',
                       68: 'Assamese',
                       69: 'Gujarati',
                       70: 'Punjabi',
                       71: 'Oriya',
                       72: 'Malayalam',
                       73: 'Kannada',
                       74: 'Tamil',
                       75: 'Telugu',
                       76: 'Sinhalese',
                       77: 'Burmese',
                       78: 'Khmer',
                       79: 'Lao',
                       80: 'Vietnamese',
                       81: 'Indonesian',
                       82: 'Tagalong',
                       83: 'Malay (Roman script)',
                       84: 'Malay (Arabic script)',
                       85: 'Amharic',
                       86: 'Tigrinya',
                       87: 'Galla',
                       88: 'Somali',
                       89: 'Swahili',
                       90: 'Kinyarwanda/Ruanda',
                       91: 'Rundi',
                       92: 'Nyanja/Chewa',
                       93: 'Malagasy',
                       94: 'Esperanto',
                       128: 'Welsh',
                       129: 'Basque',
                       130: 'Catalan',
                       131: 'Latin',
                       132: 'Quenchua',
                       133: 'Guarani',
                       134: 'Aymara',
                       135: 'Tatar',
                       136: 'Uighur',
                       137: 'Dzongkha',
                       138: 'Javanese (Roman script)',
                       139: 'Sundanese (Roman script)',
                       140: 'Galician',
                       141: 'Afrikaans',
                       142: 'Breton',
                       144: 'Scottish Gaelic',
                       145: 'Manx Gaelic',
                       146: 'Irish Gaelic (with dot above)',
                       147: 'Tongan',
                       148: 'Greek (polytonic)',
                       149: 'Greenlandic',
                       150: 'Azerbaijani (Roman script)'}

ISO_IDS = {
    0: '7-bit ASCII',
    1: 'ISO 10646',
    2: 'ISO 8859-1'
}

CUSTOMS = {}


PLATFORMS = {0: {'name': 'Unicode',
                 'encodings': UNICODE_ENCODINGS,
                 'languages': UNICODE_ENCODINGS},
             1: {'name': 'Macintosh',
                 'encodings': MACINTOSH_ENCODINGS,
                 'languages': MACINTOSH_LANGUAGES},
             2: {'name': 'ISO [deprecated]',
                 'encodings': ISO_IDS,
                 'languages': ISO_IDS},
             3: {'name': 'Windows',
                 'encodings': WINDOWS_ENCODINGS,
                 'languages': WINDOWS_LANGUAGES},
             4: {'name': 'Custom',
                 'encodings': CUSTOMS,
                 'languages': CUSTOMS}}


NAME_TABLE = {0: 'Copyright Notice',
              1: 'Font Family',
              2: 'SubFamily',
              3: 'Unique Font Identifier',
              4: 'Full Font Name',
              5: 'Version',
              6: 'PostScript Name',
              7: 'Trademark',
              8: 'Manufacturer Name',
              9: 'Designer',
              10: 'Description',
              11: 'Vendor URL',
              12: 'Designer URL',
              13: 'License Description',
              14: 'License Info URL',
              15: 'Reserved',
              16: 'Typographic Family',
              17: 'Typographic SubFamily',
              18: 'Compatible Full',
              19: 'Sample Text',
              20: 'PostScript CID findfont name',
              21: 'WWS Family Name',
              22: 'WWS SubFamily Name',
              23: 'Light Background Pallete',
              24: 'Dark Background Pallete',
              25: 'Variations PostScript Name Prefix'}


ENCODINGS = {
    "Roman": 'latin_1'
}


class FontMeta:
    """This Class provides easy way to get data"""
    def __init__(self, fontfile):
        """Takes a fontfile path and parses metas."""
        self.FONT = TTFont(fontfile)
        self.DATA = self._parse_meta()

    def _parse_meta(self):
        """The main meta parsing function. Thanks to Fonttools library."""
        data = {}
        for nti in self.FONT['name'].names:
            key = nti.nameID
            platform_data = PLATFORMS[nti.platformID]
            if platform_data['name'] == 'Custom':
                encoding = {'id': 0, 'value': 'Custom'}
                language = {'id': 0, 'value': 'Custom'}
            else:
                encoding = {'id': nti.platEncID,
                            'value': platform_data['encodings'].get(nti.platEncID, "Unknown")}
                language = {'id': nti.langID,
                            'value': platform_data['languages'].get(nti.langID, "Unknown")}
            if b'\x00' in nti.string:
                name_str = nti.string.decode('utf-16-be')
            else:
                try:
                    enc = ENCODINGS.get(encoding['value'], False)
                    if enc:
                        name_str = nti.string.decode(enc)
                    else:
                        name_str = nti.string.decode('utf-8')
                except UnicodeDecodeError:
                    print(encoding)
                    print(language)
                    print(nti.string)

            field = NAME_TABLE.get(nti.nameID, False)
            if not field:
                if 26 <= nti.nameID <= 255:
                    field = 'Reserved [{}]'.format(nti.nameID)
                elif 256 <= nti.nameID:
                    field = 'Font Specific[{}]'.format(nti.nameID)

            data[key] = {"field": field,
                         "value": name_str,
                         "encoding": encoding,
                         "language": language
            }
        return data

    def get_full_data(self):
        """Get Full Version of Data."""
        return self.DATA

    def get_data(self):
        """Get a streamlined yet usable version of data."""
        data = {}
        for key in self.DATA:
            d = self.DATA[key]
            data[d['field'].lower().replace(' ', '_')] = d['value']
        return data


def main():
    fonts = sys.argv[1:]
    for font in fonts:
        try:
            try:
                f = FontMeta(font)
                try:
                    data = f.get_data()
                    for key in data:
                        print("{}: {}".format(key, data[key]))
                except RuntimeError:
                    print("Something is wrong. Ask the goddamn developer.")
            except IOError:
                print("Can't get the file.")
        except RuntimeError:
            print("Something is wrong. Ask the goddamn developer.")


if __name__ == '__main__':
    main()

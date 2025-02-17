# List of valid ICAO ranges and their associated countries
icao_ranges = [
    #('000000', '003FFF', 'unallocated'),
    ('004000', '0043FF', 'Zimbabwe'),
    ('006000', '006FFF', 'Mozambique'),
    ('008000', '00FFFF', 'South Africa'),
    ('010000', '017FFF', 'Egypt'),
    ('018000', '01FFFF', 'Libya'),
    ('020000', '027FFF', 'Morocco'),
    ('028000', '02FFFF', 'Tunisia'),
    ('030000', '0303FF', 'Botswana'),
    ('032000', '032FFF', 'Burundi'),
    ('034000', '034FFF', 'Cameroon'),
    ('035000', '0353FF', 'Comoros'),
    ('036000', '036FFF', 'Congo'),
    ('038000', '038FFF', 'Côte d\'Ivoire'),
    ('03E000', '03EFFF', 'Gabon'),
    ('040000', '040FFF', 'Ethiopia'),
    ('042000', '042FFF', 'Equatorial Guinea'),
    ('044000', '044FFF', 'Ghana'),
    ('046000', '046FFF', 'Guinea'),
    ('048000', '0483FF', 'Guinea-Bissau'),
    ('04A000', '04A3FF', 'Lesotho'),
    ('04C000', '04CFFF', 'Kenya'),
    ('050000', '050FFF', 'Liberia'),
    ('054000', '054FFF', 'Madagascar'),
    ('058000', '058FFF', 'Malawi'),
    ('05A000', '05A3FF', 'Maldives'),
    ('05C000', '05CFFF', 'Mali'),
    ('05E000', '05E3FF', 'Mauritania'),
    ('060000', '0603FF', 'Mauritius'),
    ('062000', '062FFF', 'Niger'),
    ('064000', '064FFF', 'Nigeria'),
    ('068000', '068FFF', 'Uganda'),
    ('06A000', '06A3FF', 'Qatar'),
    ('06C000', '06CFFF', 'Central African Republic'),
    ('06E000', '06EFFF', 'Rwanda'),
    ('070000', '070FFF', 'Senegal'),
    ('074000', '0743FF', 'Seychelles'),
    ('076000', '0763FF', 'Sierra Leone'),
    ('078000', '078FFF', 'Somalia'),
    ('07A000', '07A3FF', 'Swaziland'),
    ('07C000', '07CFFF', 'Sudan'),
    ('080000', '080FFF', 'Tanzania'),
    ('084000', '084FFF', 'Chad'),
    ('088000', '088FFF', 'Togo'),
    ('08A000', '08AFFF', 'Zambia'),
    ('08C000', '08CFFF', 'D R Congo'),
    ('090000', '090FFF', 'Angola'),
    ('094000', '0943FF', 'Benin'),
    ('096000', '0963FF', 'Cape Verde'),
    ('098000', '0983FF', 'Djibouti'),
    ('09A000', '09AFFF', 'Gambia'),
    ('09C000', '09CFFF', 'Burkina Faso'),
    ('09E000', '09E3FF', 'Sao Tome'),
    ('0A0000', '0A7FFF', 'Algeria'),
    ('0A8000', '0A8FFF', 'Bahamas'),
    ('0AA000', '0AA3FF', 'Barbados'),
    ('0AB000', '0AB3FF', 'Belize'),
    ('0AC000', '0ACFFF', 'Colombia'),
    ('0AE000', '0AEFFF', 'Costa Rica'),
    ('0B0000', '0B0FFF', 'Cuba'),
    ('0B2000', '0B2FFF', 'El Salvador'),
    ('0B4000', '0B4FFF', 'Guatemala'),
    ('0B6000', '0B6FFF', 'Guyana'),
    ('0B8000', '0B8FFF', 'Haiti'),
    ('0BA000', '0BAFFF', 'Honduras'),
    ('0BC000', '0BC3FF', 'St.Vincent + Grenadines'),
    ('0BE000', '0BEFFF', 'Jamaica'),
    ('0C0000', '0C0FFF', 'Nicaragua'),
    ('0C2000', '0C2FFF', 'Panama'),
    ('0C4000', '0C4FFF', 'Dominican Republic'),
    ('0C6000', '0C6FFF', 'Trinidad and Tobago'),
    ('0C8000', '0C8FFF', 'Suriname'),
    ('0CA000', '0CA3FF', 'Antigua & Barbuda'),
    ('0CC000', '0CC3FF', 'Grenada'),
    ('0D0000', '0D7FFF', 'Mexico'),
    ('0D8000', '0DFFFF', 'Venezuela'),
    ('100000', '1FFFFF', 'Russia'),
    #('200000', '27FFFF', 'reserved AFI'),
    #('280000', '2FFFFF', 'reserved SAM'),
    ('300000', '33FFFF', 'Italy'),
    ('340000', '37FFFF', 'Spain'),
    ('380000', '3BFFFF', 'France'),
    ('3C0000', '3FFFFF', 'Germany'),
    ('400000', '43FFFF', 'United Kingdom'),
    ('440000', '447FFF', 'Austria'),
    ('448000', '44FFFF', 'Belgium'),
    ('450000', '457FFF', 'Bulgaria'),
    ('458000', '45FFFF', 'Denmark'),
    ('460000', '467FFF', 'Finland'),
    ('468000', '46FFFF', 'Greece'),
    ('470000', '477FFF', 'Hungary'),
    ('478000', '47FFFF', 'Norway'),
    ('480000', '487FFF', 'Netherlands'),
    ('488000', '48FFFF', 'Poland'),
    ('490000', '497FFF', 'Portugal'),
    ('498000', '49FFFF', 'Czech Republic'),
    ('4A0000', '4A7FFF', 'Romania'),
    ('4A8000', '4AFFFF', 'Sweden'),
    ('4B0000', '4B7FFF', 'Switzerland'),
    ('4B8000', '4BFFFF', 'Turkey'),
    ('4C0000', '4C7FFF', 'Yugoslavia'),
    ('4C8000', '4C83FF', 'Cyprus'),
    ('4CA000', '4CAFFF', 'Ireland'),
    ('4CC000', '4CCFFF', 'Iceland'),
    ('4D0000', '4D03FF', 'Luxembourg'),
    ('4D2000', '4D23FF', 'Malta'),
    ('4D4000', '4D43FF', 'Monaco'),
    ('500000', '5003FF', 'San Marino'),
    #('500000', '5FFFFF', 'reserved EUR/NAT'),
    ('501000', '5013FF', 'Albania'),
    ('501C00', '501FFF', 'Croatia'),
    ('502C00', '502FFF', 'Latvia'),
    ('503C00', '503FFF', 'Lithuania'),
    ('504C00', '504FFF', 'Moldova'),
    ('505C00', '505FFF', 'Slovakia'),
    ('506C00', '506FFF', 'Slovenia'),
    ('507C00', '507FFF', 'Uzbekistan'),
    ('508000', '50FFFF', 'Ukraine'),
    ('510000', '5103FF', 'Belarus'),
    ('511000', '5113FF', 'Estonia'),
    ('512000', '5123FF', 'Macedonia'),
    ('513000', '5133FF', 'Bosnia & Herzegovina'),
    ('514000', '5143FF', 'Georgia'),
    ('515000', '5153FF', 'Tajikistan'),
    ('600000', '6003FF', 'Armenia'),
    #('600000', '67FFFF', 'reserved MID'),
    ('600800', '600BFF', 'Azerbaijan'),
    ('601000', '6013FF', 'Kyrgyzstan'),
    ('601800', '601BFF', 'Turkmenistan'),
    #('680000', '6FFFFF', 'reserved ASIA'),
    ('680000', '6803FF', 'Bhutan'),
    ('681000', '6813FF', 'Kyrgyzstan'),
    ('682000', '6823FF', 'Mongolia'),
    ('683000', '6833FF', 'Kazakhstan'),
    ('684000', '6843FF', 'Palau'),
    ('700000', '700FFF', 'Afghanistan'),
    ('702000', '702FFF', 'Bangladesh'),
    ('704000', '704FFF', 'Myanmar'),
    ('706000', '706FFF', 'Kuwait'),
    ('708000', '708FFF', 'Laos'),
    ('70A000', '70AFFF', 'Nepal'),
    ('70C000', '70C3FF', 'Oman'),
    ('70E000', '70EFFF', 'Cambodia'),
    ('710000', '717FFF', 'Saudi Arabia'),
    ('718000', '71FFFF', 'South Korea'),
    ('720000', '727FFF', 'North Korea'),
    ('728000', '72FFFF', 'Iraq'),
    ('730000', '737FFF', 'Iran'),
    ('738000', '73FFFF', 'Israel'),
    ('740000', '747FFF', 'Jordan'),
    ('748000', '74FFFF', 'Lebanon'),
    ('750000', '757FFF', 'Malaysia'),
    ('758000', '75FFFF', 'Philippines'),
    ('760000', '767FFF', 'Pakistan'),
    ('768000', '76FFFF', 'Singapore'),
    ('770000', '777FFF', 'Sri Lanka'),
    ('778000', '77FFFF', 'Syria'),
    ('780000', '7BFFFF', 'China'),
    ('7C0000', '7FFFFF', 'Australia'),
    ('800000', '83FFFF', 'India'),
    ('840000', '87FFFF', 'Japan'),
    ('880000', '887FFF', 'Thailand'),
    ('888000', '88FFFF', 'Vietnam'),
    ('890000', '890FFF', 'Yemen'),
    ('894000', '894FFF', 'Bahrain'),
    ('895000', '8953FF', 'Brunei'),
    ('896000', '896FFF', 'United Arab Emirates'),
    ('897000', '8973FF', 'Solomon Islands'),
    ('898000', '898FFF', 'Papua New Guinea'),
    ('899000', '8993FF', 'Taiwan (unofficial)'),
    ('8A0000', '8A7FFF', 'Indonesia'),
    #('900000', '9FFFFF', 'reserved NAM/PAC'),
    ('900000', '9003FF', 'Marshall Islands'),
    ('901000', '9013FF', 'Cook Islands'),
    ('902000', '9023FF', 'Samoa'),
    ('A00000', 'AFFFFF', 'United States'),
    #('B00000', 'BFFFFF', 'reserved'),
    ('C00000', 'C3FFFF', 'Canada'),
    ('C80000', 'C87FFF', 'New Zealand'),
    ('C88000', 'C88FFF', 'Fiji'),
    ('C8A000', 'C8A3FF', 'Nauru'),
    ('C8C000', 'C8C3FF', 'Saint Lucia'),
    ('C8D000', 'C8D3FF', 'Tonga'),
    ('C8E000', 'C8E3FF', 'Kiribati'),
    ('C90000', 'C903FF', 'Vanuatu'),
    #('D00000', 'DFFFFF', 'reserved'),
    ('E00000', 'E3FFFF', 'Argentina'),
    ('E40000', 'E7FFFF', 'Brazil'),
    ('E80000', 'E80FFF', 'Chile'),
    ('E84000', 'E84FFF', 'Ecuador'),
    ('E88000', 'E88FFF', 'Paraguay'),
    ('E8C000', 'E8CFFF', 'Peru'),
    ('E90000', 'E90FFF', 'Uruguay'),
    ('E94000', 'E94FFF', 'Bolivia'),
    #('EC0000', 'EFFFFF', 'reserved CAR'),
    #('F00000', 'F07FFF', 'ICAO (1)'),
    #('F00000', 'FFFFFF', 'reserved')
]


def find_country(icao_address):
    # Convert ICAO address to numeric value
    icao_num = int(icao_address, 16)

    for start, end, country in icao_ranges:
        if int(start, 16) <= icao_num <= int(end, 16):
            return country

    return None


# # Test the function
# icao_test = "BB3887"
# country = find_country(icao_test)
# print(f"The ICAO address {icao_test} belongs to: {country}")

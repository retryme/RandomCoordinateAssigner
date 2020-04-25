import random
import csv

## Number of jobs will be created
is_sayisi = 100

# IF random_real =1 below script uses max_min_dict values regarding key else uses below configurations
random_real = 1

latitude_min = 41.0604
latitude_max = 41.0904

longitude_min = 28.817
longitude_max = 28.37

max_min_dict = {

    'k1': {'min_lat': 40.9819899882571, 'max_lat': 41.0630100403232, 'min_lon': 28.7747959793319,
           'max_lon': 28.8143776983627},
    'k2': {'min_lat': 41.0292, 'max_lat': 41.4225637390451, 'min_lon': 27.9885189588831, 'max_lon': 28.6537},
    'k3': {'min_lat': 41.0130610615777, 'max_lat': 41.081653804441, 'min_lon': 28.9082740824777,
           'max_lon': 28.9238946841663},
    'k4': {'min_lat': 40.9617, 'max_lat': 41.0357831998865, 'min_lon': 29.1253214308581, 'max_lon': 29.1979730715189},
    'k5': {'min_lat': 40.9722395089827, 'max_lat': 41.063853729348, 'min_lon': 28.7179398275386,
           'max_lon': 28.7479726659011},
    'k6': {'min_lat': 40.9610827517922, 'max_lat': 41.1037043750367, 'min_lon': 28.6403816431846,
           'max_lon': 28.6827277829949},
    'k7': {'min_lat': 41.1068448803499, 'max_lat': 41.2567606486154, 'min_lon': 28.95059741034,
           'max_lon': 29.1108925652609},
    'k8': {'min_lat': 40.9562167964377, 'max_lat': 41.0169411746608, 'min_lon': 28.7769171425581,
           'max_lon': 28.9211449932422},
    'k9': {'min_lat': 40.9546090047685, 'max_lat': 41.0016551602123, 'min_lon': 29.0457003534383,
           'max_lon': 29.1117676653079},
    'k10': {'min_lat': 40.9934148029084, 'max_lat': 41.0390428441243, 'min_lon': 28.9343821140627,
            'max_lon': 28.9815063842938},
    'k11': {'min_lat': 40.9928765289352, 'max_lat': 41.0941978236019, 'min_lon': 28.8248, 'max_lon': 29.1400420795171},
    'k12': {'min_lat': 41.0138, 'max_lat': 41.2397332682159, 'min_lon': 28.808208607604, 'max_lon': 29.0604},
    'k13': {'min_lat': 40.873268808426, 'max_lat': 40.9389865733286, 'min_lon': 29.2363909214134,
            'max_lon': 29.2448889145169},
    'k14': {'min_lat': 40.9152301885507, 'max_lat': 40.974300992451, 'min_lon': 29.1940596562003,
            'max_lon': 29.1940596562003},
    'k15': {'min_lat': 40.9811301114561, 'max_lat': 41.0396260594275, 'min_lon': 29.0222, 'max_lon': 29.0737997118336},
    'k16': {'min_lat': 40.8756619819661, 'max_lat': 41.0146, 'min_lon': 29.270288048027, 'max_lon': 29.4684290617179},
    'k17': {'min_lat': 40.9958459350447, 'max_lat': 41.0628104952018, 'min_lon': 28.8949317416637, 'max_lon': 28.8995},
    'k18': {'min_lat': 41.0222736062571, 'max_lat': 41.0556995439134, 'min_lon': 28.9694428417739,
            'max_lon': 28.9920968358671},
    'k19': {'min_lat': 41.0564922157601, 'max_lat': 41.2308945396857, 'min_lon': 29.0926400434478,
            'max_lon': 29.3065695622144},
    'k20': {'min_lat': 41.0379, 'max_lat': 41.1131, 'min_lon': 29.000429018604, 'max_lon': 29.0773},
    'k21': {'min_lat': 40.8047718886622, 'max_lat': 41.0356220204446, 'min_lon': 29.2757240258329,
            'max_lon': 29.3730417439764},
    'k22': {'min_lat': 41.0394764659958, 'max_lat': 41.0774587761194, 'min_lon': 29.0059, 'max_lon': 29.0142539928755},
    'k23': {'min_lat': 40.991952394286, 'max_lat': 41.0721322327973, 'min_lon': 29.0527722235027,
            'max_lon': 29.1245308847199},
    'k24': {'min_lat': 41.0642, 'max_lat': 41.1885, 'min_lon': 28.8532471039074, 'max_lon': 28.9222141674795},
    'k25': {'min_lat': 41.037, 'max_lat': 41.0936504460949, 'min_lon': 28.946721748061, 'max_lon': 28.9580314075359},
    'k26': {'min_lat': 41.1358187492973, 'max_lat': 41.3425682277314, 'min_lon': 28.6743184660798,
            'max_lon': 28.8089708629174},
    'k27': {'min_lat': 40.9516727458777, 'max_lat': 41.1323805562089, 'min_lon': 29.1775996824868,
            'max_lon': 29.3579635627157},
    'k28': {'min_lat': 40.9782812454119, 'max_lat': 41.2084688410413, 'min_lon': 29.3012191034021,
            'max_lon': 29.9072192127584},
    'k29': {'min_lat': 41.0549946491516, 'max_lat': 41.4044256109069, 'min_lon': 28.3843300055996,
            'max_lon': 28.6852734670206},
    'k30': {'min_lat': 41.0524884996514, 'max_lat': 41.1431171715617, 'min_lon': 28.7023838460711,
            'max_lon': 28.8682960329708},
    'k31': {'min_lat': 40.9722532341102, 'max_lat': 41.0723300844017, 'min_lon': 28.8338719117357,
            'max_lon': 29.274431083429}

}

##In open csv file directory will be written
##name_1 = '' output file name will be written

with open(r'allbcdall.csv', encoding='utf-8') as csv_file:
    name_1 = 'this' + '.json'

    text_file = open(name_1, "a+", encoding='utf-8')
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    job_type_dict = dict()
    for row in csv_reader:
        if line_count == 0:
            # coulmns in csv file
            # print(f'Column names are {", ".join(row)}')
            line_count = line_count + 1
        else:
            # creates a dictionary from csv file
            job_type_dict[row[1]] = (row[3], row[2])
    # dcit converted to list to use index
    dict_to_list = list(job_type_dict.items())
    # print(dict_to_list)

    for number_of_jobs in range(is_sayisi):

        # random items will be selected
        temp_list = random.choice(dict_to_list)

        text_file.write('{' + '\n')
        text_file.write('\"alan1\"' + ':' + str(temp_list[1][0]) + ',' + '\n')
        text_file.write('\"alan2\"' + ':' + '\"' + str(number_of_jobs + 1) + '\"' + ',' + '\n')
        text_file.write('\"alan3\"' + ':' + '\"' + str(temp_list[0]) + '\"' + ',' + '\n')
        text_file.write('\"alan4\"' + ':' + '\"' + temp_list[1][1] + '\"' + ',' + '\n')
        if random_real == 0:
            text_file.write('\"alan5\"' + ':' + '\"' + str(random.uniform(latitude_max, latitude_min)) + ',' + str(
                random.uniform(longitude_max, longitude_min)) + '\"' + ',' + '\n')
        else:
            text_file.write('\"alan6\"' + ':' + '\"' + str(
                random.uniform(float(max_min_dict[temp_list[1][0]]['max_lat']),
                               float(max_min_dict[temp_list[1][0]]['min_lat']))) + ',' + str(
                random.uniform(float(max_min_dict[temp_list[1][0]]['max_lon']),
                               float(max_min_dict[temp_list[1][0]]['min_lon']))) + '\"' + ',' + '\n')

        text_file.write('\"alan7\"' + ':' + '\"{{date1}}\"' + ',' + '\n')
        text_file.write('\"alan8\"' + ':' + '\"{{date2}}\"' + '\n')

        if number_of_jobs == is_sayisi - 1:
            text_file.write('}')
        else:
            text_file.write('},')
            text_file.write('\n')
            line_count += 1
    text_file.close()
    print("Dosya hazır", name_1)












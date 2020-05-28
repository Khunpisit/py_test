import re

#1. Remove “WUB” from a string.
def songDecoder(song):
    keyword = 'WUB'
    replacedSong = re.sub(keyword, ' ', song).strip()
    cleanSong = ' '.join(replacedSong.split())
    return cleanSong

#2 Find information from data by specific search word.
def phone(data: str, search_word):
    data_list = list(filter(None, data.split('\n')))
    info_list = parse_raw_data(data_list)
    result = list(filter(lambda x: search_word in x, info_list))

    if len(result) == 0:
        return "Error => Not found: %s" % search_word
    elif len(result) == 1:
        return "Phone => %s, Name => %s, Address => %s" % (result[0][0], result[0][1], result[0][2])
    else:
        return "Error => Too many people: %s" % search_word

def parse_raw_data(data_list):
    info_list = []

    for d in data_list:
        phone_number = re.compile(r'(\d{1,2}-\d{3}-\d{3}-\d{4})').search(d).group(1)
        name = re.compile(r'<(.*)>').search(d).group(1)
        raw_address = re.compile(r'(?:([ @!#$%^&*()<>?/\|}{~:;]\+\d{1,2}-\d{3}-\d{3}-\d{4})|<(.*)>|\/|;|!|,)').sub('', d)
        address = ' '.join(raw_address.strip().replace('_', ' ').split(None))
        info_list.append((phone_number, name, address))

    return info_list


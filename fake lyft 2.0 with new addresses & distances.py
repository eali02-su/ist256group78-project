# pair 0- DellPlain Residence Hall, Destiny USA
#pair 1- Starbucks (On University), Manley Field House
#pair 2- Bird Library, Sadler Residence Hall
#pair 3- Carrier Dome, Pastabilities
#pair 4- The Ice Cream Stand, Life Sciences Complex



dict_1={0:['601 Comstock Avenue, Syracuse, New York 13244', '9090 Destiny Usa Dr, Syracuse, New York 13204'],1:['177 Marshall St, Syracuse, New York 13210', '1301 E Colvin St, Syracuse, New York 13210'],2:['222 Waverly Ave, Syracuse, New York 13244', '1000 Irving Avenue, Syracuse, New York 13244'],3:['900 Irving Ave, Syracuse, New York 13244', '311 S Franklin St, Syracuse, New York 13202'],4:['200 W Water St, Syracuse, New York 13202', '107 College Pl, Syracuse, New York 13244']}


def fake_lyft(loc):
    """
    Input: dictionary containing various trips
    Output: price
    
    """
    new_dict ={}
    for key in loc:
        if len(loc[key]) != 2:
            if len(loc[key]) == 1:
                raise AssertionError('ERROR:No destination given, Please enter a destination and try again!')
            else:
                raise AssertionError('ERROR: Too many destinations given')
        if loc[key][0]==loc[key][1]:
            raise AssertionError('ERROR: Start and end destination are the same')
        if loc[key][0] == '601 Comstock Avenue, Syracuse, New York 13244' or loc[key][0] == '9090 Destiny Usa Dr, Syracuse, New York 13204' and loc[key][1] == '601 Comstock Avenue, Syracuse, New York 13244' or loc[key][1] == '9090 Destiny Usa Dr, Syracuse, New York 13204':
            dist = 4 #miles
            price = dist*(2.60) #miles*price per mile
            new_dict[(loc[key][0],loc[key][1])]=round(price,2)
            new_dict[(loc[key][1],loc[key][0])]=round(price,2)
        if loc[key][0] == '177 Marshall St, Syracuse, New York 13210' or loc[key][0] == '1301 E Colvin St, Syracuse, New York 13210' and loc[key][1] == '177 Marshall St, Syracuse, New York 13210' or loc[key][1] == '1301 E Colvin St, Syracuse, New York 13210':
            dist = 1.67 #miles
            price = dist*(2.60) #miles*price per mile
            new_dict[(loc[key][0],loc[key][1])]=round(price,2)
            new_dict[(loc[key][1],loc[key][0])]=round(price,2)
        if loc[key][0] == '222 Waverly Ave, Syracuse, New York 13244' or loc[key][0] == '1000 Irving Avenue, Syracuse, New York 13244' and loc[key][1] == '222 Waverly Ave, Syracuse, New York 13244' or loc[key][1] == '1000 Irving Avenue, Syracuse, New York 13244':
            dist = .75 #miles
            price = dist*(2.60) #miles*price per mile
            new_dict[(loc[key][0],loc[key][1])]=round(price,2)
            new_dict[(loc[key][1],loc[key][0])]=round(price,2)
        if loc[key][0] == '900 Irving Ave, Syracuse, New York 13244' or loc[key][0] == '311 S Franklin St, Syracuse, New York 13202' and loc[key][1] == '900 Irving Ave, Syracuse, New York 13244' or loc[key][1] == 'I311 S Franklin St, Syracuse, New York 13202':
            dist = 1.66 #miles
            price = dist*(2.60) #miles*price per mile
            new_dict[(loc[key][0],loc[key][1])]=round(price,2)
            new_dict[(loc[key][1],loc[key][0])]=round(price,2)
        if loc[key][0] == '200 W Water St, Syracuse, New York 13202' or loc[key][0] == '107 College Pl, Syracuse, New York 13244' and loc[key][1] == '200 W Water St, Syracuse, New York 13202' or loc[key][1] == '107 College Pl, Syracuse, New York 13244':
            dist = 2.22 #miles
            price = dist*(2.60) #miles*price per mile
            new_dict[(loc[key][0],loc[key][1])]=round(price,2)
            new_dict[(loc[key][1],loc[key][0])]=round(price,2)
    return new_dict
    
#print(fake_lyft(dict_1))


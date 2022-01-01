#
# using the OMW create a model
#
import os
import yaml
import wn

wn.download('omw:1.4')
wn.download('odenet:1.3')


negators = {'i18282', 'i18284', 'i18436', #no
            'i2944', # neither
            'i18262', 'i18263', # never
            'i12559', 'i18285', # none
            'i18280', # not
            'i18281', # nothing ## NOT 'i109082',
            'i18289', # nowhere   # FCB does this help?
            'i18348', # rarely, seldom
            }
# missing contracted auxiliaries and without, nope, uh-uh, uhuh, nor

intensifiers = {'i18320', #very
                'i18185', 
                'i18187', 
                'i18188', 
                'i18194', 
                'i18197', 
                'i18198', 
                'i18199', 
                'i18202', 
                'i18207', 
                'i18225', 
                'i18249', 
                'i18250', 
                'i18251', 
                'i18252', 
                'i18259',
                'i18260', 
                'i18270', 
                'i18287', 
                'i18320', 
                'i18321', 
                'i18324', 
                'i18325', 
                'i18344', 
                'i18345', 
                'i18356', 
                'i18357', 
                'i18359', 
                'i18361', 
                'i18368', 
                'i18370', 
                'i18390', 
                'i18410', 
                'i18413', 
                'i18414', 
                'i18424', 
                'i18465', 
                'i18466', 
                'i18474', 
                'i18475', 
                'i18480', 
                'i18481', 
                'i18493', 
                'i18494', 
                'i18495', 
                'i18533', 
                'i18578', 
                'i18629', 
                'i18648', 
                'i18654', 
                'i18656', 
                'i18689', 
                'i18690', 
                'i18691', 
                'i18748', 
                'i18760', 
                'i18762', 
                'i18776', 
                'i18815', 
                'i18846', 
                'i18849', 
                'i18888', 
                'i18889', 
                'i18890', 
                'i18894', 
                'i18907', 
                'i18911', 
                'i19062', 
                'i19066', 
                'i19112', 
                'i19124', 
                'i19125', 
                'i19126', 
                'i19127', 
                'i19128', 
                'i19129', 
                'i19142', 
                'i19207', 
                'i19322', 
                'i19332', 
                'i19334', 
                'i19335', 
                'i19351', 
                'i19359', 
                'i19362', 
                'i19363', 
                'i19364', 
                'i19386', 
                'i19401', 
                'i19433', 
                'i19453', 
                'i19476', 
                'i19486', 
                'i19495', 
                'i19535', 
                'i19587', 
                'i19588', 
                'i19612', 
                'i19619', 
                'i19671', 
                'i19683', 
                'i19685', 
                'i19688', 
                'i19689', 
                'i19690', 
                'i19692', 
                'i19827', 
                'i19843', 
                'i19856', 
                'i19857', 
                'i20139', 
                'i20140', 
                'i20206', 
                'i20266', 
                'i20267', 
                'i20268', 
                'i20361', 
                'i20362', 
                'i20446', 
                'i20602', 
                'i20603', 
                'i20604', 
                'i20605', 
                'i20659', 
                'i20673', 
                'i20733', 
                'i20740', 
                'i20795', 
                'i20807', 
                'i20968', 
                'i21036', 
                'i21086', 
                'i21281', 
                'i21647', 
                'i21657', 
                'i21666', 
                'i21667', 
                'i21670', 
                'i21714', 
                'i21720'
}

diminishers = {'i18163', 'i18581', #barely
               'i78', 
               'i1206', 
               'i1265', 
               'i1845', 
               'i2472', 
               'i3300', 
               'i3912', 
               'i4698', 
               'i4840', 
               'i4955', 
               'i5422', 
               'i5850', 
               'i6188', 
               'i6595', 
               'i6635', 
               'i6653', 
               'i6989', 
               'i6991', 
               'i7021', 
               'i7579', 
               'i7599', 
               'i7722', 
               'i7819', 
               'i7963', 
               'i7964', 
               'i8033', 
               'i8056', 
               'i8058', 
               'i8060', 
               'i8062', 
               'i8064', 
               'i8067', 
               'i8068', 
               'i8071', 
               'i8208', 
               'i8218', 
               'i8284', 
               'i8287', 
               'i8410', 
               'i8418', 
               'i8524', 
               'i8526', 
               'i8527', 
               'i8531', 
               'i8534', 
               'i8535', 
               'i8536', 
               'i8537', 
               'i8540', 
               'i8541', 
               'i8542', 
               'i8544', 
               'i9030', 
               'i9195', 
               'i9442', 
               'i10123', 
               'i10228', 
               'i10278', 
               'i10380', 
               'i10381', 
               'i10676', 
               'i10739', 
               'i11517', 
               'i11891', 
               'i11893', 
               'i12239', 
               'i12344', 
               'i12553', 
               'i12941', 
               'i12963', 
               'i13000', 
               'i13214', 
               'i13296', 
               'i14223', 
               'i18163', 
               'i18165', 
               'i18177', 
               'i18181', 
               'i18187', 
               'i18193', 
               'i18195', 
               'i18198', 
               'i18208', 
               'i18209', 
               'i18210', 
               'i18248', 
               'i18250', 
               'i18264', 
               'i18302', 
               'i18332', 
               'i18333', 
               'i18350', 
               'i18352', 
               'i18477', 
               'i18578', 
               'i18581', 
               'i18582', 
               'i18694', 
               'i18757', 
               'i18760', 
               'i18761', 
               'i18762', 
               'i18763', 
               'i18764', 
               'i18812', 
               'i18873', 
               'i19191', 
               'i19229', 
               'i19623', 
               'i19691', 
               'i19749', 
               'i20135', 
               'i20838', 
               'i20839', 
               'i21309', 
               'i21658', 
               'i21674'
}



#lgs = [l.language for l in wn.lexicons()]
model_dir = 'models'
lgs = ['en', 'ja', 'de']

def ilis2words(ili_list, lg):
    words = set() 
    for i in ili_list:
        for ss in wn.synsets(ili=i, lang=lg):
            for w in ss.words():
                for f in w.forms():
                    words.add(f)
    return words


for lg in lgs:
    model_name = f"omw-{lg}"
    print(model_name)
    ### make model directory
    mod_path = os.path.join(model_dir, model_name) 
    if not os.path.exists(mod_path):
        os.makedirs(mod_path)


    ### make __init__.py
    open(os.path.join(mod_path,'__init__.py'), 'a').close()
           
    ### make negators
    fh = open(os.path.join(mod_path, 'negators.txt'), 'w')
    for w in sorted(ilis2words(negators, lg)):
        print(w, file=fh)

    ### make intensifiers
    fh = open(os.path.join(mod_path, 'intensifiers.txt'), 'w')
    for w in sorted(ilis2words(intensifiers, lg)):
        print(w, file=fh)

    ### make diminishers
    fh = open(os.path.join(mod_path, 'diminishers.txt'), 'w')
    for w in sorted(ilis2words(diminishers, lg)):
        print(w, file=fh)


    ### make model metadata
    meta = { 'description': f"Model built from omw for {lg}",
             'lang': lg,
             'flags': [] 
    }
    with open(os.path.join(mod_path, 'meta.yml'),'w') as outfile:
            yaml.dump(meta, outfile, default_flow_style=False)

    ### make README        

            


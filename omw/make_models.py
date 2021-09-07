#
# using the OMW create a model
#
import os
import yaml
import wn

#wn.download('pwn:3.0')
#wn.download('omw:1.3')
#wn.download('odenet:1.3')


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
}

diminishers = {'i18163', 'i18581', #barely
}



#lgs = [l.language for l in wn.lexicons()]
model_dir = 'models'
lgs = ['en', 'ja', 'de']

def ilis2words(ili_list, lg):
    words = set() 
    for i in ili_list:
        for ss in wn.synsets(ili=i, lgcode=lg):
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

            


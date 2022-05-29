import logger


agenda = {}



def add_contact(name, number):
    logger.info("Creating new contact...")
    agenda[name] = number
    logger.info("New contact created!")


def search_contact(litere): 
    nume_gasite = [] 
    for nume in agenda:
        if litere in nume:
            nume_gasite.append(nume)
    nume_gasite.sort()
    return nume_gasite


def get_phone_number(name):
    return agenda[name]   


def contact_exists(name):
    if name in agenda:
        return True
    else:
        return False   


def delete_contact(name):
    del agenda[name]             
    
               
            
            
    

  
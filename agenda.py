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
    
               
            
            
    

  
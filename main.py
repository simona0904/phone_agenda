import logger


agenda = {}


def add_contact(name, number):
    logger.info("Creating new contact...")
    agenda[name] = number
    logger.info("New contact created!")
    

def contact_exists(name):
    if name in agenda:
        return True
    else:
        return False    
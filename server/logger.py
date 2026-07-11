import logging 

def setup_logger(name="MedicalAssistant"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)


    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(ch)

    
    return logger


logger=setup_logger()

logger.info("RAG Process Started")
logger.debug("Debugging information: RAG process is in progress.")
logger.error("Error encountered in RAG process: [Error details here]")
logger.critical("Critical issue in RAG process: [Critical details here]")    
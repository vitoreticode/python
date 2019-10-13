import logging
logging.basicConfig(level=logging.INFO, filename="sqrt.log") # DEBUG, INFO, WARN, ERROR

# LAMBDA LOGGER
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# sh = logging.StreamHandler()
# sh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - line %(lineno)s - function %(funcName)s - '
#                                  '%(message)s'))
# logger.addHandler(sh)


def sqrt(x, guess = 1.0):
    if x < 0:
        logging.error("Gor a request for sqrt of negative number")
        raise ValueError
    logging.info("Find sqrt of {} starting with guess {}".format(x, guess))
    if good_enough(guess, x):
        return guess
    else:
        logging.debug("Guess isn't good enough. Improve ...")
        new_guess = improve_guess(guess, x)
        return sqrt(x, new_guess)


def good_enough(guess, x):
    if abs(guess * guess - x) < 0.1:
        return True
    else:
        return False


def avg(a, b):
    return (a + b) / 2.0


def improve_guess(guess, x):
    new_guess = avg(guess, x/guess)
    return new_guess

print(sqrt(36))

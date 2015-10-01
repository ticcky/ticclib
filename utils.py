def init_logging(logger_name):
    import logging
    # Setup logging.
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    logging_format = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    formatter = logging.Formatter(logging_format)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logging.root = logger


def inline_print(string):
    sys.stderr.write('\r\t%s' % (string))
    sys.stderr.flush()


def pdb_on_error():
    import sys

    def info(type, value, tb):
        if hasattr(sys, 'ps1') or not sys.stderr.isatty():
        # we are in interactive mode or we don't have a tty-like
        # device, so we call the default hook
            sys.__excepthook__(type, value, tb)
        else:
            try:
                import ipdb as pdb
            except ImportError:
                import pdb
            import traceback
            # we are NOT in interactive mode, print the exception
            traceback.print_exception(type, value, tb)
            print
            #  then start the debugger in post-mortem mode.
            # pdb.pm() # deprecated
            pdb.post_mortem(tb) # more

    sys.excepthook = info

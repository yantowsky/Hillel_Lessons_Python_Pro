from django.shortcuts import render

import logging

logger = logging.getLogger('app')


def my_view(request):
    logger.debug("DEBUG message")
    logger.info("INFO message")
    logger.warning("WARNING message")
    logger.error("ERROR message")


def home(request):
    return render(request, 'home.html')

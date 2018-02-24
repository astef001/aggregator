from django.core.management import BaseCommand
from django.db import models
from search.models import SearchPlace, Category
import requests
import coloredlogs, logging
from bs4 import BeautifulSoup
import re


logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)


#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "Collect all categories from registered websites"

    # A command must define handle()
    def handle(self, *args, **options):
        search_places = SearchPlace.objects.all()
        for search_place in search_places:
            logger.info("Updating categories for %s" % (search_place.name))
            url = search_place.url
            regex = re.compile("(http(s)?:\/\/[A-Za-z\.\-1-9]*\/?)")
            url = regex.match(url)
            if not url:
                continue;
            url = url.group(0)
            response = requests.get(url,{'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})
            response = response.text
            bs = BeautifulSoup(response, 'html5lib')

            categories = bs.findAll(search_place.category_tag,
                                    {search_place.category_attribute: search_place.category_value})
            for category in categories:
                if search_place.category_tag != 'a':
                    category_links = category.findAll('a')
                    for link in category_links:
                        category_name = link.text.strip()
                        category_link = link.attrs.get('href', "")
                        logger.info("\tUpdating category %s for %s" % (category_name, search_place.name))
                        try:
                            Category.objects.get((models.Q(name=category_name)|
                                                  models.Q(link=category_link))&
                                                  models.Q(search_place=search_place))
                            logger.info("\t\tCategory %s for %s already up to date" % (category_name, search_place.name))
                        except Category.DoesNotExist:
                            logger.warning("\t\tUpdating category %s for %s not found. Creating..." % (category_name, search_place.name))
                            Category.objects.create(name=category_name, search_place=search_place)
                            logger.info("\t\t\tCategory %s for %s created" % (category_name, search_place.name))
            logger.info("Categories for %s updated" % search_place.name)


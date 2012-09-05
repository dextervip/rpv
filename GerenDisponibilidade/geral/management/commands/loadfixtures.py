# -*- encoding: utf-8 -*-

from GerenDisponibilidade import settings
from fixtures import Fixtures

from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "Load fixtures into database"
    def handle_noargs(self, **options):
        f = Fixtures()
        f.load()

        

from django.core.management.base import BaseCommand, CommandError
from tmv_app.models import *
import numpy as np
from sklearn.decomposition import NMF
from scipy.sparse import csr_matrix, find
from functools import partial
from multiprocess import Pool
from utils.db import *
from utils.utils import *
from scoping.models import *
from time import time
import gc, sys
from django.core import management
import pandas as pd
from utils.tm_mgmt import *


class Command(BaseCommand):
    help = 'rerun a dynamic topic model with a different number \
    or dynamic topics'

    def add_arguments(self, parser):
        parser.add_argument('-l','--list', nargs='+', help='<Required> list', required=True)


    def handle(self, *args, **options):

        runs = [int(x) for x in options['list']]

        print(runs)
        runs = RunStats.objects.filter(pk__in=runs)

        stat = runs.first()

        res = compare_topic_queryset(runs)

        ss = res[1]
        res = res[0]

        if runs.count()==1 and runs.first().method=="DT":
            fname = "/tmp/run_compare_{}_windows.xlsx".format(stat.run_id)
        else:
            fname = "/tmp/run_compare_{}_{}.xlsx".format(runs[0],runs[len(runs)-1])

        writer = pd.ExcelWriter(fname, engine='xlsxwriter')

        res.to_excel(writer)

        worksheet = writer.sheets['Sheet1']

        cbase = ord('A')-1
        for i in range(len(ss)):
            n = (i+1)*3-1
            l1 = ''
            if n > 26:
                l1 = chr(cbase+n//26)
            c = l1+chr(cbase+n%26+1)
            r = "{}2:{}{}".format(c,c,len(res))
            print(r)

            worksheet.conditional_format(r, {
                'type': '3_color_scale',
                'min_value': 0,
                'mid_value': 5,
                'max_value': 10,
                'min_type': 'num',
                'mid_type': 'num',
                'max_type': 'num',
            })

        writer.save()

        return(fname)

# -*- coding: utf-8 -*-

import os
import time
import tempfile
import zipfile
import shutil
from celery import Celery
from distutils.dir_util import copy_tree

env=os.environ
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL','redis://localhost:6379'),
CELERY_RESULT_BACKEND = env.get('CELERY_RESULT_BACKEND','redis://localhost:6379')

FONCIER_EXTRACTS_DIR = env.get('FONCIER_EXTRACTS_DIR', '/tmp')
FONCIER_STATIC_DIR = env.get('FONCIER_STATIC_DIR')

taskmanager = Celery('extractions',
                    broker=CELERY_BROKER_URL,
                    backend=CELERY_RESULT_BACKEND)

@taskmanager.task(name='extraction.do')
def do(year, format, proj, email, cities):
    tmpdir = tempfile.mkdtemp(dir = FONCIER_EXTRACTS_DIR, prefix = 'foncier_{0}_{1}_{2}_{3}-'.format(year, format, proj, do.request.id))
    print 'Created temp dir {0}'.format(tmpdir)

    if (FONCIER_STATIC_DIR is not None):
        try:
            copy_tree(FONCIER_STATIC_DIR, tmpdir)
        except IOError as e:
            print 'IOError copying {0} to {1}'.format(FONCIER_STATIC_DIR, tmpdir)

    # TODO: copy geo files in tmpdir here

    # zip file:
    try:
        name = shutil.make_archive(tmpdir, 'tar')
    except IOError as e:
        print 'IOError while zipping {0}'.format(tmpdir)

    # delete directory after zipping:
    shutil.rmtree(tmpdir)
    print 'Removed dir {0}'.format(tmpdir)

    # return zip file
    time.sleep(10)
    return 'done with {0} ! We should now send an email to {1} with a link to {2}'.format(cities, email, name)

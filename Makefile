export DJANGO_SETTINGS_MODULE = tests.settings
export PYTHONPATH := $(shell pwd)


maketranslations:
	cd wagtail_celery_results; django-admin makemessages -a -v2 --keep-pot

compiletranslations:
	cd wagtail_celery_results; django-admin compilemessages

translations:  maketranslations compiletranslations
	@echo "Making and compiling translations"


.PHONY: maketranslations compiletranslations

from django.core.urlresolvers import reverse_lazy


def modify(settings):

    settings['INSTALLED_APPS'] += ('crispy_forms',
                                   'tastypie',
                                   'tinymce',
                                   'django_wysiwyg',
                                   'haystack',
                                   'sorl.thumbnail',
                                   'orb.analytics',
                                   'orb.review',
                                   'orb.partners.OnemCHW',
                                   'django.contrib.humanize',
                                   'modeltranslation',
                                   'modeltranslation_exim',)
    settings['MIDDLEWARE_CLASSES'] += ('orb.middleware.SearchFormMiddleware',)
    settings[
        'TEMPLATE_CONTEXT_PROCESSORS'] += ('orb.context_processors.get_menu',)
    settings[
        'TEMPLATE_CONTEXT_PROCESSORS'] += ('orb.context_processors.get_version',)
    settings[
        'TEMPLATE_CONTEXT_PROCESSORS'] += ('orb.context_processors.base_context_processor',)
    settings['CRISPY_TEMPLATE_PACK'] = 'bootstrap3'
    settings['LOGIN_URL'] = reverse_lazy('profile_login')

    settings['STAGING'] = False

    settings['SHOW_GRAVATARS'] = True
    settings['ORB_GOOGLE_ANALYTICS_CODE'] = 'UA-58593028-1'

    settings['ORB_INFO_EMAIL'] = 'info@mpoweringhealth.org'

    settings['ORB_RESOURCE_DESCRIPTION_MAX_WORDS'] = 150

    settings['ORB_PAGINATOR_DEFAULT'] = 20

    settings['ORB_RESOURCE_MIN_RATINGS'] = 3

    settings['ORB_PARTNER_DATA_ENABLED'] = False

    settings['TASK_UPLOAD_FILE_TYPE_BLACKLIST'] = [u'application/vnd.android']

    settings['TASK_UPLOAD_FILE_MAX_SIZE'] = "5242880"

    settings['DJANGO_WYSIWYG_FLAVOR'] = "tinymce_advanced"

    settings['HAYSTACK_CONNECTIONS'] = {
        'default': {
            'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
            'INCLUDE_SPELLING': True,
            #'URL': 'http://127.0.0.1:8983/solr'
            # ...or for multicore...
            'URL': 'http://127.0.0.1:8983/solr/mpowering',
        }
    }
    settings['HAYSTACK_SIGNAL_PROCESSOR'] = 'haystack.signals.RealtimeSignalProcessor'

    settings['ADVANCED_SEARCH_CATEGORIES'] = [('health_topic', 'health-domain'),
                                              ('resource_type', 'type'),
                                              ('audience', 'audience'),
                                              ('geography', 'geography'),
                                              ('language', 'language'),
                                              ('device', 'device')]

"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import environ  # pip install django-environ

import django
# fix smart_text
django.utils.encoding.smart_text = django.utils.encoding.smart_str
# fix ugettext_lazy
django.utils.translation.ugettext_lazy = django.utils.translation.gettext_lazy
django.utils.translation.ugettext = django.utils.translation.gettext


# Build paths inside the project like this: BASE_DIR / 'subdir'.
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialise environment variables
env = environ.Env(
    # set casting, default value
    ALLOWED_HOSTS=(list, []),
    CSRF_TRUSTED_ORIGINS=(list, []),
    DEBUG=(bool, False),
    RECIPIENTS_EMAIL=(list, []),
    EMAIL_USE_TLS=(bool, True),
)
# environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
# print(DEBUG)

# ALLOWED_HOSTS = ['localhost']
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

if env('CSRF_TRUSTED_ORIGINS'):
    CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS')

POSTGRES_USER=env("POSTGRES_USER")
POSTGRES_PASSWORD=env("POSTGRES_PASSWORD")
POSTGRES_HOST=env("POSTGRES_HOST")
POSTGRES_PORT=env("POSTGRES_PORT")
POSTGRES_DB=env("POSTGRES_DB")
POSTGRES_IS_AVAIL = all([
        POSTGRES_USER, 
        POSTGRES_PASSWORD, 
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DB
])


INSTALLED_APPS = [
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'mptt',
    'djangocms_text_ckeditor',
    'djangocms_link',
    'compressor',
    'django_filters',
    'taggit',
    'taggit_labels',
    "phonenumber_field",
    "captcha",
    'haystack',  # search engine
    # приложение обеспечивающее фоновое обновление 
    # индексов при получении сигналов create/delete объектов
    # https://github.com/django-haystack/celery-haystack
    # НЕ УДАЛОСЬ СОВМЕСТИТЬ С HAYSTACK v3 (а v2 требует джанго меньшей версии)
    # 'celery_haystack',


    # 'cms_search', 
    # 'aldryn_search', NOT WORKING WITH DJANGO > 4.0 ANYMORE

    # 'taggit_autosuggest',
    # #### ALDRYN  you will probably need to add these
    # 'aldryn_apphooks_config',
    # 'aldryn_categories',
    # 'aldryn_common',
    # 'aldryn_newsblog',
    # 'aldryn_people',
    # 'aldryn_translation_tools',
    # 'parler',
    # 'sortedm2m',
    # 'taggit',
    ####

    ### DJANGOCMS BLOG
    # 'filer',
    # 'easy_thumbnails',
    # 'aldryn_apphooks_config',
    # 'parler',
    # 'taggit',
    # 'taggit_autosuggest',
    # 'meta',
    # 'sortedm2m',
    # 'djangocms_blog',
    ############
    'core',
    'background_section',
    'breadcrumbs',
    'colorfield',
    'infoblock',
    'columns',
    'catalog',
    'slider',
    'news',
    # 'djangocms_picture', # использовано в medialer
    # 'djangocms_video', # использовано в medialer
    'medialer',
    'structure',
    'docs',
    'contact',
    # 'cmsplugin_contact'
    # 'django.contrib.postgres',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]


ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'django.template.context_processors.i18n',
        
                'core.context_processors.load_settings', # custom SiteSettings
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if POSTGRES_IS_AVAIL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            'OPTIONS': {
                'options': '-c search_path=ufkis_schema'
            },
            "NAME": POSTGRES_DB,
            "USER": POSTGRES_USER,
            "PASSWORD": POSTGRES_PASSWORD,
            "HOST": POSTGRES_HOST,
            "PORT": POSTGRES_PORT,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'staticfiles/'
STATICFILES_DIRS = [
    # BASE_DIR / "static",
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    'compressor.finders.CompressorFinder',
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = "mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

####### django-cms requires
LANGUAGES = [
    #  ('ru-RU', 'Russian'),
     ('ru', 'Russian'),
    #  ('en', 'English'),
]
# CMS_LANGUAGES = {
#     'default': {
#         'fallbacks': ['ru', 'ru-RU'],
#         'redirect_on_fallback': True,
#         'public': True,
#         'hide_untranslated': False,
#     }
# }
SITE_ID = 1
X_FRAME_OPTIONS = 'SAMEORIGIN'

CMS_TEMPLATES = [
    ('base.html', 'Home page template'),
]

# CMS_ENABLE_HELP = False # off help menu from toolbar
##################

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

META_SITE_PROTOCOL = env('SITE_PROTOCOL')  # set 'http' for non ssl enabled websites
META_USE_SITES = True

META_USE_OG_PROPERTIES=True
META_USE_TWITTER_PROPERTIES=True
META_USE_GOOGLEPLUS_PROPERTIES=True # django-meta 1.x+
META_USE_SCHEMAORG_PROPERTIES=True  # django-meta 2.x+

PARLER_LANGUAGES = {
    # 1: (
    #     {'code': 'ru-RU',},
    #     # {'code': 'en',},
    #     # {'code': 'it',},
    #     # {'code': 'fr',},
    # ),
    'default': {
        'fallbacks': ['ru'],
        # 'fallbacks': ['en', 'it', 'fr'],
    }
}
CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar': 'CMS',
    'skin': 'moono-lisa',
}
CKEDITOR_SETTINGS_POST = {
    'toolbar_HTMLField': [
        [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
        ['Undo', 'Redo'],
        ['cmsplugins', 'cmswidget'],
        ['Find', 'Replace'],
        ['SelectAll'], 
        ['Scayt'],
        ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'HiddenField'],
        ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates'],
        '/',
        ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'], 
        ['CopyFormatting', 'RemoveFormat'],
        ['NumberedList', 'BulletedList'],
        ['Outdent', 'Indent'],
        ['Blockquote', 'CreateDiv'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
        ['BidiLtr', 'BidiRtl', 'Language'],
        ['Link', 'Unlink', 'Anchor'],
        ['CodeSnippet', 'Image2'],
        ['Html5audio', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'],
        '/',
        ['Styles', '-', 'Format', '-', 'Font', '-', 'FontSize'],
        ['TextColor', 'BGColor'],
        ['About'],
        ['Maximize', 'ShowBlocks']
    ]
}

# COMPRESSOR
COMPRESS_ENABLED = False
COMPRESS_CSS_HASHING_METHOD = None
COMPRESS_FILTERS = {
    'css':[
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.rCSSMinFilter',
    ],
    'js':[
        'compressor.filters.jsmin.JSMinFilter',
        # 'compressor.filters.jsmin.CalmjsFilter',
    ]
}
HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = False
############

# TAGGIT
TAGGIT_CASE_INSENSITIVE = True
#######

RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = env('RECAPTCHA_PRIVATE_KEY')
if DEBUG:
    SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')

RECIPIENTS_EMAIL = env('RECIPIENTS_EMAIL')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')


HAYSTACK_CONNECTIONS = {
    'default': {
        # 'ENGINE': 'haystack.backends.elasticsearch7_backend.Elasticsearch7SearchEngine',
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'core.backends.ElasticsearchCustomSearchEngine',
        'URL': env('ELASTICSEARCH_HOST'),
        'INDEX_NAME': 'haystack',
    },
    # 'default': {
    #     'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
    #     'URL': env('SOLR_HOST') + '/solr/tester',                 # Assuming you created a core named 'tester' as described in installing search engines.
    #     'ADMIN_URL': env('SOLR_HOST') + '/solr/admin/cores'
    #     # ...or for multicore...
    #     # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    # },
}
ELASTICSEARCH_DSL={
    'default': {
        'hosts': env('ELASTICSEARCH_DSL_HOSTS')
    },
}
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.BaseSignalProcessor'
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 12
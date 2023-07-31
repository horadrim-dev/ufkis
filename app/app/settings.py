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

# Initialise environment variables
env = environ.Env(
    # set casting, default value
    ALLOWED_HOSTS=(list, []),
    CSRF_TRUSTED_ORIGINS=(list, []),
    DEBUG=(bool, False),

)
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
# print(DEBUG)

# ALLOWED_HOSTS = ['localhost']
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
# print(ALLOWED_HOSTS)
if env('CSRF_TRUSTED_ORIGINS'):
    CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS')

DB_USERNAME=os.environ.get("POSTGRES_USER")
DB_PASSWORD=os.environ.get("POSTGRES_PASSWORD")
DB_HOST=os.environ.get("POSTGRES_HOST")
DB_PORT=os.environ.get("POSTGRES_PORT")
DB_DATABASE=os.environ.get("POSTGRES_DB")
DB_IS_AVAIL = all([
        DB_USERNAME, 
        DB_PASSWORD, 
        DB_HOST,
        DB_PORT,
        DB_DATABASE
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

if DB_IS_AVAIL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DB_DATABASE,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
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

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    # BASE_DIR / "static",
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    'compressor.finders.CompressorFinder',
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

####### django-cms requires
LANGUAGES = [
    #  ('ru', 'Russian') ,
     ('ru-ru', 'Russian') 
]
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
    1: (
        {'code': 'ru-ru',},
        # {'code': 'en',},
        # {'code': 'it',},
        # {'code': 'fr',},
    ),
    'default': {
        'fallbacks': ['ru-ru'],
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
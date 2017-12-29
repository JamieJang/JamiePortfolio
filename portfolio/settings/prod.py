from .common import *

DEBUG = False
ALLOWED_HOSTS = ['*']

# S3를 위한 설정
INSTALLED_APPS += ['storages']
# django-storages 앱 의존성 추가
# 기본 static/media 저장소를 django-storages로 변경 
STATICFILES_STORAGE = 'portfolio.storages.StaticS3Boto3Storage' 
DEFAULT_FILE_STORAGE = 'portfolio.storages.MediaS3Boto3Storage'
# S3 파일 관리에 필요한 최소 설정
# 소스코드에 설정정보를 남기지마세요. 환경변수를 통한 설정 추천
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY'] 
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME'] # 필수 지정
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'ap-northeast-2')
AWS_QUERYSTRING_AUTH = False
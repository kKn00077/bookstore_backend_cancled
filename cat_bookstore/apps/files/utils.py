import os
from uuid import uuid4
from django.utils import timezone

def upload_to_file(instance, filename):

    # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
    ymd_path = timezone.now().strftime('%Y/%m/%d')

    # 길이 32 인 uuid 값
    uuid_name = uuid4().hex

    # 확장자 추출
    extension = os.path.splitext(filename)[-1].lower()

    new_filename = uuid_name+extension

    instance.name = new_filename
    instance.origin_name = filename
    instance.file_type = extension
    instance.size = instance.file.size

    # 결합 후 return
    return '/'.join([
    ymd_path,
    new_filename,
    ])
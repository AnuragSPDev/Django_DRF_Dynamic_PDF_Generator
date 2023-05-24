from io import BytesIO
import uuid

from django.template.loader import get_template
from django.conf import settings

from xhtml2pdf import pisa

def pdf_generator(context:dict):
    '''
    Function to generate pdf file and uploading the same to media directory
    '''
    template = get_template('pdf_generator/data.html')
    html = template.render(context=context)
    response = BytesIO()
    pisa.pisaDocument(BytesIO(html.encode('utf-8')), response)
    file_name = uuid.uuid4()

    try:
        # with open(f'{settings.BASE_DIR}/static/pdf_generator/{file_name}.pdf', 'wb+') as output:
        with open(f'{settings.MEDIA_ROOT}/{file_name}.pdf', 'wb+') as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode('utf-8')), output)
            if pdf.err:
                return '', False
    except Exception as e:
        print(e)

    return file_name, True
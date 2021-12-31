from io import BytesIO
from xhtml2pdf import pisa
from weasyprint import HTML, CSS

from django.http import HttpResponse, FileResponse
from django.template.loader import get_template


MULTI_ITEMS_FIELDS = 'mutual_address therapist_address'.split()

def data_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    context_dict = {k: (context_dict.getlist(k) if k in MULTI_ITEMS_FIELDS else v) for k,v in context_dict.items()}
    html  = template.render(context_dict)
    result = BytesIO()
    HTML(string=html).write_pdf(target=result)
    return result

def some_view(request):
    buffer = data_to_pdf('pdf/bordereau.html', request.GET)
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='result.pdf')

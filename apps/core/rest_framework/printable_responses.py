from django.http import HttpResponse


def word_response(output, filename):
    response = HttpResponse(
        output.getvalue(),
        content_type='application/vnd.openxml'
                     'formats-officedocument.wordprocessingml.document'
    )
    filename = filename.encode()
    response['Content-Disposition'] = b'attachment; filename=' + filename
    return response


def pdf_response(output, filename):
    response = HttpResponse(
        output,
        content_type='application/pdf'
    )
    filename = filename.encode()
    response['Content-Disposition'] = b'attachment; filename=' + filename
    return response

import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from ...models import Aplication, Questionary, Denimi, Sigurimi, QuestionaryNotice, Shendetesore, ShendetesoreNotice, Signature


def pdf_1_ushtar(request, pk):
    """
    Generate a PDF for an 'Aplication' with details, photo, signature and comments.
    """

    # 1. Fetch required objects directly from pk
    aplikimi = get_object_or_404(Aplication, pk=pk)
    questionary = get_object_or_404(Questionary, aplication=aplikimi)
    coments = get_object_or_404(QuestionaryNotice, questionary=questionary)
    punishments = get_object_or_404(Denimi, aplication=aplikimi)
    securements = get_object_or_404(Sigurimi, aplication=aplikimi)
    healthments = get_object_or_404(Shendetesore, aplication=aplikimi)
    health_coment = get_object_or_404(ShendetesoreNotice, shendetesore=healthments)
    signatures = get_object_or_404(Signature, aplication=aplikimi)

    # 2. Helper → convert absolute file path to file:// URI
    def path_to_uri(path):
        return f'file:///{os.path.abspath(path).replace(os.sep, "/")}' if path and os.path.exists(path) else None

    # 3. Define fallback placeholder images
    personal_fallback_image = path_to_uri(os.path.join(settings.BASE_DIR, "static/qpr/img/personal_photo_placeholder.png"))
    id_fallback_image = path_to_uri(os.path.join(settings.BASE_DIR, "static/qpr/img/id_card_placeholder.png"))

    # 4. Resolve file URIs for assets
    header_image_uri = path_to_uri(os.path.join(settings.BASE_DIR, "static/qpr/img/koka_e_shkreses.jpg")) or None
    personal_photo_uri = path_to_uri(aplikimi.personal_photo.path) if getattr(aplikimi, "personal_photo", None) else personal_fallback_image
    id_card_image_uri = path_to_uri(aplikimi.ID_card_image.path) if getattr(aplikimi, "ID_card_image", None) else id_fallback_image
    signature_uri = path_to_uri(aplikimi.signature.signature.path) if getattr(aplikimi, "signature", None) and aplikimi.signature.signature else None

    # 5. Build template context
    context = {
        "info1": aplikimi,
        "info2": questionary,
        "info3": coments,
        "info4": punishments,
        "info5": securements,
        "info6": healthments, 
        "info7": health_coment, 
        "info_100": signatures,
        "is_pdf": True,
        "header_image_uri": header_image_uri,
        "personal_photo_uri": personal_photo_uri,
        "signature_uri": signature_uri,
        "personal_fallback_image": personal_fallback_image,
        "id_card_image_uri": id_card_image_uri,
    }

    # 6. Render HTML from template
    html_string = render_to_string("qpr/detail/detail_1_ushtar.html", context)

    # 7. Load stylesheet
    css_path = os.path.join(settings.BASE_DIR, "static/qpr/css/detail.css")
    css = CSS(filename=css_path)

    # 8. Generate PDF
    pdf_file = HTML(string=html_string, base_url=settings.BASE_DIR).write_pdf(stylesheets=[css])

    # 9. Return as response
    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="ushtar_{pk}.pdf"'
    return response

# Create your views here.
from django.shortcuts import render, render_to_response, get_object_or_404
from medias.models import Disciplina
from forms import FormDisciplina
from django.template import RequestContext
from django import http
from django.template.loader import get_template
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi, os

def index(request):
    return render_to_response('index.html', {
        'disciplinas': Disciplina.objects.all()
    })


def disciplina(request, id_disciplina):
    disciplina = get_object_or_404(Disciplina, pk=id_disciplina)
    if request.method == "POST":
        form = FormDisciplina(request.POST, request.FILES, instance=disciplina)
        if (form.is_valid()):
            salvar = form.save(commit=False)
            salvar.save()
            return render(request, "confirmacao.html", {})
    else:
        form = FormDisciplina(instance=disciplina)

    return render_to_response("disciplina.html", locals(), context_instance=RequestContext(request))


def excluir(request, id_disciplina):
    disciplina = get_object_or_404(Disciplina, pk=id_disciplina)
    if(request.method == "POST"):
        disciplina.delete()
        return render(request, "excluido.html", {})
    return render(request, "excluir.html", locals(), context_instance=RequestContext(request))

def adicionar(request):
    if request.method == "POST":
        form = FormDisciplina(request.POST, request.FILES)
        if form.is_valid():
            salvar = form.save(commit=False)
            salvar.save()
            return render(request, "confirmacao.html", {})
    else:
        form = FormDisciplina()
    return render(request, "adicionar.html", locals(), context_instance=RequestContext(request))


def write_to_pdf(template_src, context_dict, filename):
    # Create the HttpResponse object with the appropriate PDF headers.
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="notas.pdf"'
    #
    # # Create the PDF object, using the response object as its "file."
    # p = canvas.Canvas(response)
    #
    # # Draw things on the PDF. Here's where the PDF generation happens.
    # # See the ReportLab documentation for the full list of functionality.
    # p.drawCentredString(10, 10, "Relatorio de Notas")
    #
    # # Close the PDF object cleanly, and we're done.
    # p.showPage()
    # p.save()
    # return response
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        response = http.HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
        response.write(result.getvalue())
        return response
    return http.HttpResponse('Problema ao gerar PDF: %s' % cgi.escape(html))

def gerarpdf(request):
    disciplinas = Disciplina.objects.all()
    return write_to_pdf('templatepdf.html', {'disciplinas': disciplinas}, 'relatorio_notas')

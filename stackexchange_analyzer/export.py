import json
from jinja2 import Template

HTML_TEMPLATE_PATH = 'stackexchange_analyzer/templates/result.html'


def export_to_json(result, export_path):
    with open(export_path, 'w') as export_file:
        export_file.write(json.dumps(result))


def export_to_html(result, export_path):
    with open(HTML_TEMPLATE_PATH) as template_file:
        template = Template(template_file.read())
    rendered_html = template.render(questions=result)
    with open(export_path, 'w') as export_file:
        export_file.write(rendered_html)

import logging
from fastapi.responses import HTMLResponse
from servicefoundry.service import fastapi

logger = logging.getLogger(__name__)

app = fastapi.app()


@app.get("/", response_class=HTMLResponse)
def root():
    html_content = f"""
    <html>
        <body>
            Open <a href="/docs">Docs</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

try:
    import ${module_name}
% for function in functions:
    app.add_api_route("/${function}", ${module_name}.${function}, methods=["POST"])
% endfor
except ImportError as error:
    print("Failed to import function ${function}: " + error.message)
    raise error

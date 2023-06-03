import json

from rest_framework.renderers import JSONRenderer


class GlobalJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code
        message = renderer_context["kwargs"].get("message")
        if status_code < 400 and "next" not in data and "previous" not in data:
            return json.dumps({"success": True, "message": message, "data": data})
        else:
            return super(GlobalJSONRenderer, self).render(data)

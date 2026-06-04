from http.server import BaseHTTPRequestHandler
import json

from workflows.research_workflow import run_workflow


class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "application/json"
        )
        self.end_headers()

        response = {
            "status": "success",
            "message": "Multi-Agent Research Assistant API is running"
        }

        self.wfile.write(
            json.dumps(response).encode()
        )

    def do_POST(self):

        try:

            content_length = int(
                self.headers["Content-Length"]
            )

            body = self.rfile.read(
                content_length
            )

            data = json.loads(body)

            topic = data.get("topic")

            report = run_workflow(topic)

            response = {
                "report": report
            }

            self.send_response(200)

        except Exception as e:

            response = {
                "error": str(e)
            }

            self.send_response(500)

        self.send_header(
            "Content-Type",
            "application/json"
        )
        self.end_headers()

        self.wfile.write(
            json.dumps(response).encode()
        )
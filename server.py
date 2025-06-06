#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

# Change to the directory containing the HTML file
os.chdir('/workspace/linuxem')

PORT = 12000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('X-Frame-Options', 'ALLOWALL')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Server running at http://0.0.0.0:{PORT}/")
        print(f"Access the report viewer at: http://0.0.0.0:{PORT}/enhanced_report_viewer.html")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            sys.exit(0)
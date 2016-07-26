import SimpleHTTPServer
import SocketServer
import requests
import json

PORT = 8080

USER_EMAIL      = "elizabethwbiddlecome@gmail.com"
USER_API_KEY    = "3fe1260c-026e-47df-a038-9a47e46b4c13"
DRONE_NAME      = 'bobby'

def getLiveData():
	url = 'http://cloud.dronesmith.io/api/drone/' + DRONE_NAME + '/live'

	headers = {
		'user-email': 	USER_EMAIL,
		'user-key': 	USER_API_KEY,
		'Content-Type':	'application/json'
	}

	response = requests.get(url, headers=headers)
	print 'Status code:', response

	jsonText = json.loads(response.text)
	print 'Text:', jsonText

	return jsonText['telemetry']

print getLiveData
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("localhost", PORT), Handler)

# class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

#     def getLiveData(self):
#         url = 'http://cloud.dronesmith.io/api/drone/' + DRONE_NAME + '/live'

#         headers = {
#             'user-email':       USER_EMAIL,
#             'user-key':         USER_API_KEY,
#             'Content-Type':     'application/json'
#         }

#         response = requests.get(url, headers=headers)
#         jsonText = json.loads(response.text)
#         return jsonText['telemetry']

#     def do_GET(self):
        
#         if self.path == '/gps':
#             self.send_response(200)
#             self.send_header('Content-type','text/json')
#             self.send_header("Access-Control-Allow-Origin", "*")
#             self.end_headers()

#             data = self.getLiveData()

#             r = {
#              'lat': data['GLOBAL_POSITION_INT']['lat'],
#              'lon': data['GLOBAL_POSITION_INT']['lon'],
#              'intensity': data['PAYLOAD']['rads']
#             }

#             self.wfile.write(json.dumps(r))
#             return
#         else:
#         	SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

# httpd = SocketServer.ThreadingTCPServer(('localhost', PORT), CustomHandler)

print "Listening on", PORT
httpd.serve_forever()


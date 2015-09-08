# -*- coding: utf-8 -*-
from oauth2client.client import OAuth2WebServerFlow, OAuth2Credentials
import httplib2
import json
import pprint as pp
import xml.dom.minidom
# The client id and secret can be found on your API Console.
CLIENT_ID = '459859438108-4jga6shmfe39c62q2gduah09aguii7bn.apps.googleusercontent.com'
CLIENT_SECRET = '31AtJ3ZKGtXU0xDEJZjnW8ty'
SCOPES = ['https://docs.google.com/feeds/', 'https://spreadsheets.google.com/feeds']
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"

flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                           client_secret=CLIENT_SECRET,
                           scope=SCOPES,
                           redirect_uri=REDIRECT_URI)
if False:
    auth_uri = flow.step1_get_authorize_url()
    print auth_uri
    exit()
    # http_get_code = httplib2.Http()
    # code = http_get_code.request(auth_uri, "GET")

if False:
    code = '4/Q5jFFYP9hxU7G5JZlJ5UG3ZB4iAoaGB0Il9Ilx8DdEg'
    credentials = flow.step2_exchange(code)
    print credentials.to_json()

class Cells:

    def getCells(self):
        http = httplib2.Http()
        # url = "https://spreadsheets.google.com/feeds/spreadsheets/private/full/"
        # url = "https://spreadsheets.google.com/feeds/list/key/"+ sheet_id+ "/private/full"
        # This URL BELOW HAS THE CELL BASED FEED
        # url = "https://spreadsheets.google.com/feeds/worksheets/1xIwPItf_qYQDzcfwAHx9-a2LNLQpj_pdfq-cO4nAeyM/private/full"
        # url = url + sheet_id

        sheet_id ="1xIwPItf_qYQDzcfwAHx9-a2LNLQpj_pdfq-cO4nAeyM"
        access_token = "ya29.6AFN4RML0WD9MnJsLh55pYTWzBd4pqbZwRmTnfLoZWCEwWONvmbrwNndX6wCKL6US8FF"
        url = "https://spreadsheets.google.com/feeds/list/1xIwPItf_qYQDzcfwAHx9-a2LNLQpj_pdfq-cO4nAeyM/od6/private/full"
        url = url + "?access_token=" + access_token

        id ="1xIwPItf_qYQDzcfwAHx9-a2LNLQpj_pdfq-cO4nAeyM"
        resp, content = http.request(url, "GET")
        # print resp
        # print content
        test_data = {"test-key":"test-val"}
        return  json.dumps(test_data)
        return content

        # print ''
        # xml = xml.dom.minidom.parseString(content)
        # pretty_xml_as_string = xml.toprettyxml()
        # # pp.pprint('content: {0}'.format(content))
        # return pretty_xml_as_string

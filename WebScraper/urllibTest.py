import urllib.request

#URL of the web page to fetch
url = 'https://www.example.com'

try:
    response = urllib.request.urlopen(url)
    data = response.read()

    # Decode the data (if it isn't in bytes) to a string
    html_content = data.decode('utf-8')

    #Print the HTML content of the web page
    print(html_content)

except Exception as e:
    print("Error fetching URL: ", e)
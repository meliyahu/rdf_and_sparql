# filename: ex358.py
# Send SPARQL query to SPARQL endpoint, store and output result.

from urllib.parse import quote 
import urllib.request as request 

endpointURL = "http://dbpedia.org/sparql"
query = """
SELECT ?elvisbday WHERE {
  <http://dbpedia.org/resource/Elvis_Presley>
  <http://dbpedia.org/property/dateOfBirth> ?elvisbday .
}
"""
escapedQuery = quote(query)
requestURL = endpointURL + "?query=" + escapedQuery
with request.urlopen(requestURL) as f:
  print(f.read().decode('utf-8'))


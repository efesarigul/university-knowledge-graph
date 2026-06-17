from pyshacl import validate

results = validate(
    data_graph=r"C:\Users\sarig\Desktop\knowladge engineering\Proje\university-knowledge-graph-v2.rdf",
    shacl_graph=r"C:\Users\sarig\Desktop\knowladge engineering\Proje\sphal_deneme\shacl-shapes.ttl",
    data_graph_format="turtle",
    shacl_graph_format="turtle",
    inference="rdfs",
    debug=False
)

conforms, results_graph, results_text = results
print("Conforms:", conforms)
print(results_text)
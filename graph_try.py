from rdflib import Graph

g = Graph()
g.parse("university-knowledge-graph-v2.rdf", format="turtle")

print(f"Total triples loaded: {len(g)}")

# Tüm triple'ları listele (ilk 10)
for i, (s, p, o) in enumerate(g):
    if i >= 10:
        break
    print(f"{s} | {p} | {o}")
# 🏛️ University Knowledge Graph System

This repository contains the complete implementation of the **University Knowledge Graph** project developed for the *Knowledge Engineering and Ontologies* course.The project structurally models, validates, and queries the academic ecosystem of the **Manisa Celal Bayar University (MCBU) Engineering Faculty**, focusing on the Computer, Industrial, and Mechanical Engineering departments.

---

## 🎯 Project Objective

The primary objective of this project is to resolve the challenge of fragmented and siloed academic data across university faculties. By designing a unified Semantic Web application, this system:
* **Formalizes the Domain:** Captures complex relationships between students, academic staff (professors and research assistants), courses (mandatory and elective), and academic sub-fields using an OWL 2 ontology.
* **Ensures Data Integrity:** Employs SHACL shapes to validate essential business constraints, such as mandatory student IDs and departmental affiliations.
* **Enables Intelligent Querying:** Leverages SPARQL for logical reasoning and automated deduction (e.g., transitive prerequisite chains).
* **Integrates Large Language Models (LLMs):** Bridges the gap between natural language and structured query logic by translating user questions into ontology-grounded SPARQL queries using the Claude API, drastically minimizing AI hallucinations.

---

## 📊 Dataset Sources

]Rather than relying on static or synthetic datasets, real-time data extraction was implemented to reflect the authentic academic ecosystem of the faculty:
1. **MCBU Course Information System:** Used to scrape course codes, names, semester data, and multi-tier prerequisite chains.
2. **AVESIS (Academic Data Management System):** Used to extract academic staff attributes, including titles, institutional email addresses, and official profile URLs.

*Note: Data was collected using an automated Python pipeline leveraging **Selenium** for dynamic content handling and **BeautifulSoup** for HTML parsing, cleaned with **Pandas**, and mapped to the structural schema (TBox) to generate 1,977 RDF triples.*

---

## 📂 Repository Structure

The repository is organized as follows to fulfill all semantic web and deployment constraints:

```text
├── ontology/
│   └── university-knowledge-graph-v2.rdf  # Core OWL ontology file (Turtle format)
├── shacl/
│   └── shacl-shapes.ttl                   # SHACL constraints for data validation
├── queries/
│   ├── query1_software_staff.sparql       # SPARQL query for sub-field staff retrieval
│   ├── query2_transitive_prereq.sparql    # SPARQL query testing transitive prerequisites
│   ├── query3_professor_emails.sparql     # SPARQL query for professor contact details
│   └── query4_student_enrollments.sparql  # SPARQL query for per-student schedules
├── src/
│   ├── scraper.py                         # Python automation script (Selenium & BeautifulSoup)
│   ├── rdf_mapper.py                      # Relational CSV-to-RDF triple generator
│   ├── validator.py                       # pySHACL validation engine script
│   └── llm_interface.py                   # Claude API Natural Language to SPARQL pipeline
├── docs/                                  # WIDOCO automated ontology documentation
│   └── index.html                         # Interactive visualization and documentation
└── README.md                              # Project documentation overview


```

### 1. Running Data Validation (SHACL)

To test data integrity and see the validation constraints in action (including the intentional validation failure of the incomplete `:wrong_student` record):

```bash
python src/validator.py

```

### 2. Executing SPARQL Queries Programmatically

You can run the predefined SPARQL queries on the loaded Turtle memory graph:

```bash
python src/rdf_mapper.py

```

*Alternatively, you can open `ontology/university-knowledge-graph-v2.rdf` in **Protégé** or **GraphDB** to execute queries directly inside their respective SPARQL Query tabs.*

### 3. Running the LLM Integration (Natural Language Interface)

To launch the semantic natural language interface using Claude Sonnet, make sure to export your API key first:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
python src/llm_interface.py

```

---

## 👥 Team Members

This project was developed collaboratively by:
 
**Efe Şamil Sarıgül** 

**Ayça Selda Keskin** 



---

For a detailed look into the TBox/ABox conceptual decisions, axiom justifications, and technical outputs, please explore the interactive documentation inside the `docs/` folder or read our full project report.# university-knowledge-graph

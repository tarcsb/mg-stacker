import spacy

def parse_user_input(input_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_text)
    parsed_data = {
        "performance": [],
        "visual_elements": [],
        "data_sources": [],
        "compliance_standards": [],
        "stakeholders": [],
        "file_types": [],
        "misc": []
    }
    for ent in doc.ents:
        if ent.label_ == "PERFORMANCE":
            parsed_data["performance"].append(ent.text)
        elif ent.label_ == "VISUAL":
            parsed_data["visual_elements"].append(ent.text)
        elif ent.label_ == "DATA":
            parsed_data["data_sources"].append(ent.text)
        elif ent.label_ == "COMPLIANCE":
            parsed_data["compliance_standards"].append(ent.text)
        elif ent.label_ == "STAKEHOLDER":
            parsed_data["stakeholders"].append(ent.text)
        elif ent.label_ == "FILE":
            parsed_data["file_types"].append(ent.text)
        else:
            parsed_data["misc"].append(ent.text)
    return parsed_data

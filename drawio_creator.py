# drawio_creator.py (versão corrigida)

import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

class DrawioCreator:
    def __init__(self, entities, output_folder="outputs"):
        self.entities = entities
        self.output_folder = output_folder

    def generate_drawio_xml(self):
        # Base structure for Draw.io file
        mxfile = Element('mxfile', host="app.diagrams.net")
        diagram = SubElement(mxfile, 'diagram', name="API Diagram")
        mxGraphModel = SubElement(diagram, 'mxGraphModel')
        root = SubElement(mxGraphModel, 'root')

        # Required base cells for Draw.io
        SubElement(root, 'mxCell', id="0")
        SubElement(root, 'mxCell', id="1", parent="0")

        # Create boxes for each entity
        x_position = 20
        y_position = 20

        for idx, entity in enumerate(self.entities, start=2):
            cell_id = str(idx)
            mxCell = SubElement(root, 'mxCell', id=cell_id, value=entity['name'], style="rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", vertex="1", parent="1")
            mxGeometry = SubElement(mxCell, 'mxGeometry', x=str(x_position), y=str(y_position), width="160", height="60")
            mxGeometry.set('as', 'geometry')

            # Update position for next entity
            x_position += 200
            if x_position > 800:
                x_position = 20
                y_position += 100

        xml_str = tostring(mxfile, encoding="utf-8")
        pretty_xml = parseString(xml_str).toprettyxml(indent="  ")
        return pretty_xml

    def save_drawio_file(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        xml_content = self.generate_drawio_xml()
        filepath = os.path.join(self.output_folder, "api_diagram.drawio")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml_content)

        print(f"Draw.io diagram saved at {filepath}")
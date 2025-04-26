# drawio_creator.py (versão melhorada - entidades + métodos + endpoints)

import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

class DrawioCreator:
    def __init__(self, entities, output_folder="outputs"):
        self.entities = entities
        self.output_folder = output_folder

    def generate_drawio_xml(self):
        mxfile = Element('mxfile', host="app.diagrams.net")
        diagram = SubElement(mxfile, 'diagram', name="API Diagram")
        mxGraphModel = SubElement(diagram, 'mxGraphModel')
        root = SubElement(mxGraphModel, 'root')

        SubElement(root, 'mxCell', id="0")
        SubElement(root, 'mxCell', id="1", parent="0")

        x_position = 20
        y_position = 20

        for idx, entity in enumerate(self.entities, start=2):
            cell_id = str(idx)

            # Montar o conteúdo da caixa (nome da entidade + métodos)
            content = f"<b>{entity['name']}</b><br>"
            for action in entity['actions']:
                action = action.lower()
                endpoint = self.map_action_to_endpoint(action, entity['name'])
                content += f"+ {action.upper()} {endpoint}<br>"

            mxCell = SubElement(root, 'mxCell', id=cell_id, value=content, style="shape=swimlane;rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", vertex="1", parent="1")
            mxGeometry = SubElement(mxCell, 'mxGeometry', x=str(x_position), y=str(y_position), width="200", height="160")
            mxGeometry.set('as', 'geometry')

            # Atualizar posição para próxima entidade
            x_position += 250
            if x_position > 1000:
                x_position = 20
                y_position += 200

        xml_str = tostring(mxfile, encoding="utf-8")
        pretty_xml = parseString(xml_str).toprettyxml(indent="  ")
        return pretty_xml

    def map_action_to_endpoint(self, action, entity_name):
        entity_path = entity_name.lower()
        if action == "create":
            return f"POST /{entity_path}/"
        elif action == "read":
            return f"GET /{entity_path}/"
        elif action == "update":
            return f"PUT /{entity_path}/{{id}}"
        elif action == "delete":
            return f"DELETE /{entity_path}/{{id}}"
        elif action == "upload":
            return f"POST /{entity_path}/upload"
        elif action == "download":
            return f"GET /{entity_path}/download"
        elif action == "generate":
            return f"POST /{entity_path}/generate"
        elif action == "view":
            return f"GET /{entity_path}/view"
        elif action == "send":
            return f"POST /{entity_path}/send"
        elif action == "analyze":
            return f"POST /{entity_path}/analyze"
        else:
            return f"/{entity_path}/"

    def save_drawio_file(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        xml_content = self.generate_drawio_xml()
        filepath = os.path.join(self.output_folder, "api_diagram.drawio")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml_content)

        print(f"Draw.io diagram saved at {filepath}")
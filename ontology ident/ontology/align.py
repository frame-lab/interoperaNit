import textdistance
import numpy as np


class Align:
    def __init__(self, ontos):
        self.ontos = ontos

    def make_print(self, result):
        file = open(f'./results/ontology_result.txt', "w+")
        file.writelines(str(result))

    def make_domains(self):
        domains = []
        for onto in self.ontos:

            new_domain = False
            new_entities = False
            is_entities = False

            domain = {
                "domain_name": "",
                "domain_parameter": [],
                "entities": [],
            }

            for line in onto:
                if 'CREATE TABLE IF NOT EXISTS ' in line:
                    words = line.split(' ')
                    domain["domain_name"] = words[5].replace("\"", "")
                    new_domain = True

                elif ";" in line and new_domain:
                    new_domain = False
                    new_entities = True

                elif new_domain:
                    words = line.split(' ')
                    domain["domain_parameter"].append(
                        words[0].replace("\"", "").replace("\t", ""))

                elif new_entities and f'INSERT INTO \"${domain["domain_name"]}\"':
                    is_entities = True
                    new_entities = False

                elif ";" in line and is_entities:
                    is_entities = False

                elif is_entities:
                    words = line.split(", ")
                    domain["entities"].append(words)

            domains.append(domain)
            print(domain)


    def align(self):
        self.make_domains()

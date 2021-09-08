import textdistance
import numpy as np


class Align:
    def __init__(self, ontos):
        self.ontos = ontos

    def make_files(self, domains):
        for domain in domains:
            file = open(f'./results/{domain["domain_name"]}.sql', "w+")

            file.write(
                f'CREATE TABLE IF NOT EXISTS "{domain["domain_name"]}" (\n')

            for parameter in domain["domain_parameters"]:
                separator = " "
                file.write(
                    f'\t"{parameter["parameter"]}" {separator.join(parameter["type"])},\n')

            file.write(");\n\n")

            separator = ", "
            parameters = [f'"{parameter["parameter"]}"'
                          for parameter in domain["domain_parameters"]]
            file.write(
                f'INSERT INTO "{domain["domain_name"]}" ({separator.join(parameters)}) VALUES\n')

            last_entity = domain["entities"][-1]
            for entity in domain["entities"]:
                file.write(
                    f'\t({separator.join(entity)}),\n')

            file.write(f'\t({separator.join(last_entity)});\n')

    def make_domains(self):
        domains = []
        for onto in self.ontos:

            new_domain = False
            new_entities = False
            is_entities = False

            domain = {
                "domain_name": "",
                "domain_parameters": [],
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
                    domain_parameter = {
                        "parameter": words.pop(0).
                        replace("\t", "").
                        replace('"', ""),
                        "type": [word.
                                 replace(",", "").
                                 replace("\n", "") for word in words]
                    }
                    domain["domain_parameters"].append(domain_parameter)

                elif ";" in line and is_entities:
                    is_entities = False
                    domains.append(domain)
                    domain = {
                        "domain_name": "",
                        "domain_parameters": [],
                        "entities": [],
                    }

                elif new_entities and f'INSERT INTO \"{domain["domain_name"]}\"' in line:
                    is_entities = True
                    new_entities = False

                elif is_entities:
                    words = line.split(", ")
                    entity = [word.
                              replace("(", "").
                              replace("\t", "").
                              replace("),\n", "").
                              replace("'", "") for word in words]
                    domain["entities"].append(entity)
        return domains

    def align(self):
        domains = self.make_domains()

        self.make_files(domains)

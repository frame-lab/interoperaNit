from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
sigma_app = gateway.entry_point
print(sigma_app.getWords("Virus"))

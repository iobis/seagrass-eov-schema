from frictionless import validate

report = validate("datapackage.json")

if report.valid:
    print("The Data Package is valid!")
else:
    print("The Data Package has errors:", report.flatten(["code", "message"]))

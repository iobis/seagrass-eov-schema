from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin, RecommendedSlotsPlugin

validator = Validator(
    schema="seagrass.yaml",
    validation_plugins=[
        JsonschemaValidationPlugin(closed=True),
        RecommendedSlotsPlugin()
    ]
)
report = validator.validate({"eventID": "sample_1", "decimalLongitude": "a", "decimalLatitude": 51.3}, "Event")
print(report)

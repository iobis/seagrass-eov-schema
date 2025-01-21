# Seagrass EOV schema
## Validation

```bash
# for JSON data
linkml validate --target-class SeagrassContainer --schema linkml/seagrass.yaml data/data.json

# for CSV data
linkml validate --target-class Event --schema linkml/seagrass.yaml data/event.csv
linkml validate --target-class Occurrence --schema linkml/seagrass.yaml data/occurrence.csv

# not picking up CSV issues with scientificNameID?
linkml validate --config linkml/seagrass-validation.yaml
```

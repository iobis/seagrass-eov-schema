# Seagrass EOV schema

## LinkML
### Validation

```bash
linkml validate --config linkml/seagrass-validation.yaml
```

### Template generation

```bash
gen-excel linkml/seagrass.yaml --output seagrass_template.xlsx
```

### Docs generation

```bash
# gen-doc throwing an error for now
gen-markdown -d docs linkml/seagrass.yaml
```

## Frictionless Data Package

```bash
frictionless validate datapackage.json
```
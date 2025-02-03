# Seagrass EOV schema

<https://iobis.github.io/seagrass-eov-schema/>

## Validation

```bash
frictionless validate datapackage.json
```

```
                        dataset                        
┏━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ name         ┃ type  ┃ path                ┃ status ┃
┡━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ events       │ table │ data/event.csv      │ VALID  │
│ occurrences  │ table │ data/occurrence.csv │ VALID  │
│ measurements │ table │ data/mof.csv        │ VALID  │
└──────────────┴───────┴─────────────────────┴────────┘
```
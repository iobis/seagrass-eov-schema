# Seagrass EOV schema

The Seagrass EOV schema represents the publishing data model for Seagrass EOV datasets into global biodiversity infrastructures. It intends to be the schema where all Seagrass EOV datasets can be transformed into regardless of the data collection protocol and data entry format.

The data schema is described as a [Frictionless Data Package](https://datapackage.org/), compatible with the Darwin Core Archive format used by infrastructures such as OBIS and GBIF. The Data Package documentation is available in a human readable format at <https://iobis.github.io/seagrass-eov-schema/>.

## Example dataset

An example dataset is included as CSV in the `data` folder. The expected structure of this dataset is described in `package.json`. To validate the example dataset, install [frictionless-py](https://github.com/frictionlessdata/frictionless-py) and run `frictionless validate datapackage.json`.

```bash
% frictionless validate datapackage.json

─────────────────────── Dataset ───────────────────────
                        dataset                        
┏━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ name         ┃ type  ┃ path                ┃ status ┃
┡━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ events       │ table │ data/event.csv      │ VALID  │
│ occurrences  │ table │ data/occurrence.csv │ VALID  │
│ measurements │ table │ data/mof.csv        │ VALID  │
└──────────────┴───────┴─────────────────────┴────────┘
```
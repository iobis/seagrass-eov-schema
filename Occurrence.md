
# Class: Occurrence



URI: [https://github.com/iobis/seagrass-eov-schema/Occurrence](https://github.com/iobis/seagrass-eov-schema/Occurrence)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Event]<eventID%201..1-%20[Occurrence&#124;occurrenceID:string;scientificName:string;basisOfRecord:string;occurrenceStatus:string;scientificNameID:string;class:string%20%3F;family:string%20%3F;genus:string%20%3F;identifiedBy:string%20%3F;kingdom:string%20%3F;order:string%20%3F;phylum:string%20%3F;recordedBy:string%20%3F;taxonRank:string%20%3F;vernacularName:string%20%3F],[MeasurementOrFact]-%20occurrenceID%201..1>[Occurrence],[SeagrassDataset]++-%20occurrences%200..*>[Occurrence],[SeagrassDataset],[MeasurementOrFact],[Event])](https://yuml.me/diagram/nofunky;dir:TB/class/[Event]<eventID%201..1-%20[Occurrence&#124;occurrenceID:string;scientificName:string;basisOfRecord:string;occurrenceStatus:string;scientificNameID:string;class:string%20%3F;family:string%20%3F;genus:string%20%3F;identifiedBy:string%20%3F;kingdom:string%20%3F;order:string%20%3F;phylum:string%20%3F;recordedBy:string%20%3F;taxonRank:string%20%3F;vernacularName:string%20%3F],[MeasurementOrFact]-%20occurrenceID%201..1>[Occurrence],[SeagrassDataset]++-%20occurrences%200..*>[Occurrence],[SeagrassDataset],[MeasurementOrFact],[Event])

## Referenced by Class

 *  **[MeasurementOrFact](MeasurementOrFact.md)** *[MeasurementOrFact➞occurrenceID](MeasurementOrFact_occurrenceID.md)*  <sub>1..1</sub>  **[Occurrence](Occurrence.md)**
 *  **None** *[➞occurrences](seagrassDataset__occurrences.md)*  <sub>0..\*</sub>  **[Occurrence](Occurrence.md)**

## Attributes


### Own

 * [Occurrence➞eventID](Occurrence_eventID.md)  <sub>1..1</sub>
     * Range: [Event](Event.md)
 * [Occurrence➞occurrenceID](Occurrence_occurrenceID.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [scientificName](scientificName.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [basisOfRecord](basisOfRecord.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [occurrenceStatus](occurrenceStatus.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [scientificName](scientificName.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [scientificNameID](scientificNameID.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [class](class.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [family](family.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [genus](genus.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [identifiedBy](identifiedBy.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [kingdom](kingdom.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [order](order.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [phylum](phylum.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [taxonRank](taxonRank.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [vernacularName](vernacularName.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | http://rs.tdwg.org/dwc/terms/Occurrence |

# Class: MeasurementOrFact



URI: [https://github.com/iobis/seagrass-eov-schema/MeasurementOrFact](https://github.com/iobis/seagrass-eov-schema/MeasurementOrFact)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Occurrence],[Occurrence]<occurrenceID%201..1-%20[MeasurementOrFact&#124;measurementID:string;measurementType:MeasurementTypeType;measurementUnit:string;measurementValue:string;measurementAccuracy:string%20%3F;measurementDeterminedBy:string%20%3F;measurementDeterminedDate:date%20%3F;measurementMethod:string%20%3F;measurementTypeID:string%20%3F;measurementUnitID:string%20%3F;measurementValueID:string%20%3F;sampleSizeUnit:string%20%3F;sampleSizeValue:float%20%3F],[Event]<eventID%201..1-%20[MeasurementOrFact],[SeagrassContainer]++-%20mof%200..*>[MeasurementOrFact],[SeagrassContainer],[Event])](https://yuml.me/diagram/nofunky;dir:TB/class/[Occurrence],[Occurrence]<occurrenceID%201..1-%20[MeasurementOrFact&#124;measurementID:string;measurementType:MeasurementTypeType;measurementUnit:string;measurementValue:string;measurementAccuracy:string%20%3F;measurementDeterminedBy:string%20%3F;measurementDeterminedDate:date%20%3F;measurementMethod:string%20%3F;measurementTypeID:string%20%3F;measurementUnitID:string%20%3F;measurementValueID:string%20%3F;sampleSizeUnit:string%20%3F;sampleSizeValue:float%20%3F],[Event]<eventID%201..1-%20[MeasurementOrFact],[SeagrassContainer]++-%20mof%200..*>[MeasurementOrFact],[SeagrassContainer],[Event])

## Referenced by Class

 *  **None** *[➞mof](seagrassContainer__mof.md)*  <sub>0..\*</sub>  **[MeasurementOrFact](MeasurementOrFact.md)**

## Attributes


### Own

 * [MeasurementOrFact➞eventID](MeasurementOrFact_eventID.md)  <sub>1..1</sub>
     * Range: [Event](Event.md)
 * [MeasurementOrFact➞occurrenceID](MeasurementOrFact_occurrenceID.md)  <sub>1..1</sub>
     * Range: [Occurrence](Occurrence.md)
 * [measurementID](measurementID.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [measurementType](measurementType.md)  <sub>1..1</sub>
     * Range: [MeasurementTypeType](MeasurementTypeType.md)
 * [measurementUnit](measurementUnit.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [measurementValue](measurementValue.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [measurementAccuracy](measurementAccuracy.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [measurementDeterminedBy](measurementDeterminedBy.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [measurementDeterminedDate](measurementDeterminedDate.md)  <sub>0..1</sub>
     * Range: [Date](types/Date.md)
 * [measurementMethod](measurementMethod.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [measurementTypeID](measurementTypeID.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [measurementUnitID](measurementUnitID.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [measurementValueID](measurementValueID.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [sampleSizeUnit](sampleSizeUnit.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [sampleSizeValue](sampleSizeValue.md)  <sub>0..1</sub>
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | http://rs.iobis.org/obis/terms/ExtendedMeasurementOrFact |
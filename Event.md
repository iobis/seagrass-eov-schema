
# Class: Event



URI: [https://github.com/iobis/seagrass-eov-schema/Event](https://github.com/iobis/seagrass-eov-schema/Event)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Occurrence],[MeasurementOrFact],[MeasurementOrFact]-%20eventID%201..1>[Event&#124;eventID:string;decimalLongitude:float;decimalLatitude:float;eventDate:date;footprintSRS:string%20%3F;footprintWKT:string%20%3F;bibliographicCitation:string%20%3F;coordinateUncertaintyInMeters:float%20%3F;country:string%20%3F;datasetID:string%20%3F;datasetName:string%20%3F;fieldNotes:string%20%3F;geodeticDatum:string%20%3F;habitat:string%20%3F;institutionCode:string%20%3F;institutionID:string%20%3F;license:string%20%3F;maximumDepthInMeters:float%20%3F;minimumDepthInMeters:float%20%3F;parentEventID:string%20%3F;rightsHolder:string%20%3F;samplingProtocol:string%20%3F],[Occurrence]-%20eventID%201..1>[Event],[SeagrassDataset]++-%20events%200..*>[Event],[SeagrassDataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Occurrence],[MeasurementOrFact],[MeasurementOrFact]-%20eventID%201..1>[Event&#124;eventID:string;decimalLongitude:float;decimalLatitude:float;eventDate:date;footprintSRS:string%20%3F;footprintWKT:string%20%3F;bibliographicCitation:string%20%3F;coordinateUncertaintyInMeters:float%20%3F;country:string%20%3F;datasetID:string%20%3F;datasetName:string%20%3F;fieldNotes:string%20%3F;geodeticDatum:string%20%3F;habitat:string%20%3F;institutionCode:string%20%3F;institutionID:string%20%3F;license:string%20%3F;maximumDepthInMeters:float%20%3F;minimumDepthInMeters:float%20%3F;parentEventID:string%20%3F;rightsHolder:string%20%3F;samplingProtocol:string%20%3F],[Occurrence]-%20eventID%201..1>[Event],[SeagrassDataset]++-%20events%200..*>[Event],[SeagrassDataset])

## Referenced by Class

 *  **[MeasurementOrFact](MeasurementOrFact.md)** *[MeasurementOrFact➞eventID](MeasurementOrFact_eventID.md)*  <sub>1..1</sub>  **[Event](Event.md)**
 *  **[Occurrence](Occurrence.md)** *[Occurrence➞eventID](Occurrence_eventID.md)*  <sub>1..1</sub>  **[Event](Event.md)**
 *  **None** *[➞events](seagrassDataset__events.md)*  <sub>0..\*</sub>  **[Event](Event.md)**

## Attributes


### Own

 * [Event➞eventID](Event_eventID.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [decimalLongitude](decimalLongitude.md)  <sub>1..1</sub>
     * Range: [Float](types/Float.md)
 * [decimalLatitude](decimalLatitude.md)  <sub>1..1</sub>
     * Range: [Float](types/Float.md)
 * [eventDate](eventDate.md)  <sub>1..1</sub>
     * Range: [Date](types/Date.md)
 * [footprintSRS](footprintSRS.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [footprintWKT](footprintWKT.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [bibliographicCitation](bibliographicCitation.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [coordinateUncertaintyInMeters](coordinateUncertaintyInMeters.md)  <sub>0..1</sub>
     * Range: [Float](types/Float.md)
 * [country](country.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [datasetID](datasetID.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [datasetName](datasetName.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [fieldNotes](fieldNotes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [habitat](habitat.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [institutionCode](institutionCode.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [institutionID](institutionID.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [license](license.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [maximumDepthInMeters](maximumDepthInMeters.md)  <sub>0..1</sub>
     * Range: [Float](types/Float.md)
 * [minimumDepthInMeters](minimumDepthInMeters.md)  <sub>0..1</sub>
     * Range: [Float](types/Float.md)
 * [parentEventID](parentEventID.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [rightsHolder](rightsHolder.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [samplingProtocol](samplingProtocol.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | http://rs.tdwg.org/dwc/terms/Event |
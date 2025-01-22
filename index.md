
# Seagrass


**metamodel version:** 1.7.0

**version:** None





### Classes

 * [Event](Event.md)
 * [MeasurementOrFact](MeasurementOrFact.md)
 * [Occurrence](Occurrence.md)
 * [SeagrassDataset](SeagrassDataset.md)

### Mixins


### Slots

 * [basisOfRecord](basisOfRecord.md)
 * [bibliographicCitation](bibliographicCitation.md)
 * [class](class.md)
 * [coordinateUncertaintyInMeters](coordinateUncertaintyInMeters.md)
 * [country](country.md)
 * [datasetID](datasetID.md)
 * [datasetName](datasetName.md)
 * [decimalLatitude](decimalLatitude.md)
 * [decimalLongitude](decimalLongitude.md)
 * [eventDate](eventDate.md)
 * [eventID](eventID.md)
     * [Event➞eventID](Event_eventID.md)
     * [MeasurementOrFact➞eventID](MeasurementOrFact_eventID.md)
     * [Occurrence➞eventID](Occurrence_eventID.md)
 * [family](family.md)
 * [fieldNotes](fieldNotes.md)
 * [footprintSRS](footprintSRS.md)
 * [footprintWKT](footprintWKT.md)
 * [genus](genus.md)
 * [geodeticDatum](geodeticDatum.md)
 * [habitat](habitat.md)
 * [identifiedBy](identifiedBy.md)
 * [institutionCode](institutionCode.md)
 * [institutionID](institutionID.md)
 * [kingdom](kingdom.md)
 * [license](license.md)
 * [maximumDepthInMeters](maximumDepthInMeters.md)
 * [measurementAccuracy](measurementAccuracy.md)
 * [measurementDeterminedBy](measurementDeterminedBy.md)
 * [measurementDeterminedDate](measurementDeterminedDate.md)
 * [measurementID](measurementID.md)
 * [measurementMethod](measurementMethod.md)
 * [measurementType](measurementType.md)
 * [measurementTypeID](measurementTypeID.md)
 * [measurementUnit](measurementUnit.md)
 * [measurementUnitID](measurementUnitID.md)
 * [measurementValue](measurementValue.md)
 * [measurementValueID](measurementValueID.md)
 * [minimumDepthInMeters](minimumDepthInMeters.md)
 * [occurrenceID](occurrenceID.md)
     * [MeasurementOrFact➞occurrenceID](MeasurementOrFact_occurrenceID.md)
     * [Occurrence➞occurrenceID](Occurrence_occurrenceID.md)
 * [occurrenceStatus](occurrenceStatus.md)
 * [order](order.md)
 * [parentEventID](parentEventID.md)
 * [phylum](phylum.md)
 * [recordedBy](recordedBy.md)
 * [rightsHolder](rightsHolder.md)
 * [sampleSizeUnit](sampleSizeUnit.md)
 * [sampleSizeValue](sampleSizeValue.md)
 * [samplingProtocol](samplingProtocol.md)
 * [scientificName](scientificName.md)
 * [scientificNameID](scientificNameID.md)
 * [➞events](seagrassDataset__events.md)
 * [➞mof](seagrassDataset__mof.md)
 * [➞occurrences](seagrassDataset__occurrences.md)
 * [taxonRank](taxonRank.md)
 * [vernacularName](vernacularName.md)

### Enums

 * [MeasurementTypeType](MeasurementTypeType.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE

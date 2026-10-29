# GenesTranscriptsGenomicElementsAccessibleGenomicElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**strand** | **str** |  | [optional] 
**name** | **str** |  | 
**method** | **str** |  | [optional] 
**source_annotation** | **str** |  | 
**type** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genes_transcripts_genomic_elements_accessible_genomic_element import GenesTranscriptsGenomicElementsAccessibleGenomicElement

# TODO update the JSON string below
json = "{}"
# create an instance of GenesTranscriptsGenomicElementsAccessibleGenomicElement from a JSON string
genes_transcripts_genomic_elements_accessible_genomic_element_instance = GenesTranscriptsGenomicElementsAccessibleGenomicElement.from_json(json)
# print the JSON string representation of the object
print(GenesTranscriptsGenomicElementsAccessibleGenomicElement.to_json())

# convert the object into a dict
genes_transcripts_genomic_elements_accessible_genomic_element_dict = genes_transcripts_genomic_elements_accessible_genomic_element_instance.to_dict()
# create an instance of GenesTranscriptsGenomicElementsAccessibleGenomicElement from a dict
genes_transcripts_genomic_elements_accessible_genomic_element_from_dict = GenesTranscriptsGenomicElementsAccessibleGenomicElement.from_dict(genes_transcripts_genomic_elements_accessible_genomic_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



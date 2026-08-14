# GenesStructure200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**strand** | **str** |  | 
**type** | **str** |  | 
**gene_id** | **str** |  | 
**gene_name** | **str** |  | 
**transcript_id** | **str** |  | 
**transcript_name** | **str** |  | 
**protein_id** | **str** |  | [optional] 
**exon_number** | **str** |  | 
**exon_id** | **str** |  | 
**organism** | **str** |  | 
**source** | **str** |  | 
**version** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genes_structure200_response_inner import GenesStructure200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenesStructure200ResponseInner from a JSON string
genes_structure200_response_inner_instance = GenesStructure200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GenesStructure200ResponseInner.to_json())

# convert the object into a dict
genes_structure200_response_inner_dict = genes_structure200_response_inner_instance.to_dict()
# create an instance of GenesStructure200ResponseInner from a dict
genes_structure200_response_inner_from_dict = GenesStructure200ResponseInner.from_dict(genes_structure200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



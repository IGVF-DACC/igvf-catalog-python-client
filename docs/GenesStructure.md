# GenesStructure


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
from igvf_catalog_client.models.genes_structure import GenesStructure

# TODO update the JSON string below
json = "{}"
# create an instance of GenesStructure from a JSON string
genes_structure_instance = GenesStructure.from_json(json)
# print the JSON string representation of the object
print(GenesStructure.to_json())

# convert the object into a dict
genes_structure_dict = genes_structure_instance.to_dict()
# create an instance of GenesStructure from a dict
genes_structure_from_dict = GenesStructure.from_dict(genes_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



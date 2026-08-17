# GeneCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chr** | **str** |  | 
**gene_id** | **str** |  | 
**hgnc** | **str** |  | [optional] 
**name** | **str** |  | 
**organism** | **str** |  | 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.gene_compact import GeneCompact

# TODO update the JSON string below
json = "{}"
# create an instance of GeneCompact from a JSON string
gene_compact_instance = GeneCompact.from_json(json)
# print the JSON string representation of the object
print(GeneCompact.to_json())

# convert the object into a dict
gene_compact_dict = gene_compact_instance.to_dict()
# create an instance of GeneCompact from a dict
gene_compact_from_dict = GeneCompact.from_dict(gene_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



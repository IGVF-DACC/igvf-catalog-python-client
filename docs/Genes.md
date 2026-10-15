# Genes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_name** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genes import Genes

# TODO update the JSON string below
json = "{}"
# create an instance of Genes from a JSON string
genes_instance = Genes.from_json(json)
# print the JSON string representation of the object
print(Genes.to_json())

# convert the object into a dict
genes_dict = genes_instance.to_dict()
# create an instance of Genes from a dict
genes_from_dict = Genes.from_dict(genes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



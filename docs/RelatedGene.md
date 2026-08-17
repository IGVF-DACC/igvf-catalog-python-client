# RelatedGene


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
from igvf_catalog_client.models.related_gene import RelatedGene

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedGene from a JSON string
related_gene_instance = RelatedGene.from_json(json)
# print the JSON string representation of the object
print(RelatedGene.to_json())

# convert the object into a dict
related_gene_dict = related_gene_instance.to_dict()
# create an instance of RelatedGene from a dict
related_gene_from_dict = RelatedGene.from_dict(related_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



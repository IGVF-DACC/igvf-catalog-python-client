# RelatedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**uniprot_names** | **List[str]** |  | 
**files_filesets** | **str** |  | [optional] 
**chr** | **str** |  | 
**gene_id** | **str** |  | 
**hgnc** | **str** |  | [optional] 
**organism** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.related_item import RelatedItem

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedItem from a JSON string
related_item_instance = RelatedItem.from_json(json)
# print the JSON string representation of the object
print(RelatedItem.to_json())

# convert the object into a dict
related_item_dict = related_item_instance.to_dict()
# create an instance of RelatedItem from a dict
related_item_from_dict = RelatedItem.from_dict(related_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



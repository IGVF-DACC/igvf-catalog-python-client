# LinkedFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant_id** | **str** |  | 
**ranges** | **List[str]** |  | 

## Example

```python
from igvf_catalog_client.models.linked_feature import LinkedFeature

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedFeature from a JSON string
linked_feature_instance = LinkedFeature.from_json(json)
# print the JSON string representation of the object
print(LinkedFeature.to_json())

# convert the object into a dict
linked_feature_dict = linked_feature_instance.to_dict()
# create an instance of LinkedFeature from a dict
linked_feature_from_dict = LinkedFeature.from_dict(linked_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



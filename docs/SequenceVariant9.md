# SequenceVariant9


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chr** | **str** |  | 
**pos** | **float** |  | 
**rsid** | **List[str]** |  | [optional] 
**ref** | **str** |  | 
**alt** | **str** |  | 
**spdi** | **str** |  | 
**hgvs** | **str** |  | 
**ca_id** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.sequence_variant9 import SequenceVariant9

# TODO update the JSON string below
json = "{}"
# create an instance of SequenceVariant9 from a JSON string
sequence_variant9_instance = SequenceVariant9.from_json(json)
# print the JSON string representation of the object
print(SequenceVariant9.to_json())

# convert the object into a dict
sequence_variant9_dict = sequence_variant9_instance.to_dict()
# create an instance of SequenceVariant9 from a dict
sequence_variant9_from_dict = SequenceVariant9.from_dict(sequence_variant9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SequenceVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chr** | **str** |  | 
**pos** | **float** |  | 
**rsid** | **List[str]** |  | [optional] 
**ref** | **str** |  | 
**alt** | **str** |  | 
**spdi** | **str** |  | [optional] 
**hgvs** | **str** |  | [optional] 
**ca_id** | **str** |  | [optional] 
**strain** | **List[str]** |  | [optional] 
**qual** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 
**annotations** | [**VariantAnnotations**](VariantAnnotations.md) |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**organism** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.sequence_variant import SequenceVariant

# TODO update the JSON string below
json = "{}"
# create an instance of SequenceVariant from a JSON string
sequence_variant_instance = SequenceVariant.from_json(json)
# print the JSON string representation of the object
print(SequenceVariant.to_json())

# convert the object into a dict
sequence_variant_dict = sequence_variant_instance.to_dict()
# create an instance of SequenceVariant from a dict
sequence_variant_from_dict = SequenceVariant.from_dict(sequence_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



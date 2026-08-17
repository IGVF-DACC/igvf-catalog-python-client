# Motif


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**tf_name** | **str** |  | 
**length** | **float** |  | 
**pwm** | **List[List[str]]** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.motif import Motif

# TODO update the JSON string below
json = "{}"
# create an instance of Motif from a JSON string
motif_instance = Motif.from_json(json)
# print the JSON string representation of the object
print(Motif.to_json())

# convert the object into a dict
motif_dict = motif_instance.to_dict()
# create an instance of Motif from a dict
motif_from_dict = Motif.from_dict(motif_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



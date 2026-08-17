# Qtls3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**cell_types** | [**List[CellTypes]**](CellTypes.md) |  | 
**genes** | [**List[Genes2]**](Genes2.md) |  | 

## Example

```python
from igvf_catalog_client.models.qtls3 import Qtls3

# TODO update the JSON string below
json = "{}"
# create an instance of Qtls3 from a JSON string
qtls3_instance = Qtls3.from_json(json)
# print the JSON string representation of the object
print(Qtls3.to_json())

# convert the object into a dict
qtls3_dict = qtls3_instance.to_dict()
# create an instance of Qtls3 from a dict
qtls3_from_dict = Qtls3.from_dict(qtls3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



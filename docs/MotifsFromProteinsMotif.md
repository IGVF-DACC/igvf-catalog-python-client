# MotifsFromProteinsMotif


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**tf_name** | **str** |  | 
**length** | **float** |  | 
**pwm** | **List[List[MotifPwmInnerInner]]** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.motifs_from_proteins_motif import MotifsFromProteinsMotif

# TODO update the JSON string below
json = "{}"
# create an instance of MotifsFromProteinsMotif from a JSON string
motifs_from_proteins_motif_instance = MotifsFromProteinsMotif.from_json(json)
# print the JSON string representation of the object
print(MotifsFromProteinsMotif.to_json())

# convert the object into a dict
motifs_from_proteins_motif_dict = motifs_from_proteins_motif_instance.to_dict()
# create an instance of MotifsFromProteinsMotif from a dict
motifs_from_proteins_motif_from_dict = MotifsFromProteinsMotif.from_dict(motifs_from_proteins_motif_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



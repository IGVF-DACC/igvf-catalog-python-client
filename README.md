# igvf-catalog-client

Python client for the [IGVF Catalog API](https://api.catalogkg.igvf.org/).

IGVF Catalog OpenAPI compliant REST API built using tRPC with Express.

Our database uses 0-based, half-open coordinates for genomic coordinates in the GRCh38 (human) and GRCm39 (mouse) reference genomes.

Data is licensed under the <a href=https://creativecommons.org/licenses/by/4.0/ target=\"_blank\">Creative Commons license</a> and the software is licensed under the <a href=https://spdx.org/licenses/MIT.html target=\"_blank\">MIT license</a>.

- API version: 1.3.1.dev20261013000000
- Package version: 1.3.1.dev20261013000000
- Generator version: 7.14.0

This package is generated with [OpenAPI Generator](https://openapi-generator.tech) by
[igvf-catalog-client-openapi-spec](https://github.com/IGVF-DACC/igvf-catalog-client-openapi-spec)
whenever the IGVF Catalog changes. Don't edit generated files by hand; change
`templates/` here or the pipeline in that repo instead.

## Requirements

Python 3.9+

## Installation

Releases follow IGVF Catalog releases and are published to PyPI:

```sh
pip install igvf-catalog-client
```

Development builds track the catalog's `dev` branch and are installed from this repo's `dev` branch:

```sh
pip install "git+https://github.com/IGVF-DACC/igvf-catalog-python-client.git@dev"
```

The default host is the API the package was generated against: releases use
`https://api.catalogkg.igvf.org/api` and dev builds use
`https://catalog-api-dev.demo.igvf.org/api`. Pass `Configuration(host=...)` to use another.

## Quick start

```python
import igvf_catalog_client

configuration = igvf_catalog_client.Configuration(host="https://api.catalogkg.igvf.org/api")

with igvf_catalog_client.ApiClient(configuration) as api_client:
    api = igvf_catalog_client.IgvfCatalogApi(api_client)
    genes = api.genes(name="ATF3")
    print(genes[0].to_dict())
```

Every endpoint is a method on `IgvfCatalogApi`, listed below. The interactive API documentation is at
[api.catalogkg.igvf.org](https://api.catalogkg.igvf.org/).

## Getting Started

```python

import igvf_catalog_client
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://catalog-api-dev.demo.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://catalog-api-dev.demo.igvf.org/api"
)



# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str | 
    dataset = 'dataset_example' # str | 
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.all_coding_variants_from_genes(gene_id, dataset, page=page, limit=limit)
        print("The response of IgvfCatalogApi->all_coding_variants_from_genes:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IgvfCatalogApi->all_coding_variants_from_genes: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://catalog-api-dev.demo.igvf.org/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IgvfCatalogApi* | [**variants**](docs/IgvfCatalogApi.md#variants) | **GET** /variants | 
*IgvfCatalogApi* | [**coding_variants**](docs/IgvfCatalogApi.md#coding_variants) | **GET** /coding-variants | 
*IgvfCatalogApi* | [**genomic_elements**](docs/IgvfCatalogApi.md#genomic_elements) | **GET** /genomic-elements | 
*IgvfCatalogApi* | [**genes**](docs/IgvfCatalogApi.md#genes) | **GET** /genes | 
*IgvfCatalogApi* | [**genes_structure**](docs/IgvfCatalogApi.md#genes_structure) | **GET** /genes-structure | 
*IgvfCatalogApi* | [**transcripts**](docs/IgvfCatalogApi.md#transcripts) | **GET** /transcripts | 
*IgvfCatalogApi* | [**proteins**](docs/IgvfCatalogApi.md#proteins) | **GET** /proteins | 
*IgvfCatalogApi* | [**complexes**](docs/IgvfCatalogApi.md#complexes) | **GET** /complexes | 
*IgvfCatalogApi* | [**pathways**](docs/IgvfCatalogApi.md#pathways) | **GET** /pathways | 
*IgvfCatalogApi* | [**motifs**](docs/IgvfCatalogApi.md#motifs) | **GET** /motifs | 
*IgvfCatalogApi* | [**drugs**](docs/IgvfCatalogApi.md#drugs) | **GET** /drugs | 
*IgvfCatalogApi* | [**ontology_term**](docs/IgvfCatalogApi.md#ontology_term) | **GET** /ontology-terms | 
*IgvfCatalogApi* | [**studies**](docs/IgvfCatalogApi.md#studies) | **GET** /studies | 
*IgvfCatalogApi* | [**genomic_elements_from_variants**](docs/IgvfCatalogApi.md#genomic_elements_from_variants) | **GET** /variants/genomic-elements | 
*IgvfCatalogApi* | [**genes_from_variants**](docs/IgvfCatalogApi.md#genes_from_variants) | **GET** /variants/genes | 
*IgvfCatalogApi* | [**proteins_from_variants**](docs/IgvfCatalogApi.md#proteins_from_variants) | **GET** /variants/proteins | 
*IgvfCatalogApi* | [**phenotypes_from_variants**](docs/IgvfCatalogApi.md#phenotypes_from_variants) | **GET** /variants/phenotypes | 
*IgvfCatalogApi* | [**biosamples_from_variants**](docs/IgvfCatalogApi.md#biosamples_from_variants) | **GET** /variants/biosamples | 
*IgvfCatalogApi* | [**variants_from_proteins**](docs/IgvfCatalogApi.md#variants_from_proteins) | **GET** /proteins/variants | 
*IgvfCatalogApi* | [**proteins_proteins**](docs/IgvfCatalogApi.md#proteins_proteins) | **GET** /proteins/proteins | 
*IgvfCatalogApi* | [**variants_from_phenotypes**](docs/IgvfCatalogApi.md#variants_from_phenotypes) | **GET** /phenotypes/variants | 
*IgvfCatalogApi* | [**coding_variants_from_phenotypes**](docs/IgvfCatalogApi.md#coding_variants_from_phenotypes) | **GET** /phenotypes/coding-variants | 
*IgvfCatalogApi* | [**genomic_elements_from_phenotypes**](docs/IgvfCatalogApi.md#genomic_elements_from_phenotypes) | **GET** /phenotypes/genomic-elements | 
*IgvfCatalogApi* | [**variants_from_genomic_elements**](docs/IgvfCatalogApi.md#variants_from_genomic_elements) | **GET** /genomic-elements/variants | 
*IgvfCatalogApi* | [**genes_from_genomic_elements**](docs/IgvfCatalogApi.md#genes_from_genomic_elements) | **GET** /genomic-elements/genes | 
*IgvfCatalogApi* | [**phenotypes_from_genomic_elements**](docs/IgvfCatalogApi.md#phenotypes_from_genomic_elements) | **GET** /genomic-elements/phenotypes | 
*IgvfCatalogApi* | [**biosamples_from_genomic_elements**](docs/IgvfCatalogApi.md#biosamples_from_genomic_elements) | **GET** /genomic-elements/biosamples | 
*IgvfCatalogApi* | [**genomic_elements_from_genomic_elements**](docs/IgvfCatalogApi.md#genomic_elements_from_genomic_elements) | **GET** /genomic-elements/genomic-elements | 
*IgvfCatalogApi* | [**variants_from_genes**](docs/IgvfCatalogApi.md#variants_from_genes) | **GET** /genes/variants | 
*IgvfCatalogApi* | [**genomic_elements_from_genes**](docs/IgvfCatalogApi.md#genomic_elements_from_genes) | **GET** /genes/genomic-elements | 
*IgvfCatalogApi* | [**phenotypes_from_coding_variants**](docs/IgvfCatalogApi.md#phenotypes_from_coding_variants) | **GET** /coding-variants/phenotypes | 
*IgvfCatalogApi* | [**variants_from_biosamples**](docs/IgvfCatalogApi.md#variants_from_biosamples) | **GET** /biosamples/variants | 
*IgvfCatalogApi* | [**genomic_elements_from_biosamples**](docs/IgvfCatalogApi.md#genomic_elements_from_biosamples) | **GET** /biosamples/genomic-elements | 
*IgvfCatalogApi* | [**variant_by_frequency_source**](docs/IgvfCatalogApi.md#variant_by_frequency_source) | **GET** /variants/freq | 
*IgvfCatalogApi* | [**grn**](docs/IgvfCatalogApi.md#grn) | **GET** /gene-regulatory-network | 
*IgvfCatalogApi* | [**enhancer_gene_predictions**](docs/IgvfCatalogApi.md#enhancer_gene_predictions) | **GET** /enhancer-gene-predictions | 
*IgvfCatalogApi* | [**qtls**](docs/IgvfCatalogApi.md#qtls) | **GET** /qtls | 
*IgvfCatalogApi* | [**variant_summary**](docs/IgvfCatalogApi.md#variant_summary) | **GET** /variants/summary | 
*IgvfCatalogApi* | [**variants_from_variant_id_summary**](docs/IgvfCatalogApi.md#variants_from_variant_id_summary) | **GET** /variants/variant-ld/summary | 
*IgvfCatalogApi* | [**variants_region_summary**](docs/IgvfCatalogApi.md#variants_region_summary) | **GET** /variants/region-summary | 
*IgvfCatalogApi* | [**qtl_summary_endpoint**](docs/IgvfCatalogApi.md#qtl_summary_endpoint) | **GET** /variants/genes/summary | 
*IgvfCatalogApi* | [**genomic_elements_from_variants_count**](docs/IgvfCatalogApi.md#genomic_elements_from_variants_count) | **GET** /variants/predictions-count | 
*IgvfCatalogApi* | [**predictions_from_variants**](docs/IgvfCatalogApi.md#predictions_from_variants) | **GET** /variants/predictions | 
*IgvfCatalogApi* | [**deprecated_coding_variants_summary**](docs/IgvfCatalogApi.md#deprecated_coding_variants_summary) | **GET** /variants/phenotypes/score-summary | 
*IgvfCatalogApi* | [**nearest_genes**](docs/IgvfCatalogApi.md#nearest_genes) | **GET** /variants/nearest-genes | 
*IgvfCatalogApi* | [**variants_alleles**](docs/IgvfCatalogApi.md#variants_alleles) | **GET** /variants/gnomad-alleles | 
*IgvfCatalogApi* | [**variants_genomic_elements_genes**](docs/IgvfCatalogApi.md#variants_genomic_elements_genes) | **GET** /variants/genomic-elements/genes | 
*IgvfCatalogApi* | [**genomic_elements_predictions_from_variant**](docs/IgvfCatalogApi.md#genomic_elements_predictions_from_variant) | **GET** /variants/genomic-elements/cell-gene-predictions | 
*IgvfCatalogApi* | [**genes_proteins_from_variants**](docs/IgvfCatalogApi.md#genes_proteins_from_variants) | **GET** /variants/genes-proteins | 
*IgvfCatalogApi* | [**coding_variants_from_genes**](docs/IgvfCatalogApi.md#coding_variants_from_genes) | **GET** /genes/coding-variants/scores | 
*IgvfCatalogApi* | [**all_coding_variants_from_genes**](docs/IgvfCatalogApi.md#all_coding_variants_from_genes) | **GET** /genes/coding-variants/all-scores | 
*IgvfCatalogApi* | [**variants_from_gene_proteins**](docs/IgvfCatalogApi.md#variants_from_gene_proteins) | **GET** /genes-proteins/variants | 
*IgvfCatalogApi* | [**genes_proteins_genes_proteins**](docs/IgvfCatalogApi.md#genes_proteins_genes_proteins) | **GET** /genes-proteins/genes-proteins | 
*IgvfCatalogApi* | [**coding_variants_summary**](docs/IgvfCatalogApi.md#coding_variants_summary) | **GET** /coding-variants/phenotypes/score-summary | 
*IgvfCatalogApi* | [**coding_variants_count_from_gene**](docs/IgvfCatalogApi.md#coding_variants_count_from_gene) | **GET** /coding-variants/phenotypes-count | 
*IgvfCatalogApi* | [**ontology_term_parents**](docs/IgvfCatalogApi.md#ontology_term_parents) | **GET** /ontology-terms/{ontology_term_id}/parents | 
*IgvfCatalogApi* | [**ontology_term_children**](docs/IgvfCatalogApi.md#ontology_term_children) | **GET** /ontology-terms/{ontology_term_id}/children | 
*IgvfCatalogApi* | [**ontology_term_transitive_closure**](docs/IgvfCatalogApi.md#ontology_term_transitive_closure) | **GET** /ontology-terms/{ontology_term_id_start}/transitive-closure/{ontology_term_id_end} | 
*IgvfCatalogApi* | [**variants_from_variant_id**](docs/IgvfCatalogApi.md#variants_from_variant_id) | **GET** /variants/variant-ld | 
*IgvfCatalogApi* | [**coding_variants_from_variants**](docs/IgvfCatalogApi.md#coding_variants_from_variants) | **GET** /variants/coding-variants | 
*IgvfCatalogApi* | [**drugs_from_variants**](docs/IgvfCatalogApi.md#drugs_from_variants) | **GET** /variants/drugs | 
*IgvfCatalogApi* | [**disease_from_variants**](docs/IgvfCatalogApi.md#disease_from_variants) | **GET** /variants/diseases | 
*IgvfCatalogApi* | [**variants_from_coding_variants**](docs/IgvfCatalogApi.md#variants_from_coding_variants) | **GET** /coding-variants/variants | 
*IgvfCatalogApi* | [**transcripts_from_genes**](docs/IgvfCatalogApi.md#transcripts_from_genes) | **GET** /genes/transcripts | 
*IgvfCatalogApi* | [**genes_transcripts_genes**](docs/IgvfCatalogApi.md#genes_transcripts_genes) | **GET** /genes/transcripts/genes | 
*IgvfCatalogApi* | [**proteins_from_genes**](docs/IgvfCatalogApi.md#proteins_from_genes) | **GET** /genes/proteins | 
*IgvfCatalogApi* | [**pathways_from_genes**](docs/IgvfCatalogApi.md#pathways_from_genes) | **GET** /genes/pathways | 
*IgvfCatalogApi* | [**genes_genes**](docs/IgvfCatalogApi.md#genes_genes) | **GET** /genes/genes | 
*IgvfCatalogApi* | [**diseases_from_genes**](docs/IgvfCatalogApi.md#diseases_from_genes) | **GET** /genes/diseases | 
*IgvfCatalogApi* | [**genes_from_transcripts**](docs/IgvfCatalogApi.md#genes_from_transcripts) | **GET** /transcripts/genes | 
*IgvfCatalogApi* | [**proteins_from_transcripts**](docs/IgvfCatalogApi.md#proteins_from_transcripts) | **GET** /transcripts/proteins | 
*IgvfCatalogApi* | [**transcripts_from_proteins**](docs/IgvfCatalogApi.md#transcripts_from_proteins) | **GET** /proteins/transcripts | 
*IgvfCatalogApi* | [**genes_from_proteins**](docs/IgvfCatalogApi.md#genes_from_proteins) | **GET** /proteins/genes | 
*IgvfCatalogApi* | [**complexes_from_proteins**](docs/IgvfCatalogApi.md#complexes_from_proteins) | **GET** /proteins/complexes | 
*IgvfCatalogApi* | [**proteins_from_complexes**](docs/IgvfCatalogApi.md#proteins_from_complexes) | **GET** /complexes/proteins | 
*IgvfCatalogApi* | [**motifs_from_proteins**](docs/IgvfCatalogApi.md#motifs_from_proteins) | **GET** /proteins/motifs | 
*IgvfCatalogApi* | [**proteins_from_motifs**](docs/IgvfCatalogApi.md#proteins_from_motifs) | **GET** /motifs/proteins | 
*IgvfCatalogApi* | [**genes_from_pathways**](docs/IgvfCatalogApi.md#genes_from_pathways) | **GET** /pathways/genes | 
*IgvfCatalogApi* | [**pathways_from_pathways**](docs/IgvfCatalogApi.md#pathways_from_pathways) | **GET** /pathways/pathways | 
*IgvfCatalogApi* | [**annotations_from_go_terms**](docs/IgvfCatalogApi.md#annotations_from_go_terms) | **GET** /go-terms/gene-products | 
*IgvfCatalogApi* | [**go_terms_from_annotations**](docs/IgvfCatalogApi.md#go_terms_from_annotations) | **GET** /gene-products/go-terms | 
*IgvfCatalogApi* | [**variants_from_diseases**](docs/IgvfCatalogApi.md#variants_from_diseases) | **GET** /diseases/variants | 
*IgvfCatalogApi* | [**genes_from_diseases**](docs/IgvfCatalogApi.md#genes_from_diseases) | **GET** /diseases/genes | 
*IgvfCatalogApi* | [**variants_from_drugs**](docs/IgvfCatalogApi.md#variants_from_drugs) | **GET** /drugs/variants | 
*IgvfCatalogApi* | [**files_filesets**](docs/IgvfCatalogApi.md#files_filesets) | **GET** /files-filesets | 
*IgvfCatalogApi* | [**llm_query**](docs/IgvfCatalogApi.md#llm_query) | **POST** /llm-query | 

## Documentation For Models

 - [AccessibleGenomicElement](docs/AccessibleGenomicElement.md)
 - [AccessibleGenomicElementPromoterOf](docs/AccessibleGenomicElementPromoterOf.md)
 - [Annotations](docs/Annotations.md)
 - [AnnotationsFromGoTerms](docs/AnnotationsFromGoTerms.md)
 - [Biosamples](docs/Biosamples.md)
 - [BiosamplesFromGenomicElements](docs/BiosamplesFromGenomicElements.md)
 - [BiosamplesFromGenomicElementsBiosample](docs/BiosamplesFromGenomicElementsBiosample.md)
 - [BiosamplesFromGenomicElementsGenomicElement](docs/BiosamplesFromGenomicElementsGenomicElement.md)
 - [BiosamplesFromVariants](docs/BiosamplesFromVariants.md)
 - [BiosamplesFromVariantsGenomicElement](docs/BiosamplesFromVariantsGenomicElement.md)
 - [BiosamplesFromVariantsVariant](docs/BiosamplesFromVariantsVariant.md)
 - [CaddScores](docs/CaddScores.md)
 - [CellTypes](docs/CellTypes.md)
 - [CellTypes2](docs/CellTypes2.md)
 - [CodingVariant](docs/CodingVariant.md)
 - [CodingVariants](docs/CodingVariants.md)
 - [CodingVariantsFromGenes](docs/CodingVariantsFromGenes.md)
 - [CodingVariantsFromPhenotypes](docs/CodingVariantsFromPhenotypes.md)
 - [CodingVariantsSummary](docs/CodingVariantsSummary.md)
 - [Complex](docs/Complex.md)
 - [ComplexComplexAssembly](docs/ComplexComplexAssembly.md)
 - [ComplexesFromProteins](docs/ComplexesFromProteins.md)
 - [ComplexesFromProteinsComplex](docs/ComplexesFromProteinsComplex.md)
 - [ComplexesFromProteinsProtein](docs/ComplexesFromProteinsProtein.md)
 - [DiseaseFromVariants](docs/DiseaseFromVariants.md)
 - [DiseaseFromVariantsSequenceVariant](docs/DiseaseFromVariantsSequenceVariant.md)
 - [DiseasesFromGenes](docs/DiseasesFromGenes.md)
 - [DiseasesFromGenesGene](docs/DiseasesFromGenesGene.md)
 - [Drug](docs/Drug.md)
 - [DrugsFromVariants](docs/DrugsFromVariants.md)
 - [DrugsFromVariantsDrug](docs/DrugsFromVariantsDrug.md)
 - [Elements](docs/Elements.md)
 - [EnhancerGenePredictions](docs/EnhancerGenePredictions.md)
 - [EnhancerGenePredictionsElements](docs/EnhancerGenePredictionsElements.md)
 - [FilesFilesets](docs/FilesFilesets.md)
 - [Gene](docs/Gene.md)
 - [Gene4](docs/Gene4.md)
 - [Gene6](docs/Gene6.md)
 - [GeneCompact](docs/GeneCompact.md)
 - [GeneNoSynonyms](docs/GeneNoSynonyms.md)
 - [GeneRef](docs/GeneRef.md)
 - [Genes](docs/Genes.md)
 - [Genes2](docs/Genes2.md)
 - [GenesFromGenomicElements](docs/GenesFromGenomicElements.md)
 - [GenesFromGenomicElementsGene](docs/GenesFromGenomicElementsGene.md)
 - [GenesFromGenomicElementsGenomicElement](docs/GenesFromGenomicElementsGenomicElement.md)
 - [GenesFromGenomicElementsPValue](docs/GenesFromGenomicElementsPValue.md)
 - [GenesFromPathways](docs/GenesFromPathways.md)
 - [GenesFromPathwaysPathway](docs/GenesFromPathwaysPathway.md)
 - [GenesFromProteins](docs/GenesFromProteins.md)
 - [GenesFromTranscripts](docs/GenesFromTranscripts.md)
 - [GenesFromTranscriptsTranscript](docs/GenesFromTranscriptsTranscript.md)
 - [GenesFromVariants](docs/GenesFromVariants.md)
 - [GenesFromVariantsSequenceVariant](docs/GenesFromVariantsSequenceVariant.md)
 - [GenesFromVariantsStudy](docs/GenesFromVariantsStudy.md)
 - [GenesGenes](docs/GenesGenes.md)
 - [GenesGenesGene1](docs/GenesGenesGene1.md)
 - [GenesProteinsFromVariants](docs/GenesProteinsFromVariants.md)
 - [GenesProteinsGenesProteins](docs/GenesProteinsGenesProteins.md)
 - [GenesStructure](docs/GenesStructure.md)
 - [GenesTranscriptsGenes](docs/GenesTranscriptsGenes.md)
 - [GenesTranscriptsGenesTranscript](docs/GenesTranscriptsGenesTranscript.md)
 - [GenomicElement](docs/GenomicElement.md)
 - [GenomicElement2](docs/GenomicElement2.md)
 - [GenomicElement4](docs/GenomicElement4.md)
 - [GenomicElement5](docs/GenomicElement5.md)
 - [GenomicElement7](docs/GenomicElement7.md)
 - [GenomicElement9](docs/GenomicElement9.md)
 - [GenomicElementFull](docs/GenomicElementFull.md)
 - [GenomicElementsFromGenomicElements](docs/GenomicElementsFromGenomicElements.md)
 - [GenomicElementsFromGenomicElementsPerturbedGenomicElement](docs/GenomicElementsFromGenomicElementsPerturbedGenomicElement.md)
 - [GenomicElementsFromPhenotypes](docs/GenomicElementsFromPhenotypes.md)
 - [GenomicElementsFromPhenotypesPhenotype](docs/GenomicElementsFromPhenotypesPhenotype.md)
 - [GenomicElementsFromVariants](docs/GenomicElementsFromVariants.md)
 - [GenomicElementsPredictionsFromVariant](docs/GenomicElementsPredictionsFromVariant.md)
 - [Grn](docs/Grn.md)
 - [IdName](docs/IdName.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObjectIssuesInner](docs/InlineObjectIssuesInner.md)
 - [LinkedFeature](docs/LinkedFeature.md)
 - [LlmQuery](docs/LlmQuery.md)
 - [LlmQueryRequest](docs/LlmQueryRequest.md)
 - [MethodCount](docs/MethodCount.md)
 - [MethodsAndContexts](docs/MethodsAndContexts.md)
 - [Motif](docs/Motif.md)
 - [MotifsFromProteins](docs/MotifsFromProteins.md)
 - [MotifsFromProteinsMotif](docs/MotifsFromProteinsMotif.md)
 - [NearestGene](docs/NearestGene.md)
 - [NearestGenes](docs/NearestGenes.md)
 - [OntologyTerm](docs/OntologyTerm.md)
 - [OntologyTermBasic](docs/OntologyTermBasic.md)
 - [OntologyTermChildren](docs/OntologyTermChildren.md)
 - [OntologyTermTransitiveClosure](docs/OntologyTermTransitiveClosure.md)
 - [Paths](docs/Paths.md)
 - [Pathway](docs/Pathway.md)
 - [PathwaysFromPathways](docs/PathwaysFromPathways.md)
 - [Phenotype](docs/Phenotype.md)
 - [PhenotypeRef](docs/PhenotypeRef.md)
 - [PhenotypesFromVariants](docs/PhenotypesFromVariants.md)
 - [PhenotypesFromVariants37](docs/PhenotypesFromVariants37.md)
 - [PhenotypesFromVariantsStudy](docs/PhenotypesFromVariantsStudy.md)
 - [PhenotypesFromVariantsVariant](docs/PhenotypesFromVariantsVariant.md)
 - [Predictions](docs/Predictions.md)
 - [Predictions2](docs/Predictions2.md)
 - [PredictionsFromVariants](docs/PredictionsFromVariants.md)
 - [Protein](docs/Protein.md)
 - [ProteinBasic](docs/ProteinBasic.md)
 - [ProteinChange](docs/ProteinChange.md)
 - [ProteinCompact](docs/ProteinCompact.md)
 - [ProteinComplexOption](docs/ProteinComplexOption.md)
 - [ProteinsFromTranscripts](docs/ProteinsFromTranscripts.md)
 - [ProteinsFromTranscriptsProtein](docs/ProteinsFromTranscriptsProtein.md)
 - [ProteinsFromVariants](docs/ProteinsFromVariants.md)
 - [ProteinsFromVariantsBiosampleTerm](docs/ProteinsFromVariantsBiosampleTerm.md)
 - [ProteinsFromVariantsProteinComplex](docs/ProteinsFromVariantsProteinComplex.md)
 - [ProteinsProteins](docs/ProteinsProteins.md)
 - [ProteinsProteinsProtein1](docs/ProteinsProteinsProtein1.md)
 - [QtlSummaryEndpoint](docs/QtlSummaryEndpoint.md)
 - [Qtls](docs/Qtls.md)
 - [Qtls3](docs/Qtls3.md)
 - [Related](docs/Related.md)
 - [RelatedGene](docs/RelatedGene.md)
 - [RelatedItem](docs/RelatedItem.md)
 - [RelatedSources](docs/RelatedSources.md)
 - [Scores](docs/Scores.md)
 - [SequenceVariant](docs/SequenceVariant.md)
 - [SequenceVariant9](docs/SequenceVariant9.md)
 - [Sources](docs/Sources.md)
 - [Sources4](docs/Sources4.md)
 - [Study](docs/Study.md)
 - [Study2](docs/Study2.md)
 - [StudyParameters](docs/StudyParameters.md)
 - [Summary](docs/Summary.md)
 - [TargetGene](docs/TargetGene.md)
 - [TfBinding](docs/TfBinding.md)
 - [Transcript](docs/Transcript.md)
 - [Variant](docs/Variant.md)
 - [VariantAnnotations](docs/VariantAnnotations.md)
 - [VariantBasic](docs/VariantBasic.md)
 - [VariantMinimal](docs/VariantMinimal.md)
 - [VariantRef](docs/VariantRef.md)
 - [VariantSummary](docs/VariantSummary.md)
 - [Variants](docs/Variants.md)
 - [VariantsAllelesValue](docs/VariantsAllelesValue.md)
 - [VariantsFromDrugs](docs/VariantsFromDrugs.md)
 - [VariantsFromPhenotypesItem](docs/VariantsFromPhenotypesItem.md)
 - [VariantsFromVariantID](docs/VariantsFromVariantID.md)
 - [VariantsFromVariantIDSequenceVariant](docs/VariantsFromVariantIDSequenceVariant.md)
 - [VariantsFromVariantIDSummary](docs/VariantsFromVariantIDSummary.md)
 - [VariantsGenomicElementsGenes](docs/VariantsGenomicElementsGenes.md)
 - [VariantsRegionSummary](docs/VariantsRegionSummary.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization"></a>
### Authorization

- **Type**: Bearer authentication


## Author

encode-help@lists.stanford.edu



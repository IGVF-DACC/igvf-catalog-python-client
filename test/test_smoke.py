"""Offline checks that the generated client imports and exposes the API."""

from importlib.metadata import version

import igvf_catalog_client


def test_version_matches_metadata():
    assert igvf_catalog_client.__version__ == version("igvf_catalog_client")


def test_api_methods():
    with igvf_catalog_client.ApiClient() as api_client:
        api = igvf_catalog_client.IgvfCatalogApi(api_client)
        for name in ["genes", "variants", "genes_from_variants", "llm_query"]:
            assert callable(getattr(api, name))


def test_configuration_host():
    configuration = igvf_catalog_client.Configuration(host="https://example.org/api")
    assert configuration.host == "https://example.org/api"

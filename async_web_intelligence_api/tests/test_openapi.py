from pathlib import Path

import yaml


def test_openapi_contract_exists_and_is_valid():
    contract_path = (
        Path(__file__).parents[1] / "openapi.yaml"
    )

    assert contract_path.exists()

    contract = yaml.safe_load(
        contract_path.read_text(
            encoding="utf-8-sig"
        )
    )

    assert contract["openapi"] == "3.1.1"

    assert "info" in contract
    assert "paths" in contract
    assert "components" in contract

    assert "/crawl" in contract["paths"]
    assert "/health" in contract["paths"]
    assert "/results" in contract["paths"]


def test_crawl_endpoint_contract():

    contract_path = (
        Path(__file__).parents[1] / "openapi.yaml"
    )

    contract = yaml.safe_load(
        contract_path.read_text(
            encoding="utf-8-sig"
        )
    )

    crawl = contract["paths"]["/crawl"]["post"]

    assert "requestBody" in crawl
    assert "responses" in crawl

    request_schema = (
        crawl["requestBody"]["content"]
        ["application/json"]["schema"]
    )

    assert "urls" in request_schema["properties"]
    assert "urls" in request_schema["required"]


def test_required_schemas_exist():

    contract_path = (
        Path(__file__).parents[1] / "openapi.yaml"
    )

    contract = yaml.safe_load(
        contract_path.read_text(
            encoding="utf-8-sig"
        )
    )

    schemas = contract["components"]["schemas"]

    assert "CrawlResponse" in schemas
    assert "CrawlResult" in schemas
    assert "MovieData" in schemas
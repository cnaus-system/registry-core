PYTHON ?= python3

.PHONY: help validate validate-conformance validate-feed jsonlint

help:
	@echo "Targets:"
	@echo "  make validate              - run all non-core validation checks"
	@echo "  make validate-conformance  - run conformance validator runner"
	@echo "  make validate-feed         - basic feed.json structural checks"
	@echo "  make jsonlint              - parse-check key JSON files"

validate: jsonlint validate-conformance validate-feed
	@echo "PASS: validate"

validate-conformance:
	@$(PYTHON) tools/validator/validate_conformance.py

validate-feed:
	@$(PYTHON) tools/validator/validate_feed.py

jsonlint:
	@$(PYTHON) -m json.tool feed.json > /dev/null
	@$(PYTHON) -m json.tool Conformance/manifest.json > /dev/null
	@$(PYTHON) -m json.tool schemas/revocation.schema.json > /dev/null
	@$(PYTHON) -m json.tool schemas/registry.schema.json > /dev/null
	@$(PYTHON) -m json.tool schemas/proof.schema.json > /dev/null
	@$(PYTHON) -m json.tool schemas/feed.schema.json > /dev/null
	@echo "OK: jsonlint"

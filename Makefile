PYTHON ?= python3

.PHONY: smoke manifest verify clean

smoke:
	$(PYTHON) scripts/run_smoke_tests.py

manifest:
	$(PYTHON) scripts/build_packet_manifest.py

verify:
	$(PYTHON) scripts/verify_manifest.py

clean:
	rm -rf tmp

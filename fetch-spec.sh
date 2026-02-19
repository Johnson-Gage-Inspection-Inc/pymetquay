#!/usr/bin/env bash
curl "https://app.swaggerhub.com/apiproxy/registry/metquayinc-c94/Metquay.API.CRUD/1.0.0-jgi?format=json" > 1.0.json
python -c "import json; data = json.load(open('1.0.json')); json.dump(data, open('1.0.json', 'w'), ensure_ascii=False, indent=4)"
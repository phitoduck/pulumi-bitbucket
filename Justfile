set dotenv-load := true

install:
    python -m pip install -e .

pulumi-up:
    #!/bin/bash
    pulumi up --yes -v 3 --stack repogen

    # this was logging the github access token to out.txt!!! very bad. Luckily GitHub auto-revokes those
    # pulumi up --logtostderr --logflow -v=9 2> out.txt

pulumi-destroy:
    #!/bin/bash
    pulumi destroy --skip-preview --yes --stack repogen

pulumi-cancel:
    pulumi cancel


generate-bitbucket-cloud-api-python-client:
    #!/bin/bash
    BITBUCKET_CLOUD_OPENAPI_JSON_URL="https://api.bitbucket.org/swagger.json"
    
    # I used swagger.io to convert the openapi v2 swagger.json that bitbucket
    # uses to the newer OpenAPI v3 version which this tool supports
    pipx run openapi-python-client generate --path ./bitbucket.openapi3.yaml


update-project:
    python .projenrc.py

build:
    #!/bin/bash
    python -m pip install build
    python -m build --wheel

publish-test:
    twine upload \
        --repository-url "https://test.pypi.org/legacy/" \
        --username "$TEST_PYPI__TWINE_USERNAME" \
        --password "$TEST_PYPI__TWINE_PASSWORD" \
        --verbose \
        dist/*

publish-prod:
    twine upload \
        --repository-url "https://upload.pypi.org/legacy/" \
        --username "$TWINE_USERNAME" \
        --password "$TWINE_PASSWORD" \
        --verbose \
        dist/*

clean:
    rm -rf dist/ build/
    
release: update-project clean build publish-test publish-prod
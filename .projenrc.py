from phito_projen import PythonPackage

project = PythonPackage(
    name="pulumi-bitbucket-py",
    module_name="bitbucket_iac",
    version="0.0.0",
    install_requires=[
        "pulumi>=3.0.0,<4.0.0",
        "pynacl",
        "atlassian-python-api",
        "GitPython",
        "python-dotenv",
        "phitoduck-projen",
        "typer",
        "rich",
        "requests",
    ],
    entrypoints={"bitbucket": "bitbucket_iac.cli:run"}
)
project.gitignore.add_patterns("!sample.env")

project.synth()
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graphql_starwars",
    version="0.1",
    author="Roman Aliyev",
    description="Another GraphQL example with Star Wars data",
    packages=setuptools.find_packages(),
    install_requires=["werkzeug", "graphql-core"],
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RomanAliyev/graphql-starwars",
    include_package_data=True,
)

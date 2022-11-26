import pathlib
import re
import setuptools

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding="utf8")

with open(HERE / "SpendScheme/__init__.py") as file:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), re.MULTILINE).group(1)

setuptools.setup(
    name = "SpendScheme",
    author = "Jupiter404E",
    url = "https://github.com/Jupiter404E/SpendScheme",
    version = version,
    packages = setuptools.find_packages(),
    license = "MIT",
    description = "SpendScheme is a microframework for text formatting in Python 3",
    long_description = README,
    long_description_content_type = "text/markdown",
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        "random"
    ],
    test_suite = "tests",
    project_urls = {
        "Documentation (GitHub)": "https://github.com/Jupiter404E/SpendScheme/blob/main/README.md",
        "Source (GitHub)": "https://github.com/Jupiter404E/SpendScheme",
    },
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Communications :: Chat",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ]
)

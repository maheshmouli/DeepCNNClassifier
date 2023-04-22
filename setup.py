import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.3"

REPOSITORY_NAME = "DeepCNNClassifier"
AUTHOR_USER_NAME = "Mouli Siramdasu"
SRC_REPOSITORY = "DEEPCNNCLASSIFIER"
AUTHOR_EMAIL = "maheshmouli225@gmail.com"

setuptools.setup(
    name=SRC_REPOSITORY,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python Package for CNN App",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPOSITORY_NAME}",
    project_urls ={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPOSITORY_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)